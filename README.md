# serverless-playground

# SSO を用いた AWS CLIへのログイン

```bash
$ aws sso login --profile admin-role
```

# docker: 環境構築
前提
- Rancher Desktopを用いる

使用する docker イメージをビルドする。
```bash
docker build -t test_image .

=> ERROR [internal] load metadata for public.ecr.aws/lambda/python:3.12
```
認証情報取得のエラーが出たので、以下のコマンドを実行する。

```bash
brew install docker-credential-helper
```
