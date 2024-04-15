from datetime import datetime
import mydb

class Invoce:
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
            q += ",dt int"
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


            