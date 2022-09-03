for x in ('Good morning!', 123, 45.6, print):
    print(f'{x=}') # xには↑の()内の値が順次代入されていく
    print(f'{type(x)=}')