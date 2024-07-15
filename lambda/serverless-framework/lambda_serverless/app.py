import json
from openai import OpenAI


# OpenAI APIキーを環境変数から取得
client = OpenAI()

def lambda_handler(event, context):
    # OpenAI APIを呼び出してHello Worldメッセージを生成
    messages = [
        {
            "role": "system",
            "content": "Hello, how can I help you today?"
        },
    ]
    response = client.chat.completions.create(
        model="gpt-4o",
        # hello worldを入力
        messages=messages,
    )

    # 生成されたメッセージを取得
    message = response.choices[0].message.content

    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': message
        })
    }


if __name__ == "__main__":
    event = {}
    context = {}
    print(lambda_handler(event, context))