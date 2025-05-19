# Dockerfile

## sudoコマンドを強引に利用したい場合

`Dockerfile`を以下のように追記する

```Dockerfile
# jovyan パスワード
ARG PASSWORD=password

# ユーザー設定
RUN echo "jovyan:${PASSWORD}" | chpasswd && \
    echo "jovyan ALL=(ALL) ALL" >> /etc/sudoers
```

### 例

```diff 
# イメージの構築
FROM base

+ # jovyan パスワード
+ ARG PASSWORD=password

# root ユーザーに切り替え
USER root

+ # ユーザー設定
+ RUN echo "jovyan:${PASSWORD}" | chpasswd && \
+     echo "jovyan ALL=(ALL) ALL" >> /etc/sudoers

# 作業ディレクトリの設定
WORKDIR /home/jovyan/work
```

## Pythonパッケージのインストール内容を変更したい場合

`requirements.txt`を編集する

## フォントのインストール内容を変更したい場合

`fonts.txt`を編集する
