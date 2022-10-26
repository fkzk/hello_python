class Fruit:
    def __init__(self, jp, en, price): # 初期化用, selfは作成されるインスタンス（実例）
        self.jp = jp # peachという変数ならpeach.jp = jpに相当
        self.en = en
        self.price = price

    def print_info(self, with_tax=False):
        # [演習] オプションで消費税8%を加えた表示にできるよう書き換え
        if with_tax:
            price = int(self.price * 1.08) # 小数からintクラスのオブジェクトを作成
            postfix = '（税込）'
        else:
            price = self.price
            postfix = '（税抜）'
        print(f'{self.jp}({self.en}): {price}円{postfix}')

def main():
    fruits = [ # a list of tuples
        Fruit('リンゴ', 'apple', 479), # __init__が実行される。第1引数のselfは省略
        Fruit('みかん', 'orange', 339),
        Fruit('いちご', 'strawberry', 2064),
        Fruit('バナナ', 'banana', 185),
    ]
    peach = Fruit('もも', 'peach', 837)
    fruits.append(peach) # peach.append('山梨県')は失敗 -> tupleだとappendできない
    # [演習] fruitsの中身を展開して「No. i: fruit」の形式でprint
    for fruit in fruits:
        fruit.print_info()

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