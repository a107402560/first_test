# import base64
#
# from Cryptodome.Cipher import AES
#
#
# key = '9346618975164281'
# password = 'helloworld'
# # text = 'helloworld      '
#
# if len(password) == 16:
#     text = password
# elif len(password) < 16:
#     text = password + (16 - len(password)) * ' '
# else:
#     text = 'error'
# encryption_suite = AES.new(key.encode('utf-8'), AES.MODE_ECB)
# cipher_text = encryption_suite.encrypt(text.encode('utf-8'))
# print(cipher_text)
# print(base64.b64encode(cipher_text).decode('utf-8'))

from cryptography.fernet import Fernet

key = Fernet.generate_key()
source = '我哦哦哦.//‘’。-*'
fn = Fernet(key)
en_result = fn.encrypt(source.encode('utf-8'))  # encode将字符串转为bytes格式
de_result = fn.decrypt(en_result)
print(en_result, de_result.decode('utf-8'))  # 反之
