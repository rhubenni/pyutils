import nacl.secret
import nacl.utils
import nacl.pwhash
import hashlib
import codecs


def Encrypt(salt, pwl):
    hashkey = hashlib.md5(salt.encode("utf-8")).digest() + hashlib.md5(codecs.encode(salt, 'rot_13').encode("utf-8")).digest()
    box = nacl.secret.SecretBox(hashkey)
    message = pwl.encode()
    encrypted = box.encrypt(message)
    return encrypted


def Decrypt(salt, pwl):
    hashkey = hashlib.md5(salt.encode("utf-8")).digest() + hashlib.md5(codecs.encode(salt, 'rot_13').encode("utf-8")).digest()
    box = nacl.secret.SecretBox(hashkey)
    plaintext = box.decrypt(pwl).decode()
    return plaintext
