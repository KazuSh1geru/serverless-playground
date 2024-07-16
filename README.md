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

## エラー対応1: docker build でエラーが出る

解決策: 認証情報取得のエラーが出たので、以下のコマンドを実行する。

```bash
brew install docker-credential-helper
```

## エラー対応2: sam build でエラーが出る
```bash
sam build

Building codeuri: /Users/xxx/workspace/serverless-playground/lambda/hello-sam runtime: None metadata:
{'Dockerfile': 'Dockerfile', 'DockerContext':
'/Users/xxx/workspace/serverless-playground/lambda/hello-sam/hello_world', 'DockerTag': 'python3.12-v1'}
architecture: arm64 functions: HelloWorldFunction
Building image for HelloWorldFunction function

Build Failed
Error: Building image for HelloWorldFunction requires Docker. is Docker running?
```

解決策: .zshrcに環境変数を作成して、DOCKER_HOSTを指定する.
```bash
docker context ls

NAME                DESCRIPTION                               DOCKER ENDPOINT               KUBERNETES ENDPOINT   ORCHESTRATOR
rancher-desktop *   Rancher Desktop moby context              unix:///Users/xxx-xxx/.rd/docker.sock 
```

```bash: .zshrc
export DOCKER_HOST=unix:///Users/xxx-xxx/.rd/docker.sock
```


[参考サイト](https://dev.classmethod.jp/articles/aws-sam-cli-resolve-docker-error/)


