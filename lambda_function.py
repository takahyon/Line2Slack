import json

def lambda_handler(event, context):
    # TODO implement
    body = str(get_line_message(event))
    return {
        'statusCode': 200,
        # テストで日本語も使いたいためensure_asciiをFalseにして \uXXXXを回避
        'body': json.dumps(body, ensure_ascii=False)
    }
# Lineから送られてきたメッセージを抽出するメソッド
def get_line_message(event):
    return event["events"][0]["message"]["text"]
