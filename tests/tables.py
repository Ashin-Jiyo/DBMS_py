D={}
While True:
    print('Do you wish to add \'id\' coloum to the table')
    c0=input("Yes or No (Y/N): ")
    print('Do you wish to make \'id\' coloum as primary key')
    # print('\'id\' will auto increment if it is primary key')
    c02=input("Yes or No (Y/N): ")
    if c0 in ['Y','y','Yes','yes']:
            D['id']=[]
            if c02 in ['Y','y','Yes','yes']:
                pk=True
            else:
                pk=False