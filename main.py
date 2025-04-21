import random
from Crypto.Cipher import AES
import base64
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
import tkinter as tk
from tkinter import ttk
import time
from back import caesar_challenge, vigenere_challenge, xor_challenge, AES_challenge, DES_challenge, challenge_rsa




def start():
    print("Choose difficulty level: Easy / Medium / Hard")
    level = input("Your choice: ").lower()

    print("Choose cipher type:")
    print("1. Caesar Cipher")
    print("2. Vigenere Cipher")
    print("3. XOR Cipher")
    print("4. AES Algorithm")
    print("5. DES Algorithm")
    print("6. RSA Algorithm")
    cipher_choice = input("Enter number: ").strip()


    if cipher_choice == "1":
        caesar_challenge(level)
    elif cipher_choice == "2":
        vigenere_challenge()
    elif cipher_choice == "3":
        xor_challenge()
    elif cipher_choice == "4":
        AES_challenge(level)
    elif cipher_choice == "5":
        DES_challenge()
    elif cipher_choice == "6":
        challenge_rsa()
    else:
        print("Unknown cipher type.")


if __name__ == "__main__":
    start()
