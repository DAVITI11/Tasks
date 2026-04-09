
StLst = []

SbLst = []

StInfo = ('სახელი', 'გვარი', 'ასაკი', 'ტელეფონი', 'პროგრამა')

def add_st(*args):
    StLst.append({
        StInfo[0] : args[0],
        StInfo[1] : args[1],
        StInfo[2] : args[2],
        StInfo[3] : args[3],
        StInfo[4] : args[4],
    })

def add_sb(**args):
    SbLst.append(args)

def PrintAllStInfo():
    print(StLst)
    print(SbLst)

def SearchStudent(firstname, lastname):
    cnt = int(0)
    for i in StLst:
        if i['სახელი'] == firstname and i['გვარი'] == lastname:
            print(f'{firstname} {lastname} მონაცემები : {i}')
            print(SbLst[cnt])
            return
        cnt += 1
    print(f'სტუდენტი {firstname} {lastname} არ მოიძებნა სიაში!!!')


while True:

    op = input('სტუდენტის დამატება 1\nსტუდენტის ძებნა 2\nმთლიანი სიის დაბეჭვდა 3\nდამთავრება 4\n---> ')

    if op == '1':
        tmp = []
        for i in StInfo:
            tmp.append(input(f'შეიყვანე სტუდენტის {i} : '))
        add_st(*tmp)
        sbMrk = {}
        st = input(f'შეიყვანეთ {tmp[0]} {tmp[1]} საგნები : ').split()
        for i in st:
            sbMrk[i] = input(f'შეიყვანეთ {i} საგნის ნიშანი : ')
        add_sb(**sbMrk)
    elif op == '2':
        fsnm, lsnm = input('შეიყვანე სტუდენტის სახელი და გვარი : ').split()
        SearchStudent(fsnm, lsnm)
    elif op == '3':
        PrintAllStInfo()
    elif op == '4':
        break
    else:
        print('არასწორი ოპერაცია')