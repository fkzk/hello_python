items = ('Good morning!', 123, 45.6, print) # 繰り返しの対象をひとつの変数に代入
print(f'{items=}')
print(f'{type(items)=}')
for x in items:
    print(f'{x=}') # xには↑の()内の値が順次代入されていく