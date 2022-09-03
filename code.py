start = 3
end = 13
step = 2
for c_type in (tuple, list):
    print(f'// {c_type=}')
    numbers = c_type(range(15)) # rangeをtuple型やlist型に変換する
    print(f'// {numbers=}')
    print(f'// {start=}, {end=}, {step=}')
    print('')

    print(f'** {start}番目から({end}-1)番目までを{step}個おきに取り出す **')
    print(f'{numbers[start:end:step]=}')
    print('')

    print(f'** {start}番目以降を取り出す **')
    print(f'{numbers[start:]=}')
    print('')

    print(f'** ({end}-1)番目までを{step}個おきに取り出す **')
    print(f'{numbers[:end:step]=}')
    print('')

    print('** 逆順にする **')
    print(f'{numbers[::-1]=}')
    print('')