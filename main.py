import mysql.connector as connector


class DBconnect:
    def __init__(self):
        self.con=connector.connect(host='localhost',port=3306,user='root',password='UBNqaly W;8b&>{',database='pythontest',auth_plugin='mysql_native_password')

        query='create table if not exists users(ID int primary key, Name varchar(20), Address varchar(20), Contact_Number bigint)'

        cur=self.con.cursor()
        cur.execute(query)
        print('DB created')

    
    #Inserting datas
    def insert_values(self,id,name,address,number):
        query="insert into users values({},'{}','{}',{})".format(id,name,address,number)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print('Data Inserted')
    
    def display_records(self):
        query='select * from users'
        cur=self.con.cursor()
        cur.execute(query)
        for row in cur:
            print(row)
    
    def delete_record(self,userid):
        query="delete from users where id='{}'".format(userid)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print('Data successfully deleted')

    def display_menu(self): 
        continue_="yes"

        while continue_=="yes":
            print('****************Enter Operation**************')
            print()
            print('1. Insert')
            print('2. Fetch')
            print('3. Delete')
            print()
            print('*********************************************')

            choice=int(input())

            if choice==1:
                print('Enter ID')
                id=input()
                print('Enter Name')
                name=input()
                print('Enter Address')
                address=input()
                print('Enter phone number')
                number=input()

                connect.insert_values(id,name,address,number)

            elif choice==2:
                connect.display_records()

            elif choice==3:
                print("Enter user id you want to delete")
                userid=int(input())
                connect.delete_record(userid)

            else:
                print('Invalid Operation')

            print("Do you want to continue ? yes/no")
            continue_=input().lower()

connect=DBconnect()
connect.display_menu()

