# -*- coding: utf-8 -*-
import various as va
def main():
    mode = input("[C]aesar,[S]ubstitution,[V]igenere, MODE: ")
    if mode == "C":
        va.caesar.main()
    elif mode == "S":
        va.substitution.main()
    else:
        print("Bye")
        return
    return

if __name__ == '__main__':
    main()