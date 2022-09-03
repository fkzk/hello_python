x_tuple = ('Hello', 123, 45.6, print) # tuple: ()で囲って列挙
print(f'** {type(x_tuple)}の中身をfor文で展開 **')
for x in x_tuple:
    print(f'{x=}')

fruits_list = ['リンゴ', 'みかん', 'バナナ'] # list: []で囲って列挙
print(f'** {type(fruits_list)}の中身をfor文で展開 **')
for fruit in fruits_list:
    print(f'{fruit}を食べた')