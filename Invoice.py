from datetime import datetime
import mydb
import Invoice_detail

class Invoice:
    def __init__(self) -> None:
        #Read Current Date
        today = datetime.today()
        strtoday = today.strftime("%Y-%m-%d")
        today = datetime.strptime(strtoday,"%Y-%m-%d")

        #init Database
        self.db = mydb.mydb()
        
        if self.db.ExistTable("Invoce") == False :
            q = "create table Invoce("
            q += "id INTEGER PRIMARY KEY AUTOINCREMENT"
            q += ",bs_name nvarchar(100)"
            q += ",dt varchar(10)"
            q += ",no  varchar(20)"
            q += ",discount integer"
            q += ",payment integer"
            q += ")"
            self.db.ExcuteNoneQuery(q)

        #Init Variables
        self.v_bs_name = ""
        self.v_dt = today.strftime("%Y-%m-%d")
        self.v_no = ""
        self.v_discount = 0
        self.v_payment = 0

        self.v_invoice_detail = []

    def AddDetail(self,Description,Amount,Num):
        self.v_invoice_detail.append(Invoice_detail.Invoice_Detail())
        index = len(self.v_invoice_detail)
        if index>0 :
            index -= 1
            self.v_invoice_detail[index].v_description = Description
            self.v_invoice_detail[index].v_amount = Amount
            self.v_invoice_detail[index].v_num = Num

    def Print(self):
        print("Name : " + self.v_bs_name + "\t\t" + self.v_no + "\t\t\t" + self.v_dt )
        print("----------------------------------------------------------------------")
        print("Description \t\t Amount \t Number \t\t Sum")
        print("----------------------------------------------------------------------")

        self.v_payment = 0
        for inv_detail in self.v_invoice_detail :
            inv_detail.Print()
            self.v_payment += (inv_detail.v_amount * inv_detail.v_num)

        print("----------------------------------------------------------------------")
        print("\t\t\t\t\t\t\tDiscount \t" + str(self.v_discount))
        self.v_payment -= self.v_discount
        print("\t\t\t\t\t\t\t\t" + str(self.v_payment))

    def SaveAll(self):
        pass