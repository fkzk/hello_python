message = 'Hello, World!'
message_list = [
    'message',
    message,
    f'{message}',
    f'メッセージ: {message}',
    f'{message = }', # 実は最後の要素に,をつけてもOK
]
# スライドでは個々より上の部分を次から省略
for item in message_list:
    print(item)