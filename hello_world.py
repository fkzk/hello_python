message = 'Hello, World!'
message_list = [
    'message',
    message,
    f'{message}',
    f'メッセージ: {message}',
    f'{message = }', # 実は最後の要素に,をつけてもOK
]
# スライドでは個々より上の部分を次から省略

def is_small(num, th=3): # define（定義する）のdef
    return num < th

for i_loop, item in enumerate(message_list):
    if is_small(i_loop, th=1):
        print('最初のループ', end= ' / ') # print関数にも引数がある
    elif is_small(i_loop): # thは省略可能（3として扱う）
        print('もう少しがんばろう', end=' / ') # endの初期値は改行コード
    print(f'{i_loop}回目のループ: {item}')