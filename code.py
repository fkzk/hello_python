message = 'Good morning!'
# "#"以降はプログラムに影響しないコメント（写しても写さなくてもOK）
print(f'{message=}') # Python3.8～　変数名=値　の表示が可能（以降多用する）
print(f'{type(message)=}') # type(変数名)で変数の型を調べられる
number = 123
print(f'{number=}')
print(f'{type(number)=}')
number = 45.6 # すでに使われている変数名の場合は上書きされる
print(f'{number=}')
print(f'{type(number)=}')
print_fn = print # 関数も代入可能
print(f'{print_fn=}')
print(f'{type(print_fn)=}')