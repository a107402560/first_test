from sanic.response import json, text
from cryptography.fernet import Fernet


key = Fernet.generate_key()
fn = Fernet(key)


async def encrypt(request):

    if request.method == 'POST':
        password = request.json['text']
        en_result = fn.encrypt(password.encode('utf-8'))
        return json({'state': 'success', 'result': en_result.decode('utf-8')})
        # if len(password) == 16:
        #     source_text = password
        # elif len(password) < 16:
        #     source_text = password + (16 - len(password)) * ' '
        # else:
        #     source_text = 'error'
        # if source_text != 'error':
        #     encryption_suite = AES.new(key.encode('utf-8'), AES.MODE_ECB)
        #     cipher_text = encryption_suite.encrypt(source_text.encode('utf-8'))
        #     print(base64.b64encode(cipher_text).decode('utf-8'))
        #     return json({'state': 'success', 'result': base64.b64encode(cipher_text).decode('utf-8')})
        # else:
        #     return json({'state': 'error', 'result': '密码过长（一次性加密大于16字符）'})
    if request.method == 'OPTIONS':
        # print('sssss')
        return text("Hello, cross-origin-world!")


async def decrypt(request):
    if request.method == 'POST':
        try:
            cipher_text = request.json['text']
            de_result = fn.decrypt(cipher_text.encode('utf-8'))
            return json({'state': 'success', 'result': de_result.decode('utf-8')})
        except:
            return json({'state': 'error', 'result': '解密出错，请输入完整正确的密文'})

        # decryption_suite = AES.new(key.encode('utf-8'), AES.MODE_ECB)
        # plain_text = decryption_suite.decrypt(base64.b64decode(cipher_text.encode('utf-8')))
        # return json({'state': 'success', 'result': plain_text.decode('utf-8').strip()})

    if request.method == 'OPTIONS':
        return text("Hello, cross-origin-world!")