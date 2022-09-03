def add_tax(price): # 関数名は動詞（原形）から始めるのが基本。 _ で単語をつなぐ
    tax = round(price * 0.10) # roundやprintはPythonが用意したbuilt-in関数
    price = price + tax
    return price

def main_fruits():
    fruits1 = [ # このlistの各データの順番が入れ替わったり追加・削除されても違和感がない
        ('リンゴ', 'apple', 479), # ('apple', 479, 'リンゴ')に変えると変
        ('みかん', 'orange', 339), # ('みかん', 'orange', 339, '愛媛')に変えると変
        ('いちご', 'strawberry', 2064), # ('いちご', 2064)に変えると変
        ('バナナ', 'banana', 185), # 最後の要素の後にコンマをつけてもOK
    ]
    print(f'{fruits1=}')

    fruits_yen_with_tax = [add_tax(fruit[2]) for fruit in fruits1] # 処理が明快に
    print(f'{fruits_yen_with_tax=}')
    print('')

    for fn in (add_tax, print, round):
        print(f'{fn.__name__}: {type(fn)}') # 関数.__name__で関数名がわかる

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

main_affine()