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
