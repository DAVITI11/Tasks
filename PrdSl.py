import sqlite3

class BaseHlpr:
    def __init__(self):

        self.con = sqlite3.connect("Mrk.db")
        self.cur = self.con.cursor()

    def create_tables(self):

        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS product(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                size REAL,
                get_price REAL,
                sale_price REAL,
                count INTEGER
            )
        """)

        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS sale(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                pid INTEGER,
                count INTEGER
            )
        """)
        self.con.commit()
    
    def check_count(self,id):

        self.cur.execute("SELECT count FROM product WHERE id=?",(id,))
        cnt = self.cur.fetchone()
        return cnt[0]
        
    def sell_prod(self,pid,count):

        cnt = self.check_count(pid)
        cnt, count = int(cnt), int(count)

        if cnt >= count:
            self.cur.execute("INSERT INTO sale(pid,count) VALUES(?,?)",(pid,count))
            self.cur.execute("UPDATE product set count=? where id=?",(cnt-count,pid))
            self.con.commit()

        else:
            print("არასაკმარისი პროდუქტი")

    def select_prod(self):
        
        self.cur.execute("SELECT * FROM product")
        for i in self.cur.fetchall():
            print(i)

    def select_sale(self):

        self.cur.execute("SELECT * FROM sale")
        for i in self.cur.fetchall():
            print(i)

    def insert_prod(self,*args):

        try:
            self.cur.execute("INSERT INTO product(name,size,get_price,sale_price,count) VALUES(?,?,?,?,?)",(args[0],args[1],args[2],args[3],args[4]))
            self.con.commit()
        except:
            self.con.rollback()

    def get_profit(self,id):

        self.cur.execute("SELECT SUM(count) FROM sale WHERE pid=?", (id,))
        selcnt = self.cur.fetchone()
        
        self.cur.execute("SELECT get_price FROM product where id=?",(id,))
        get_price = self.cur.fetchone()

        self.cur.execute("SELECT sale_price FROM product WHERE id=?", (id,))
        sale_price = self.cur.fetchone()
        
        total_count = selcnt[0] if selcnt[0] is not None else 0
        price = (sale_price[0] if sale_price[0] is not None else 0) - (get_price[0] if get_price[0] is not None else 0)
        
        pfr = total_count * price
        print(pfr)

bs = BaseHlpr()
#bs.create_tables()

while True:

    op = input("პროდუცტის დამატება 1\nგაყიდვების დამატება 2\nპროდუცტის ცხრილის ნახვა 3\nგაყიდვების ცხრილის ნახვა 4\nმოგების ნახვა id_ით 5\nგამოსვლა 6\n ------> ")

    if op == '1':
        st = input("შეიყვანე პროდუქტის მონაცემები: სახელი, ზომა, მიღების ფასი, გაცემის ფასი, რაოდენობა ---> ").split()
        pr = []
        for i in st:
            pr.append(i)
        bs.insert_prod(pr[0],pr[1],pr[2],pr[3],pr[4])

    elif op == '2':
        st = input("შეიყვანე პროდუქციის id და რეოდენობა : ").split()
        sl = []
        for i in st:
            sl.append(i)
        bs.sell_prod(sl[0],sl[1])

    elif op == '3':
        bs.select_prod()

    elif op == '4':
        bs.select_sale()

    elif op == '5':
        id = int(input("შეიყვანე id --> "))
        bs.get_profit(id)

    elif op == '6':
        break

    else:
        print("არასწორი ოპერაცია !!!")
    print()