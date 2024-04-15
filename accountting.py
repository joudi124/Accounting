from datetime import datetime
import mydb

class Accounting:
    def __init__(self) -> None:
        #Read Current Date
        today = datetime.today()
        strtoday = today.strftime("%Y-%m-%d")
        today = datetime.strptime(strtoday,"%Y-%m-%d")

        #init Database
        self.db = mydb.mydb()
        
        if self.db.ExistTable("account") == False :
            q = "create table account("
            q += "id INTEGER PRIMARY KEY AUTOINCREMENT"
            q += ",description nvarchar(100)"
            q += ",dt  varchar(10)"
            q += ",invoice_id integer"
            q += ",increase integer"
            q += ",decrease integer"
            q += ",inventory integer"
            q += ")"
            self.db.ExcuteNoneQuery(q)

        #Init Variables
        self.v_Description = ""
        self.v_DT = today.strftime("%Y-%m-%d")
        self.v_Invoice_Id = 0
        self.v_Increase = 0
        self.v_Decrease = 0
        
        res = self.db.Select("select inventory from account order by id desc LIMIT 1")
           
        if len(res)==0 :
            self.v_Inventory = 0            
        else :            
            self.v_Inventory = res[0][0]

    def InsertToDb(self):
        q = "insert into account(description,dt,invoice_id,increase,decrease,inventory) values(?,?,?,?,?,?)"
        self.db.Insert(q,(self.v_Description,self.v_DT,self.v_Invoice_Id,self.v_Increase,self.v_Decrease,self.v_Inventory))

    
    def PrintAccount(self):
        print("Description\tDate\t\t\t\t\tInvoice Id\tIncrease\tDecrease\tInventory")
        print(self.v_Description + "\t\t"+str(self.v_DT) +"\t\t\t" + str(self.v_Invoice_Id) + "\t\t" +str(self.v_Increase) + "\t\t" + str(self.v_Decrease) + "\t\t" + str(self.v_Inventory) )
    
    def PrintAll(self):
        print("Description\tDate\t\t\t\t\tInvoice Id\tIncrease\tDecrease\tInventory")
        q = "select * from account"
        rows = self.db.Select(q)
        for row in rows :
            print(row)
    
    def Increase(self,v_Description,v_DT,v_Increase):
        self.v_Description = v_Description
        self.v_DT = v_DT
        self.v_Increase = v_Increase
        self.v_Decrease = 0
        self.v_Inventory += v_Increase
        self.InsertToDb()
    
    def Decrease(self,v_Description,v_DT,v_Decrease):
        self.v_Description = v_Description
        self.v_DT = v_DT
        self.v_Decrease = v_Decrease
        self.v_Increase = 0
        self.v_Inventory -= v_Decrease
        self.InsertToDb()


#acc = Accounting()

#acc.PrintAll()

#DT = datetime.strptime("2024-01-16","%Y-%m-%d")
#acc.Increase("Test 01",DT,700000)
#acc.Increase("Test 02",DT,17000)
#acc.Decrease("Test 03",DT,23000)

#acc.PrintAll()

