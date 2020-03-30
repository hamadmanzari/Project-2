while True:
    x = input('Enter Username:\n')
    if x == 'hamad':
        print('Username correct')
        y = input('Enter Password:\n')
        if y == 'manzari':
            break
        else:
            print('Log in failed')
    else:
        print('Try again')
    

   