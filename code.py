items = ('Good morning!', 123, 45.6, print) # 繰り返しの対象をひとつの変数に代入
for i, x in enumerate(items): # enumerateで囲うことにより何番目のループかわかる
    print(f'{i}回目のループ {x=}') # iは0から始まる