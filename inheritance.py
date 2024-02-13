class mpesa:
    def __init__(self,account_balance,phone_number):
        self.account_balance =account_balance
        self.phone_number=phone_number
    def send_money(self,amount,recipient):
        if self.account_balance >= amount:

            self.account_balance -= amount
            print(f"{amount}KES sent to {recipient}succesfull")
        else:
            print ("insufficient balance")
class personal_Mpesa(mpesa):
    def __init__(self,account_balance,phone_number,id_number):
        super().__init__(account_balance, phone_number)
        self.id_number =id_number
    def buyairtime(self,amount):
        if self.account_balance >=amount:
            self.account_balance -= amount
            print(f"{amount}KES aitime bought ")
        else:
            print ("insufficient balance")
class bussines(mpesa):
    def __init__(self,account_balance,phone_number,bussines_name):
        super().__init__(account_balance,phone_number)
        self.bussines_name=bussines_name

    def receive_money(self,amount):
        self.account_balance +=amount
        print(f"{amount}kes received successfully")
personal=personal_Mpesa(500,7345454,454464543,)
personal.send_money(400,4546453)
personal.buyairtime(25)

buss=bussines(734,74636878,"skillibeng")
buss.receive_money(20)



