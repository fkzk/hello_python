def main():
    fruits = [ # a list of tuples
        ('リンゴ', 'apple', 479),
        ('みかん', 'orange', 339),
        ('いちご', 'strawberry', 2064),
        ('バナナ', 'banana', 185),
    ]
    peach = ('もも', 'peach', 837)
    fruits.append(peach) # peach.append('山梨県')は失敗 -> tupleだとappendできない
    # [演習] fruitsの中身を展開して「No. i: fruit」の形式でprint
    for i, fruit in enumerate(fruits):
        print(f'No. {i}: {fruit}')

def check_types():
    # ( )の中を,区切りで列挙したものをtupleという
    # hello_world.pyで定義していたのは[ ]で囲ったlist
    item_tuple = (
        1, 1.0, "1.0", True, False, None, print
    )
    print(f'{type(item_tuple) = }')
    print(f'{item_tuple = }')
    print('')
    # [演習]以下にtupleの中身それぞれについて上と同様に型・値を表示するコードを書く
    for item in item_tuple:
        print(f'{type(item) = }')
        print(f'{item = }')
        print('')

if __name__ == '__main__': # sandbox.pyを直接実行したら
    main()