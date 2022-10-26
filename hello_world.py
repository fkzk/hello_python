message = 'Hello, World!'
message_list = [
    'message',
    message,
    f'{message}',
    f'メッセージ: {message}',
    f'{message = }'
]
for item in message_list:
    print(item)
print('繰り返し終了')