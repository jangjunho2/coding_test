while(1):
    try:
        a=input()
        if a=='0':
            break
        elif(a==a[::-1]):
            print('yes')
        else:
            print('no')
    except:
        break