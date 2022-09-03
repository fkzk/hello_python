fruits1 = [ # このlistの各データの順番が入れ替わったり追加・削除されても違和感がない
    ('リンゴ', 'apple', 479), # ('apple', 479, 'リンゴ')に変えると変
    ('みかん', 'orange', 339), # ('みかん', 'orange', 339, '愛媛')に変えると変
    ('いちご', 'strawberry', 2064), # ('いちご', 2064)に変えると変
    ('バナナ', 'banana', 185), # 最後の要素の後にコンマをつけてもOK
]
print(f'{fruits1=}')

# これまでに習ったやり方で日本語の名前だけのリストを作る
fruits_jp = []
for fruit in fruits1:
    fruits_jp.append(fruit[0])
print(f'{fruits_jp=}')

# リスト内包表記
fruits_en = [fruit[1] for fruit in fruits1] # 1行で英語の名前のリストを作れる
print(f'{fruits_en=}')
fruits_yen_with_tax = [int(fruit[2] * 1.10) for fruit in fruits1] # * はかけ算
print(f'{fruits_yen_with_tax=}')
