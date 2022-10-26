import math # mathはPythonの標準モジュールの1つ

def main():
    a = 5
    b = 3
    c = 4
    print(f'{a = }, {b = }, {c = }')
    print(f'{a + b = }') # 足し算
    print(f'{b + c = }') # 引き算
    print(f'{a + b * c = }') # かけ算は足し算より先に計算
    print(f'{(a + b) * c = }') # ( )で優先順位を変えられる
    print(f'{a / b = }') # 普通の割り算
    print(f'{a // b = }') # 整除算（あまりを無視した商）
    print(f'{a % b = }') # aをbで割ったときのあまり
    print(f'{a ** b = }') # aのb乗

def affine(x, a, b = 0):
    return a * x + b

def input_kwargs():
    kwargs = dict(a = 1, x = 2, b = 3) # {'a': 1, 'x': 2, 'b': 3}と同じ
    print(f'{affine(**kwargs) = }') # **dict名 で一気に引数を指定

def poly(data):
    print(f'{data}を多項式フィッティングで回帰')

def gp(data):
    print(f'{data}をガウス過程回帰で回帰')

def nn(data):
    print(f'{data}をニューラルネットワークで回帰')

def switch_regressor():
    method = 'poly' # 回帰方法の指定
    regressors = {
        'poly': poly,
        'gp': gp,
        'nn': nn,
    }
    regressor = regressors[method] # regressorはpoly関数になる
    data = 'データ'
    f_x = regressor(data) # poly(data)が呼び出されている

def introduce_dict():
    fruits = { # 'key': value の形式で列挙
        'apple': Fruit('リンゴ', 'apple', 479),
        'orange': PeelableFruit('みかん', 'orange', 339),
    }
    fruits['peach'] = PeelableFruit('もも', 'peach', 837) # 要素の追加
    for key, value in fruits.items(): # .keys()や.values()もある
        print(f'{key = }')
        value.print_info(with_tax = True)

def use_math():
    root2 = math.sqrt(2)
    pi = math.pi
    print(f'{root2 = }')
    print(f'{pi = }')

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

class PeelableFruit(Fruit):
    def peel(self):
        print(f'{self.jp}の皮を手で剥いた')

def print_fruits():
    fruits = [ # a list of tuples
        Fruit('リンゴ', 'apple', 479), # __init__が実行される。第1引数のselfは省略
        PeelableFruit('みかん', 'orange', 339),
        Fruit('いちご', 'strawberry', 2064),
        PeelableFruit('バナナ', 'banana', 185),
    ]
    peach = PeelableFruit('もも', 'peach', 837)
    fruits.append(peach) # peach.append('山梨県')は失敗 -> tupleだとappendできない
    # [演習] fruitsの中身を展開して「No. i: fruit」の形式でprint
    for fruit in fruits:
        if isinstance(fruit, PeelableFruit): # PeelableFruitのfruitなら
            fruit.peel()
        fruit.print_info() # PeelableFruitもprint_infoが使える

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