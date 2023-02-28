import re
data = {'times': '2023-02-28T18:46:08.070254Z',
        'messages': 'G-046063 是您的 Google 驗證碼。'}
code = verification_code = data['messages'].split(' ')[0][2:]

print(code)
