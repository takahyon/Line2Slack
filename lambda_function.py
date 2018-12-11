import json
import urllib

def lambda_handler(event, context):
    # TODO implement
    body = str(get_line_message(event))
    post_slack(body)
    return {
        'statusCode': 200,
        # テストで日本語も使いたいためensure_asciiをFalseにして \uXXXXを回避
        'body': json.dumps(body, ensure_ascii=False)
    }
# Lineから送られてきたメッセージを抽出するメソッド
def get_line_message(event):
    b = event["body"]
    try:
        jos = json.loads(b)
        return jos["events"][0]["message"]["text"]
    except:
        return b

def post_slack(text):
    # ここにslack botの incoming webhook URLを入れる
    url = "https://hooks.slack.com. your slack webhook URL"
    method = "POST"

    # slackにはlineのテキストを転送するだけ
    item = {
        "text":str(text)
    }
    # SlackにPOSTする
    header = {"Content-Type" : "application/json"}
    json_data = json.dumps(item).encode("utf-8")
    request = urllib.request.Request(url, data= json_data, method=method, headers=header)
    with urllib.request.urlopen(request) as response:
        response_body = response.read().decode("utf-8")
