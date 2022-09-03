def add_tax(price): # 関数名は動詞（原形）から始めるのが基本。 _ で単語をつなぐ
    tax = round(price * 0.10) # roundやprintはPythonが用意したbuilt-in関数
    price = price + tax
    return price

class Fruit:
    def __init__(self, jp, en, price): # __init__はインスタンス作成時に呼ばれる
        self.names = {'jp': jp, 'en': en}
        self.price = price

    def print(self, lang='jp'): # 子クラスからも利用可能
        name = self.names[lang]
        print(f'{name}: {self.price}円')

class PeelableFruit(Fruit): # Fruitは親クラス, PeelableFruitは子クラス
    def __init__(self, jp, en, price, way='ナイフ'):
        super().__init__(jp, en, price) # 親クラス（Fruit）の__init__を実行
        self.way = way # 親クラスにない処理を書き足せる

    def peel(self, lang='jp'): # 親クラスにない関数も追加できる
        name = self.names[lang]
        print(f'{self.way}で{name}の皮をむいた')

def print_money(yen):
    # 変数 = Trueのときに代入される値 if 真偽値 else Falseのときに代入される値
    message = f'{yen}円も持ってる!' if yen > 2000 else f'{yen}円しか持ってない…'
    print(message)

def print_fruit(fruit, max_price):
    if fruit[2] < max_price / 4:
        print(f'{fruit[0]}: {fruit[2]}円！安い！')
    elif fruit[2] < max_price: # ifの条件がFalseの場合評価され、Trueなら実行
        print(f'{fruit[0]}: {fruit[2]}円')
    else: # ifの条件にもelifの条件（複数可）にも当てはまらない場合に実行
        print(f'{fruit[0]}: {fruit[2]}円…買えない…')

def main_fruits():
    fruits = [
        PeelableFruit('リンゴ', 'apple', 479), # __init__のself以外の引数を指定
        PeelableFruit('みかん', 'orange', 339, '手'), 
        Fruit('いちご', 'strawberry', 2064),
        PeelableFruit('バナナ', 'banana', 185, '手'),
    ]
    peach = PeelableFruit('もも', 'peach', 837) # インスタンスはもちろん代入できる
    fruits.append(peach) # listクラスのappend関数を呼び出している
    for fruit in fruits:
        fruit.print() # Fruitクラス内で定義したprint関数はPeelableFruitに継承される
        if isinstance(fruit, PeelableFruit): # PeelableFruitのインスタンスかどうか
            fruit.peel()
        else:
            print(f'{fruit.names["jp"]}は皮をむけない')
        print('')

def normalize(x, y): # 引数を複数設定可能
    r = (x**2 + y**2)**(0.5) # ** は累乗
    ex = x / r # / は割り算（結果はfloat）
    ey = y / r
    return ex, ey # 複数の返り値もOK（tupleとして返される）

def main_normalize():
    x = 3
    y = 4
    v = (x, y)
    ex, ey = normalize(x, y) # 分割して受け取れる
    e = normalize(*v) # 入出力ともにまとめてもOK
    print(f'{(x, y)=}')
    print(f'{(ex, ey)=}')
    print(f'{e=}, {type(e)}')

def affine(x, a, b=0): # bは指定されなければ0が使われる
    return a*x+b

def main_affine():
    x_in, a_in, b_in = 3, 2, 5 # まとめて代入できる（読みにくくならないよう注意）
    print(f'{(x_in, a_in, b_in)=}')
    print(f'{affine(x_in, a_in)=}') # キーワード引数 b は省略可能
    print(f'{affine(x_in, a_in, b=b_in)=}')
    print(f'{affine(x_in, a_in, b_in)=}') # 順番通り並べれば=は不要
    print(f'{affine(b=b_in, a=a_in, x=x_in)=}') # =を使えば順番が変わってもよい

def main_affine_lambda():
    # lambda 引数: 戻り値  （ラムダ式）によって簡単な関数が書ける
    lambda_affine = lambda x, a, b=0: x*a+b
    print(f'{type(lambda_affine)=}')
    x_in, a_in, b_in = 3, 2, 5
    print(f'{(x_in, a_in, b_in)=}')
    print(f'{lambda_affine(x_in, a_in)=}')
    print(f'{lambda_affine(b=b_in, a=a_in, x=x_in)=}')

def main_dict():
    d = {
        'x': 3, # 'key': valueの形で対応する値を記録
        'a': 2,
        'b': 5,
    }

    for key in d.keys(): # d.keys()の代わりにdのみでも同じ結果となる
        print(f'{key=}')

    for value in d.values():
        print(f'{value=}')

    for key, value in d.items():
        print(f'{key=}, {value=}, {d[key]=}')

def one_hour_true():
    print('～1時間後～')
    return True

def one_sec_false():
    print('～1秒後～')
    return False

def main_bool():
    b1 = 2 < 3
    b2 = 2 == 3
    print(f'{b1=}, {not b1=}')
    print(f'{b2=}, {not b2=}')

main_fruits()