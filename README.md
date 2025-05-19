# devcontainer-jupyter-latex-template

## Overview

Jupyter Notebook環境とLaTeX・Markdown・Marpの執筆環境をDevcontainerで簡単に構築できるテンプレート

AMD64向けの `jupyter/datascience-notebook:x86_64-ubuntu-22.04` をベースイメージとしている（ARMには未対応）

イメージサイズは約20GB（2025/5時点）

本リポジトリおよび付随するソースコード・設定ファイル等の利用によって生じた損害や問題について作成者は一切責任を負わない

> [!WARNING]
> 本リポジトリは生成AI（Claude 3.7 Sonnet, o4-mini-high）を活用して作成された

## Requirement

- [Docker](https://www.docker.com/)
- [VS Code](https://code.visualstudio.com/) または [Cursor](https://www.cursor.com/ja/)
- [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

## Usage

1. 本リポジトリをクローン
1. VS CodeまたはCursorでリポジトリを開き「コンテナーで再度開く」を選択
1. 必要なDockerイメージのビルド・起動が自動的に行われる（初回は時間がかかる）Jupyter NotebookおよびLaTeX・Markdown・Marpの執筆環境が利用可能

## Features

Devcontainerで以下の環境を構築可能

- VS CodeまたはCursorから利用できるJupyter Notebook環境
- LaTeX執筆環境（フォーマッタは未導入ひとまずコンパイルが通るレベル）
- Markdown・Marp執筆環境

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
        ├── Sample(一部は別レポジトリから配置)
        └── mylib
```

## Reference

### 公式ドキュメント

- [Visual Studio Code documentation](https://code.visualstudio.com/docs)
- [docker docs](https://matsuand.github.io/docs.docker.jp.onthefly/desktop/)
- [Dev Containers docs](https://code.visualstudio.com/docs/devcontainers/containers)
- [devcontainer.json reference](https://containers.dev/implementors/json_reference/)
- [Marp theme beam](https://github.com/rnd195/my-marp-themes)

### VS Code Extensions

- [Extensions for Visual Studio Code](https://marketplace.visualstudio.com/vscode)

- Common
  - [ics.japanese-proofreading](https://marketplace.visualstudio.com/items?itemName=ics.japanese-proofreading)

- Python, Jupyter Notebook
  - [ms-python.python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
  - [ms-python.vscode-pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)
  - [ms-toolsai.jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter)

- LaTeX
  - [james-yu.latex-workshop](https://marketplace.visualstudio.com/items?itemName=james-yu.latex-workshop)

- Markdown
  - [yzhang.markdown-all-in-one](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one)
  - [davidanson.vscode-markdownlint](https://marketplace.visualstudio.com/items?itemName=davidanson.vscode-markdownlint)
  - [shd101wyy.markdown-preview-enhanced](https://marketplace.visualstudio.com/items?itemName=shd101wyy.markdown-preview-enhanced)
  - [yzane.markdown-pdf](https://marketplace.visualstudio.com/items?itemName=yzane.markdown-pdf)

- Mermaid
  - [bierner.markdown-mermaid](https://marketplace.visualstudio.com/items?itemName=bierner.markdown-mermaid)
  - [bpruitt-goddard.mermaid-markdown-syntax-highlighting](https://marketplace.visualstudio.com/items?itemName=bpruitt-goddard.mermaid-markdown-syntax-highlighting)
  - [corschenzi.mermaid-graphical-editor](https://marketplace.visualstudio.com/items?itemName=corschenzi.mermaid-graphical-editor)

- Marp
  - [marp-team.marp-vscode](https://marketplace.visualstudio.com/items?itemName=marp-team.marp-vscode)

### Dev Containerの作り方

- <https://zenn.dev/secondselection/articles/how_to_devcontainer>

### 各種設定

#### VS Code便利設定

- <https://qiita.com/htcd/items/21266f6472ac2c39933e>
- <https://zenn.dev/owayo/articles/70814e23ab3cfb>

#### LaTeX関連

- <https://github.com/SoRA-X7/latex-devcontainer-termpaper>

#### Markdown関連

- <https://qiita.com/satshout/items/1d0d179f7188454a115c>
