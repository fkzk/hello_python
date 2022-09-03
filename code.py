x_tuple = ('Hello', 123, 45.6, print) # tuple: ()で囲って列挙
print(f'{x_tuple=}')
fruits_list = ['リンゴ', 'みかん', 'バナナ'] # list: []で囲って列挙
print(f'{fruits_list=}')
for i in (0, 2, -1):
    print(f'** {i=}番目の要素を表示 **')
    print(f'{x_tuple[i]=}')
    print(f'{fruits_list[i]=}')
fruits_list[0] = 'いちご' # listは要素を指定して代入できる
print(f'{fruits_list=}') # 0番目（最初）の要素が 'リンゴ' → 'いちご' に
x_tuple[0] = 'Good morning!' # tupleは要素に代入できないのでエラーが出る