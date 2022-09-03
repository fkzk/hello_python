fruits1 = [ # このlistの各データの順番が入れ替わったり追加・削除されても違和感がない
    ('リンゴ', 'apple', 479), # ('apple', 479, 'リンゴ')に変えると変
    ('みかん', 'orange', 339), # ('みかん', 'orange', 339, '愛媛')に変えると変
    ('いちご', 'strawberry', 2064), # ('いちご', 2064)に変えると変
    ('バナナ', 'banana', 185), # 最後の要素の後にコンマをつけてもOK
]
print(f'{fruits1=}')
print('')

peach = ('もも', 'peach', 837)
fruits1.append(peach) # listの末尾に要素をひとつ追加
print(f'peachをappendした結果: {fruits1=}')

fruits2 = [
    ('さくらんぼ', 'cherry', 1867),
    ('レモン', 'lemon', 459),
]
print(f'{fruits2=}')
print('')

print(f'{fruits1+fruits2=}') # + でlistを結合できる（tupleでも可）
print(f'{fruits2+fruits1=}') # + の前後の順番で結果が変わる
print('')

print(f'{fruits1=}') # さっきの + では中身は変化していない
fruits1.extend(fruits2) # listの末尾に別のlistを結合して追加
print(f'fruit2をextendした結果: {fruits1=}') # extendにより中身が変化
print('')

peach.append('山梨') # tupleはappendが使えないのでエラー