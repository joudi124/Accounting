import sqlite3

class mydb:
    def __init__(self) -> None:
        self.v_DbName = "JANY_Acc.db"
        
    def ExcuteNoneQuery(self,Query):
        result = False
        if Query == "" :
            return result

        conn = sqlite3.connect(self.v_DbName)
        cur = conn.cursor()
        
        res = cur.execute(Query)
        result = res.fetchone() is None

        conn.commit()
        conn.close()

        return result

    def ExistTable(self,TableName):
        result = False
        if TableName == "" :
            return result

        conn = sqlite3.connect(self.v_DbName)
        
        q = "select count(*) from sqlite_master where type=? and name=?"
        cur = conn.cursor()

        cur.execute(q,("table",TableName))
        data = cur.fetchone()

        if data[0] == 1 :
            result = True
        
        #conn.commit()
        conn.close()
       
        return result
    def Insert(self,Query,data):
        result = False
        if Query == "" :
            return result

        conn = sqlite3.connect(self.v_DbName)
        cur = conn.cursor()
        
        res = cur.execute(Query,data)
        result = True

        conn.commit()
        conn.close()

        return result
    def Select(self,Query,data=None):
        result = None
        if Query == "" :
            return result

        conn = sqlite3.connect(self.v_DbName)
        cur = conn.cursor()
        try:
            if data is None :
                cur.execute(Query)
            else:
                cur.execute(Query,data)
            
            result = cur.fetchall()
        except:
            result = None
            

        conn.commit()
        conn.close()

        return result
    def Update(self,Query,data=None):
        result = False
        if Query == "" :
            return result

        conn = sqlite3.connect(self.v_DbName)
        cur = conn.cursor()
        try:
            if data is None :
                cur.execute(Query)
            else:
                cur.execute(Query,data)
            
            result = True
        except:
            result = False
            

        conn.commit()
        conn.close()

        return result


    
    
#m = mydb()
#q = "insert into account(description,dt,invoice_id,increase,decrease,inventory) values(?,?,?,?,?,?)"
#m.Insert(q,("test12","2024-03-16",0,2000,500,3500))
#rows = m.Select("select * from account")

#print(rows[0])
#print(rows[3])
