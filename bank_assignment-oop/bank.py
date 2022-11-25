class Bank:
    bank_name="American bank"
    
    def __init__(self,user_name,account_num,city):
        self.user_name=user_name
        self.account_num=account_num
        self.city=city
        self.has_balance=False
        self.balance=0
        self.record_scores=0

    def greeting(self):
        return f"Welcome {self.user_name} to {Bank.bank_name} 😊"

    def add_ammount(self,amount):
        self.balance+=amount
        self.has_balance=True
        if amount>=100:
            self.record_scores+=50
        return f"{self.user_name},you added {amount} and your current balance is ${self.balance}"

    def withdrow_money(self,amt):
        charge=0
        if self.balance<amt:
            self.has_balance=False
            charge+=10
            return f"no enogh amount to withdrow you have been chareged ${charge}  "
        self.balance-=amt
        return f"you withrew {amt} and your remaining balance is ${self.balance}"

    def take_loan(self,amount_):
        self.balance+=amount_
        if self.record_scores<50:
            return "you have not accepted for a loan "
        return f"you have accepted for a loan ${amount_} and your current balance is ${self.balance}"


user_Nina=Bank("Nina Adam",23490,"Bangor")
print(user_Nina.greeting())
print(user_Nina.add_ammount(200))
print(user_Nina.withdrow_money(100))
print(user_Nina.take_loan(1000))
print(user_Nina.withdrow_money(600))
print(user_Nina.withdrow_money(600))