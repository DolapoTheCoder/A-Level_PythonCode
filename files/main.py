choice = input('Answer "yes" if you would like to restart register OR answer "no" if you would like to continue register')
if choice == 'yes':
    choice1 = input('Do you want to delete a line from this text file:')
    if choice1 == 'yes':
        g = open('formgroup.txt','r')
        lines = g.readlines()
        print(lines)
        print(len(lines))
        for line in lines:
            print(line)
        g.close()
        delete = int(input("What line would you like to delete: "))
        g1 = open('formgroup1.txt','w')
        
        
    FN = input('Firstname: ')
    SN = input('Surname: ')
    Y = input('Year: ')
    F = input('Form: ')
    print('you entered', FN, SN, Y, F)
    g = open('formgroup.txt','a+')
    g.write('Firstname: ' + FN)
    g.write(' Surname: ' + SN)
    g.write(' Year: ' + Y)
    g.write(' Form: ' + F)
    g.write('\n')
    g.close()
else:
    FN = input('Firstname: ')
    SN = input('Surname: ')
    Y = input('Year: ')
    F = input('Form: ')
    print('you entered', FN, SN, Y, F)
    g = open('formgroup.txt','w')
    g.write('Firstname: ' + FN)
    g.write(' Surname: ' + SN)
    g.write(' Year: ' + Y)
    g.write(' Form: ' + F)
    g.write('\n')
    g.close()