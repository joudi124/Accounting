import accountting
import store

#Init Variables
acc = accountting.Accounting()
st = store.Store()

#Create Menu
while True:
    print("")
    print("")
    print("JANY Accounting Menu")
    print("0- Exit")
    print("##########################################")
    print("1- Accounting Print all")
    print("2- Accounting increase")
    print("3- Accounting decrease")
    print("##########################################")
    print("4- Store Print all products")
    print("5- Store increase Product")
    print("6- Store decrease Product")
    print("##########################################")
    print("7- Invoce Print all")
    print("8- Invoce increase")
    print("9- Invoce decrease")    

    #Input Choice Menu
    ch = input("Enter Choice Number : ")

    #Run Choice Menu
    if ch=="0" : # Exit
        break
    elif ch=='1' : # Accounting Print all accounts
        acc.PrintAll()
    elif ch=='2' : # Accounting increase value
        description = input("Description : ")
        DT = input("Enter Miladi Date (yyyy-mm-dd) : ")
        increase = input("Enter Increase Number : ")
        ch = input("This data is true(press y to accept)? ")
        if ch=='y' :
            acc.Increase(description,DT,int(increase))
            print("##### Data Inserted database. #####")
        
    elif ch=='3' : # Accounting decrease value
        description = input("Description : ")
        DT = input("Enter Miladi Date (yyyy-mm-dd) : ")
        decrease = input("Enter Decrease Number : ")
        ch = input("This data is true(press y to accept)? ")
        if ch=='y' :
            acc.Decrease(description,DT,int(decrease))
            print("##### Data Decserted database. #####")
    elif ch=='4' : # Store Print all products
        st.PrintAll()
    elif ch=='5' : # Store increase Product        
        product_name = input("Product Name : ")
        last_purchase_amount = input("Last Purchase Amount : ")
        last_purchase_dt = input("Last Purchase Date (yyyy-mm-dd) : ")
        estimated_salse_amount = input("Estimated Salse Amount : ")
        Num = input("Increase Number : ")
        ch = input("This data is true(press y to accept)? ")
        if ch=='y' :
            st.Increase(product_name,int(last_purchase_amount),last_purchase_dt,int(estimated_salse_amount),int(Num))
    elif ch=='6' : # Store decrease Product
        product_name = input("Product Name : ")        
        Num = input("Decrease Number : ")
        ch = input("This data is true(press y to accept)? ")
        if ch=='y' :
            st.Decrease(product_name,int(Num))
    elif ch=='7' : # Invoce Print all
        pass
    elif ch=='8' : # Invoce increase
        pass
    elif ch=='9' : # Invoce decrease
        pass