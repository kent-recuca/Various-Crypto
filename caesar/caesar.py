# -*- coding: utf-8 -*-
def main():
    direction = input("[E]ncode,[D]ecode: ")
    inputtext = input("INPUTTEXT: ")
    key = input("KEY(Number or [A]ll): ")
    print("OUTPUTTEXT: ",end="")
    if direction == "E":
        print(decrypt(inputtext, key))
    elif direction == "D":
        print(encrypt(inputtext, key))
    else:
        return

def encrypt(txt, key):
    if key == 'A':
        ciphertexts = list()
        for i in range(1,26):
            ciphertext = ""
            for j in list(txt):
                if 'A' <= j <= 'Z':
                    ciphertext += chr((ord(j) - ord('A') - i) % 26 + ord('A'))
                elif 'a' <= j <= 'z':
                    ciphertext += chr((ord(j) - ord('a') - i) % 26 + ord('a'))
                elif '0' <= j <= '9':
                    ciphertext += chr((ord(j) - ord('0') - i) % 10 + ord('0'))
                else:
                    ciphertext += j
            ciphertexts.append(ciphertext)
        return ciphertexts
    else:
        key = int(key)
        ciphertext = ""
        for j in list(txt):
            if 'A' <= j <= 'Z':
                ciphertext += chr((ord(j) - ord('A') - key) % 26 + ord('A'))
            elif 'a' <= j <= 'z':
                ciphertext += chr((ord(j) - ord('a') - key) % 26 + ord('a'))
            elif '0' <= j <= '9':
                ciphertext += chr((ord(j) - ord('0') - key) % 10 + ord('0'))
            else:
                ciphertext += j
        return ciphertext

def decrypt(txt, key):
    if key == 'A':
        plaintexts = list()
        for i in range(1,26):
            plaintext = ""
            for j in list(txt):
                if 'A' <= j <= 'Z':
                    plaintext += chr((ord(j) - ord('A') + i) % 26 + ord('A'))
                elif 'a' <= j <= 'z':
                    plaintext += chr((ord(j) - ord('a') + i) % 26 + ord('a'))
                elif '0' <= j <= '9':
                    plaintext += chr((ord(j) - ord('0') - i) % 10 + ord('0'))
                else:
                    plaintext += j
            plaintexts.append(plaintext)
        return plaintexts
    else:
        key = int(key)
        plaintext = ""
        for j in list(txt):
            if 'A' <= j <= 'Z':
                plaintext += chr((ord(j) - ord('A') + key) % 26 + ord('A'))
            elif 'a' <= j <= 'z':
                plaintext += chr((ord(j) - ord('a') + key) % 26 + ord('a'))
            elif '0' <= j <= '9':
                plaintext += chr((ord(j) - ord('0') - key) % 10 + ord('0'))
            else:
                plaintext += j
        return plaintext

if __name__ == '__main__':
    main()