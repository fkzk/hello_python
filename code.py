message = 'Good morning!'
print(message)
print(f'{message}')
# "#"以降はプログラムに影響しないコメント（写しても写さなくてもOK）
print(f'message') # {}で囲っていないのでそのまま"message"と表示される
print(f'朝の挨拶：{message}') # 文字列の中に値が代入される
print(f'{message=}') # Python3.8～　変数名=値　の表示が可能（以降多用する）