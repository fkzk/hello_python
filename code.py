message = 'Good morning!'
# "#"以降はプログラムに影響しないコメント（写しても写さなくてもOK）
print(f'{message=}') # Python3.8～　変数名=値　の表示が可能（以降多用する）
number = 123
print(f'{number=}')
number = 45.6 # すでに使われている変数名の場合は上書きされる
print(f'{number=}')
print_fn = print # 関数も代入可能
print(f'{print_fn=}')
print_fn(f'{message=}')
おまけ = '変数名は日本語でも大丈夫（使わないほうがいい）'
print(f'{おまけ=}')