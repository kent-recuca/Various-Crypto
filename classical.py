# -*- coding: utf-8 -*-
import caesar as cs
def main(mode):
    if mode == "C":
        cs.caesar.main()
    else:
        print("Bye")
        return
    return

if __name__ == '__main__':
    mode = input("[C]aesar,[V]igenere, MODE:")
    main(mode)