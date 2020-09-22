from random import SystemRandom
import pyAesCrypt
import string
import des


def get_key(length=18):
    random = SystemRandom()

    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


def encrypt_aes(input_path, output_path, key):
    pyAesCrypt.encryptFile(input_path, output_path, key, 65536)


def decrypt_aes(input_path, output_path, key):
    pyAesCrypt.decryptFile(input_path, output_path, key, 65536)


def encrypt_des(input_path, output_path, key):
    key = des.DesKey(key.encode('utf8'))

    with open(input_path, 'rb') as input_file:
        contents = input_file.read()
    
    with open(output_path, 'wb') as output_file:
        output_file.write(key.encrypt(contents, padding=True))


def decrypt_des(input_path, output_path, key):
    key = des.DesKey(key.encode('utf8'))

    with open(input_path, 'rb') as input_file:
        contents = input_file.read()
    
    with open(output_path, 'wb') as output_file:
        output_file.write(key.decrypt(contents, padding=True))


algorithms = {
    'AES-256': {
        'Encrypt': encrypt_aes,
        'Decrypt': decrypt_aes,
        'get_key': get_key,
        'length': 18,
    },

    'DES': {
        'Encrypt': encrypt_des,
        'Decrypt': decrypt_des,
        'get_key': get_key,
        'length': 24,
    },
}
