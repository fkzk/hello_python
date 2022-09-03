fruits1 = [ # このlistの各データの順番が入れ替わったり追加・削除されても違和感がない
    ('リンゴ', 'apple', 479), # ('apple', 479, 'リンゴ')に変えると変
    ('みかん', 'orange', 339), # ('みかん', 'orange', 339, '愛媛')に変えると変
    ('いちご', 'strawberry', 2064), # ('いちご', 2064)に変えると変
    ('バナナ', 'banana', 185), # 最後の要素の後にコンマをつけてもOK
]
print(f'{fruits1=}')

def add_tax(price): # 関数名は動詞（原形）から始めるのが基本。 _ で単語をつなぐ
    tax = round(price * 0.10) # roundやprintはPythonが用意したbuilt-in関数
    price = price + tax
    return price

fruits_yen_with_tax = [add_tax(fruit[2]) for fruit in fruits1] # 処理が明快に
print(f'{fruits_yen_with_tax=}')
print('')

for fn in (add_tax, print, round):
    print(f'{fn.__name__}: {type(fn)}') # 関数.__name__で関数名がわかる