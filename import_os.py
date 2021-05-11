import os
import time


def main():
    content = '顯示系統'
    while True:
        os.system('cls')
        time.sleep(2)
        
        print(content)
        content = content[1:] + content[0]

if __name__ == '__main__':
    main()
