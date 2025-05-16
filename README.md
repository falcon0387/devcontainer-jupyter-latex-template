# devcontainer-jupyter-latex

## はじめに

このリポジトリは、AIを活用してコーディングを行ったプログラミング初学者の学生が作成しました。  
また、dockerコンテナ内での動作確認や開発作業を簡単にするため、`ARG PASSWORD=password` のように非常に単純なパスワードを設定しています(セキュリティレベルは低いため、本番環境や外部公開には絶対に使わないでください)。  
本リポジトリおよび付随するソースコード・設定ファイル等の利用によって生じた損害や問題について、作成者は一切責任を負いません。ご利用は自己責任でお願いします。

`jupyter/datascience-notebook:x86_64-ubuntu-22.04` イメージをベースにしているため、**x86_64アーキテクチャ専用**です。**armアーキテクチャ(Apple Siliconなど)では動作しません**のでご注意ください。

Dockerfileでビルドするとイメージサイズは約20GBです(2025/5現在)。

## 前提環境

利用には以下の環境が必要です。

- [Docker](https://www.docker.com/)(x86_64アーキテクチャ対応)がインストールされていること
- [Visual Studio Code (VS Code)](https://code.visualstudio.com/) または [Cursor](https://www.cursor.com/ja/) エディタがインストールされていること
- [Dev Containers拡張機能](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)がインストールされていること

## 目的

- Devcontainerで以下の環境を構築
  - Jupyter Notebook 環境を VS Code (Cursor) から利用
  - LaTeX 執筆環境
  - Markdown・Marp 執筆環境 

## ディレクトリ階層構造
```
devcontainer-jupyter-latex
├── .devcontainer
│   ├── docker-compose.yml
│   ├── devcontainer.json
│   └── jupyter
│       ├── Dockerfile
│       ├── requirements.txt
│       └── start-xvfb.sh
└── jupyter
    ├── .vscode
    │   ├── marp
    │   │   └── latex_beamer_style.css
    │   └── launch.json
    └── src
        ├── Sample
        └── mylib
```

## 主要な設定ファイル

### `.devcontainer/docker-compose.yml`
```yaml
services:
  jupyter-latex:
    image: jupyter-latex:1.0
    container_name: jupyter-latex
    environment:
      - TZ=Asia/Tokyo
      - PYTHONPATH=/home/jovyan/work/src:${PYTHONPATH}
    build: ./jupyter
    working_dir: /home/jovyan/work
    volumes:
      - ../jupyter:/home/jovyan/work
    stdin_open: true
    tty: true
```

### `.devcontainer/devcontainer.json`
```json
{
    "name": "jupyter-latex",
    "dockerComposeFile": "docker-compose.yml",
    "service": "jupyter-latex",
    "workspaceFolder": "/home/jovyan/work",
    "remoteUser": "jovyan",
    "customizations": {
      "vscode": {
        "extensions": [
          // Python, Jupyter Notebook
          "ms-python.python",
          "ms-python.vscode-pylance",
          "ms-toolsai.jupyter",
          // LaTeX
          "james-yu.latex-workshop",
          // Markdown
          "shd101wyy.markdown-preview-enhanced",
          // Mermaid
          "bierner.markdown-mermaid",
          "bpruitt-goddard.mermaid-markdown-syntax-highlighting",
          "corschenzi.mermaid-graphical-editor",
          // Marp
          "marp-team.marp-vscode"
        ],
        "settings": {
          // Editor settings
          "editor.tabSize": 2,
          "workbench.colorTheme": "Default Dark Modern",
          
          // Python, Jupyter Notebook
          "python.defaultInterpreterPath": "/opt/conda/bin/python",
          "python.analysis.extraPaths": [
            "/home/jovyan/work/src/mylib"
          ],
  
          // LaTeX
          "latex-workshop.latex.outDir": "output",
          "latex-workshop.latex.autoBuild.run": "onSave",
  
          "latex-workshop.latex.recipes": [
            {
              "name": "lualatex",
              "tools": [
                "lualatex"
              ]
            }
          ],
  
          "latex-workshop.latex.tools": [
            {
              "name": "lualatex",
              "command": "lualatex",
              "args": [
                "--cmdx",
                "-file-line-error",
                "-synctex=1",
                "-interaction=nonstopmode",
                "-halt-on-error",
                "-output-directory=%OUTDIR%",
                "%DOC%"
              ],
              "env": {}
            }
          ],

          // Markdown Preview Enhanced
          "markdown-preview-enhanced.chromePath": "/usr/bin/google-chrome-stable",
          "markdown-preview-enhanced.enableScriptExecution": true,
          "markdown-preview-enhanced.hideDefaultVSCodeMarkdownPreviewButtons": false,
          
          // Marp
          "markdown.marp.browserPath": "/usr/bin/google-chrome-stable",
          "markdown.marp.html": "all",
          "markdown.marp.themes": [
            ".vscode/marp/latex_beamer_style.css"
          ]
        }
      }
    }
}
```

### `.devcontainer/jupyter/start-xvfb.sh`
```bash
#!/bin/bash
Xvfb :99 -screen 0 1920x1080x24 -ac +extension GLX +render -noreset &
export DISPLAY=:99
sleep 5
exec "$@"
```

### `.devcontainer/jupyter/Dockerfile`
```dockerfile
# イメージの準備
FROM texlive/texlive:latest AS texlive
FROM jupyter/datascience-notebook:x86_64-ubuntu-22.04 AS base

# メタ情報
LABEL maintainer="falcon"
LABEL version="1.0"
LABEL description="Using Jupyter and TeX within Docker from Cursor"

# イメージの構築
FROM base

# jovyan パスワード
ARG PASSWORD=password

# root ユーザーに切り替え
USER root

# ユーザー設定
RUN echo "jovyan:${PASSWORD}" | chpasswd && \
    echo "jovyan ALL=(ALL) ALL" >> /etc/sudoers

# 作業ディレクトリの設定
WORKDIR /home/jovyan/work

# texliveイメージからLaTeXをコピー
# `apt install texlive-full`による直接インストールは時間がかかる上にパッケージ不足となることがある。
# そのため、すでにLaTeXがインストール済みのtexliveイメージを利用する。
COPY --from=texlive /usr/local/texlive /usr/local/texlive

# TexLive の設定
# - バージョンを動的に取得
# - PATH を環境変数に追加
RUN TEXLIVE_YEAR=$(ls -1 /usr/local/texlive | grep -E '^[0-9]{4}$' | sort -n | tail -n 1) && \
    echo "PATH=/usr/local/texlive/${TEXLIVE_YEAR}/bin/x86_64-linux:${PATH}" >> /etc/environment && \
    /usr/local/texlive/${TEXLIVE_YEAR}/bin/x86_64-linux/tlmgr path add

# 基本パッケージのインストール
# - xvfb: 仮想ディスプレイサーバー
# - ghostscript: EPS to PDF変換
# - nodejs: JavaScript実行環境
# - wget: ファイルダウンロード用
# - gnupg: 署名鍵管理
# - openssl: セキュリティ通信ライブラリ
# - ca-certificates: 証明書管理
# - libnss3: ネットワークセキュリティサービス
# - libharfbuzz0b: テキストレンダリングライブラリ
# - libfreetype6: フォントレンダリングライブラリ
# - libfontconfig1: フォント設定ライブラリ
# - fonts-noto-cjk: 日本語フォント
# - fonts-noto: Notoフォント
# - fonts-noto-color-emoji: 絵文字フォント
# - fonts-freefont-ttf: フリーフォント
# - fonts-ipafont-gothic: IPAゴシックフォント
# - fonts-ipafont-mincho: IPA明朝フォント
# - fonts-mplus: M+フォント
RUN apt-get update && \
    apt-get install -y \
    xvfb \
    ghostscript \
    nodejs \
    wget \
    gnupg \
    openssl \
    ca-certificates \
    libnss3 \
    libharfbuzz0b \
    libfreetype6 \
    libfontconfig1 \
    fonts-noto-cjk \
    fonts-noto \
    fonts-noto-color-emoji \
    fonts-freefont-ttf \
    fonts-ipafont-gothic \
    fonts-ipafont-mincho \
    fonts-mplus \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Google Chromeリポジトリの設定
# - Chromeブラウザをインストールするための公式リポジトリを追加
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google.list

# Google Chromeのインストール
RUN apt-get update && \
    apt-get install -y google-chrome-stable && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Puppeteer環境設定
# - PUPPETEER_SKIP_CHROMIUM_DOWNLOAD: PuppeteerによるChrome自動ダウンロードをスキップ
# - PUPPETEER_EXECUTABLE_PATH: Puppeteerで利用するChromeのパス
# - PUPPETEER_ARGS: Chromeの起動オプション
# - DISPLAY: 仮想ディスプレイ番号
ENV PUPPETEER_SKIP_CHROMIUM_DOWNLOAD=true \
    PUPPETEER_EXECUTABLE_PATH=/usr/bin/google-chrome-stable \
    PUPPETEER_ARGS="--no-sandbox --disable-setuid-sandbox --disable-dev-shm-usage" \
    DISPLAY=:99

# Puppeteerのインストール
RUN npm install -g puppeteer

# 仮想ディスプレイ起動スクリプトをコピー
COPY start-xvfb.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/start-xvfb.sh

# Python パッケージのインストール
COPY requirements.txt .
RUN pip install -U pip && \
    pip install -r requirements.txt && \
    rm requirements.txt

# Jupyter設定
# - Pythonカーネルの登録
# - デフォルトカーネルの設定
RUN python -m ipykernel install --sys-prefix --name 'python3' --display-name "Python 3 (/opt/conda/bin/python)" && \
    echo "c.MultiKernelManager.default_kernel_name = 'python3'" >> /etc/jupyter/jupyter_server_config.py

# 通常ユーザーに戻す
USER jovyan

# コンテナ起動コマンド
CMD ["/usr/local/bin/start-xvfb.sh", "jupyter", "lab"]
```

### `.devcontainer/jupyter/requirements.txt`
```text
dotenv
japanize_matplotlib
nbconvert
openai
pyppeteer
```
