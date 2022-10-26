message = 'Hello, World!'
message_list = [
    'message',
    message,
    f'{message}',
    f'メッセージ: {message}',
    f'{message = }', # 実は最後の要素に,をつけてもOK
]
# スライドでは個々より上の部分を次から省略
for i_loop, item in enumerate(message_list):
    if i_loop == 0: # == は”等しいかどうか"を判定
        print('最初のループ')
    elif i_loop < 3:
        print('もう少しがんばろう') # 0回目では実行されない
    print(f'{i_loop}回目のループ: {item}')