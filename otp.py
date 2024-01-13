# -*- coding: utf-8 -*-
"""Otp.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1L7O0Mb8_26kO5R5UKtRYSeLWiPHdE5s-
"""

def otp_encrypt(plaintext, key):
    encrypted_text = ""
    for i in range(len(plaintext)):
        char = chr(ord(plaintext[i]) ^ ord(key[i % len(key)]))
        encrypted_text += char
    return encrypted_text

def otp_decrypt(ciphertext, key):
    decrypted_text = ""
    for i in range(len(ciphertext)):
        char = chr(ord(ciphertext[i]) ^ ord(key[i % len(key)]))
        decrypted_text += char
    return decrypted_text

plaintext = input("Masukkan plainteks: ").upper()
key = input("Masukkan kunci.: ").upper()

hasil_enkripsi = otp_encrypt(plaintext, key)
hasil_dekripsi = otp_decrypt(hasil_enkripsi, key)

print("\nHasil Enkripsi:", hasil_enkripsi)
print("Hasil Dekripsi:", hasil_dekripsi)