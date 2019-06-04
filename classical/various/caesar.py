# -*- coding: utf-8 -*-
def encrypt(ptxt, key):
    if key == 'A':
        ctxts = list()
        for i in range(1,26):
            ctxt = ""
            for j in list(ptxt):
                if 'A' <= j <= 'Z':
                    ctxt += chr((ord(j) - ord('A') - i) % 26 + ord('A'))
                elif 'a' <= j <= 'z':
                    ctxt += chr((ord(j) - ord('a') - i) % 26 + ord('a'))
                elif '0' <= j <= '9':
                    ctxt += chr((ord(j) - ord('0') - i) % 10 + ord('0'))
                else:
                    ctxt += j
            ctxts.append(ctxt)
        return ctxts
    else:
        key = int(key)
        ctxt = ""
        for j in list(ptxt):
            if 'A' <= j <= 'Z':
                ctxt += chr((ord(j) - ord('A') - key) % 26 + ord('A'))
            elif 'a' <= j <= 'z':
                ctxt += chr((ord(j) - ord('a') - key) % 26 + ord('a'))
            elif '0' <= j <= '9':
                ctxt += chr((ord(j) - ord('0') - key) % 10 + ord('0'))
            else:
                ctxt += j
        return ctxt

def decrypt(ctxt, key):
    if key == 'A':
        ptxts = list()
        for i in range(1,26):
            ptxt = ""
            for j in list(ctxt):
                if 'A' <= j <= 'Z':
                    ptxt += chr((ord(j) - ord('A') + i) % 26 + ord('A'))
                elif 'a' <= j <= 'z':
                    ptxt += chr((ord(j) - ord('a') + i) % 26 + ord('a'))
                elif '0' <= j <= '9':
                    ptxt += chr((ord(j) - ord('0') - i) % 10 + ord('0'))
                else:
                    ptxt += j
            ptxts.append(ptxt)
        return ptxts
    else:
        key = int(key)
        ptxt = ""
        for j in list(ctxt):
            if 'A' <= j <= 'Z':
                ptxt += chr((ord(j) - ord('A') + key) % 26 + ord('A'))
            elif 'a' <= j <= 'z':
                ptxt += chr((ord(j) - ord('a') + key) % 26 + ord('a'))
            elif '0' <= j <= '9':
                ptxt += chr((ord(j) - ord('0') - key) % 10 + ord('0'))
            else:
                ptxt += j
        return ptxt

def main():
    mode = input("[E]ncode,[D]ecode: ")
    inputtext = input("INPUTTEXT: ")
    key = input("KEY([0-9] or [A]ll): ")
    print("OUTPUTTEXT: ",end="")
    if mode == "E":
        print(decrypt(inputtext, key))
    elif mode == "D":
        print(encrypt(inputtext, key))
    else:
        return

if __name__ == '__main__':
    main()
