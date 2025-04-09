#Employee Information System Project with oops ---using mysql
import mysql.connector as sql
class employee:
    def __init__(self):
        print("*" * 50)
        print("\tEMP INFORMATION SYSTEM")
        print("*" * 50)
        print("\t\t1. New Employee")
        print("\t\t2. Delete Employee")
        print("\t\t3. Update Employee")
        print("\t\t4. View Single Employee")
        print("\t\t5. View All Employee")
        print("\t\t6. Search for Employee")
        print("\t\t7. Exit")
        print("*" * 50)
    def addemp(self):
        try:
            con = sql.connect(host="localhost",
                              user="supriya",
                              passwd="soup",
                              database="python11am")
            cur=con.cursor()
            self.empno = int(input("Enter Employee Number:"))
            self.empname = input("Enter Employee Name:")
            self.empsal = float(input("Enter Employee Salary:"))
            self.compname = input("enter compname")
            iq="insert into employee values (%d,'%s',%f,'%s')"
            cur.execute(iq %(self.empno,self.empname,self.empsal,self.compname))
            con.commit()
            if(cur.rowcount>0):
                print("record added ---verify")
            else:
                print("employee record doesnot exist")
        except sql.DatabaseError as db:
            print("problem in sql database",db)


    def deletemp(self):
        try:
            con = sql.connect(host="localhost",
                              user="supriya",
                              passwd="soup",
                              database="python11am")
            cur = con.cursor()
            self.eno = int(input("enter employee number to be deleted"))
            dq= "delete from employee where eno=%d"
            cur.execute(dq %(self.eno))
            con.commit()
            if(cur.rowcount>0):
                print("{} record deleted".format(cur.rowcount))
            else:
                print("record doesnot exist")
        except sql.DatabaseError as db:
            print("problem in sql database",db)
    def updatemp(self):
        try:
            con = sql.connect(host="localhost",
                              user="supriya",
                              passwd="soup",
                              database="python11am")
            cur = con.cursor()
            self.empno = int(input("Enter Employee Number:"))
            self.empname = input("Enter Employee Name:")
            self.empsal = float(input("Enter Employee Salary:"))
            self.compname = input("enter compname")
            uq="update employee set  ename='%s',empsal=%f,compname='%s' where eno=%d"
            cur.execute(uq %(self.empname,self.empsal,self.compname,self.empno))
            con.commit()
            if(cur.rowcount>0):
                print("record updated ---verify")
            else:
                print("employee record doesnot exist")
        except sql.DatabaseError as db:
            print("problem in sql database",db)
    def viewemployee(self):
        try:
            con = sql.connect(host="localhost",
                              user="supriya",
                              passwd="soup",
                              database="python11am")
            cur = con.cursor()
            self.eno=int(input("enter eno to be view"))
            vq = "select ename,empsal,compname from employee where eno=%d"
            cur.execute(vq  %(self.eno))
            colinfo = cur.description
            for column in colinfo:
                print(column[0], end="\t\t")
            print()

            record = cur.fetchone()
            if(record):

                for val in record:
                    print("\t{}".format(val), end="\t")
                print()
            else:
                print("empno desnot exist")
        except sql.DatabaseError as db:
            print("problem in sql database",db)
    def viewmployees(self):
        try:
            con = sql.connect(host="localhost",
                              user="supriya",
                              passwd="soup",
                              database="python11am")
            cur = con.cursor()
            vq="select * from employee"
            cur.execute(vq)
            colinfo = cur.description
            for column in colinfo:
                print(column[0],end="\t\t")
            print()

            record = cur.fetchall()
            if(record):
                for records in record:
                    for val in records:
                        print("\t{}".format(val),end="\t")
                    print()
        except sql.DatabaseError as db:
            print("problem in sql database",db)
    def searchemp(self):
        try:
            con = sql.connect(host="localhost",
                              user="supriya",
                              passwd="soup",
                              database="python11am")
            cur = con.cursor()
            self.eno=int(input("enter empno to search"))
            vq="select eno from employee where eno=%d"
            cur.execute(vq %(self.eno))

            res=cur.fetchone()

            if(res):
                print("employee record exist")
            else:
                print("employee doesnotexist")

        except sql.DatabaseError as db:
            print("problem in sql database",db)


while(True):
    s=employee()
    ch=int(input("enter ur choice"))
    match(ch):
        case 1:
            s.addemp()
        case 2:

            s.deletemp()
        case 3:

            s.updatemp()
        case 4:

            s.viewemployee()
        case 5:
            s.viewmployees()
        case 6:

            s.searchemp()
        case 7:
            print("thanks fr using this program")
            break
        case _:
            print("\t ur selection of choice is wrong---try again")
