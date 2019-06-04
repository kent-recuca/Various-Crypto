# -*- coding: utf-8 -*-
def key(dst):
    key = {
        "src": "abcdefghijklmnopqrstuvwxyz",
        "dst": dst
    }
    return key

def encrypt(ptxt, key):
    ctxt = ""
    for p in ptxt:
        if p in key["src"]:
            i = key["src"].index(p)
            ctxt += key["dst"][i]
        else:
            ctxt += p
    return ctxt

def decrypt(ctxt, key):
    ptxt = ""
    for c in ctxt:
        if c in key["dst"]:
            i = key["dst"].index(c)
            ptxt += key["src"][i]
        else:
            ptxt += c
    return ptxt

def main():
    mode = input("[E]ncode,[D]ecode: ")
    dst = input("DESTINATION KEY: ")
    table = key(dst)
    if 26 > len(table["dst"]):
        print("key insufficient")
        return
    inputtext = input("INPUTTEXT: ")
    if mode == "E":
        print(encrypt(inputtext, table))
    elif mode == "D":
        print(decrypt(inputtext, table))
    else:
        return

if __name__ == '__main__':
    main()