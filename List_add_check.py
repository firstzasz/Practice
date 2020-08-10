database_ = ['a', 'm', 'g']
x_input = input("add new database_ : ")
#database_.pop()
if x_input in database_:
    print('data is alredy recorded')
else:
    database_.append(x_input)
    print('data successfully recroded')

if input('show data list ? (Y/N)') == 'Y':
    print(database_)
    print('done')
else:
    print('Bye')