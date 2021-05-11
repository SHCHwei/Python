import random

def main():
    content = '請猜數字，_A_B A為正確，B為錯誤'
    Ans = [
        random.choice('1234567980'),
        random.choice('1234567980'),
        random.choice('1234567980'),
        random.choice('1234567980'),
    ]
    
    requestStatus = True

    while requestStatus:
        UserAns = callUser()


        promptWord = {'A':0 , 'B':0}
        check = True

        for i in UserAns:
            for j in Ans:
                if i == j:
                    promptWord['A'] = promptWord['A']+1
                    check = False
                    break
            
            if check:
                promptWord['B'] = promptWord['B']+1
            else:
                check = True

        final = str(promptWord['A'])+'A'+str(promptWord['B'])+'B'

        if final == '4A0B':
            print('恭喜你答對了喔')
            break
        else:    
            print('提示',final)

def callUser():

    user = input('請輸入四位數的號碼 0000~9999，超過就幹死你 ：')

    if len(user) != 4:
        callUser()


    UserAns = [
        user[0:1],
        user[1:2],
        user[2:3],
        user[3:4]
    ]

    return UserAns


if __name__ == '__main__':
    main()