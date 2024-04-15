from datetime import datetime
import mydb

class Store:
    def __init__(self) -> None:
        #Read Current Date
        today = datetime.today()
        strtoday = today.strftime("%Y-%m-%d")
        today = datetime.strptime(strtoday,"%Y-%m-%d")

        #init Database
        self.db = mydb.mydb()
        
        if self.db.ExistTable("store") == False :
            q = "create table store("
            q += "id INTEGER PRIMARY KEY AUTOINCREMENT"
            q += ",product_name nvarchar(100)"
            q += ",last_purchase_amount int"
            q += ",last_purchase_dt  varchar(10)"
            q += ",estimated_salse_amount integer"
            q += ",inventory integer"
            q += ")"
            self.db.ExcuteNoneQuery(q)

        #Init Variables
        self.v_product_name = ""
        self.v_last_purchase_amount = 0
        self.v_last_purchase_dt = today.strftime("%Y-%m-%d")
        self.v_estimated_salse_amount = 0

        self.v_increase = 0
        self.v_decrease = 0

        self.v_inventory = 0

    def SaveToDb(self):
        id = self.FindProductByName(self.v_product_name)
        if  id == 0 : # Add New
            q = "insert into store(product_name,last_purchase_amount,last_purchase_dt,estimated_salse_amount,inventory) values(?,?,?,?,?)"
            self.v_inventory += (self.v_increase - self.v_decrease )
            self.db.Insert(q,(self.v_product_name,self.v_last_purchase_amount,self.v_last_purchase_dt,self.v_estimated_salse_amount,self.v_inventory))
        else: # Update
            #Backup variables
            Last_Purchase_Amount = self.v_last_purchase_amount
            Last_Purchase_Dt = self.v_last_purchase_dt
            Estimated_Salse_Amount = self.v_estimated_salse_amount

            # Read Product from database
            if self.FindProductByID(id)==True :
                #UpDate Data
                self.v_last_purchase_amount = Last_Purchase_Amount
                self.v_last_purchase_dt = Last_Purchase_Dt
                self.v_estimated_salse_amount = Estimated_Salse_Amount
            
            self.v_inventory += (self.v_increase - self.v_decrease )
            q = "update store set product_name=?,last_purchase_amount=?,last_purchase_dt=?,estimated_salse_amount=?,inventory=? where id = ?"
            self.db.Update(q,(self.v_product_name,self.v_last_purchase_amount,self.v_last_purchase_dt,self.v_estimated_salse_amount,self.v_inventory,id))
    
    def FindProductByName(self,Product_Name):
        result = 0
        q = "select id from store where product_name=?"
        res = self.db.Select(q,(Product_Name,))
        if len(res)>0 :
            result = res[0][0]

        return result
    
    def FindProductByID(self,ID):
        result = False
        q = "select product_name,last_purchase_amount,last_purchase_dt,estimated_salse_amount,inventory from store where id=?"
        res = self.db.Select(q,(ID,))
        if len(res)>0 :
            result = True
            self.v_product_name = res[0][0]
            self.v_last_purchase_amount = res[0][1]
            self.v_last_purchase_dt = res[0][2]
            self.v_estimated_salse_amount = res[0][3]
            self.v_inventory = res[0][4]

        return result
    
    def PrintProduct(self):
        print("Product Name : " + self.v_product_name)
        print("Last Purchase Amount : " + str(self.v_last_purchase_amount))
        print("Last Purchase Date : " + self.v_last_purchase_dt)
        print("Estimated Salse Amount : " + str(self.v_estimated_salse_amount))
        print("Inventory : " + str(self.v_inventory))
        

    def PrintAll(self):
        print("product_name,last_purchase_amount,last_purchase_dt,estimated_salse_amount,inventory")
        q = "select * from store"
        rows = self.db.Select(q)
        for row in rows :
            print(row)
            

    def Increase(self,product_name,last_purchase_amount,last_purchase_dt,estimated_salse_amount,Num):
        id = self.FindProductByName(product_name)
        if id == 0 :
            self.v_product_name = product_name
            self.v_inventory = 0
        else:
            self.FindProductByID(id)
            
        self.v_last_purchase_amount = last_purchase_amount
        self.v_last_purchase_dt = last_purchase_dt
        self.v_estimated_salse_amount = estimated_salse_amount
        self.v_increase = Num

        self.SaveToDb()
    
    def Decrease(self,product_name,Num):
        result = False
        id = self.FindProductByName(product_name)
        if id == 0 :
            self.v_product_name = product_name
            self.v_inventory = 0
        else:
            self.FindProductByID(id)
            
        self.v_decrease = Num
        if (self.v_inventory-self.v_decrease )>=0 :            
            self.SaveToDb()
            result = True
        else:
            print("Inventory<0  ... con't save to database...")

        return result
