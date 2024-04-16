class Invoice_Detail:
    def __init__(self) -> None:
        #init Database

        
        #Init Variables
        self.v_id = 0
        self.v_Invoice_id = 0
        self.v_description = ""        
        self.v_amount = 0
        self.v_num = 0

    def Print(self) :
        print(self.v_description + "\t\t" + str(self.v_amount ) + "\t" + str(self.v_num) + "\t" + str(self.v_amount * self.v_num))
            