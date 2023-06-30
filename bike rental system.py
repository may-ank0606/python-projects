class bikeshop:
    def __init__(self,stock):
        self.stock=stock
    def displaybikeinfo(self):
        print(self.stock)
    def rentbike(self,q):
        if q<=0:
            print("this is invalid number for bike rent")
        elif q>self.stock:
            print("this is out of stock choose less quantity or try later if available")
        else:
            self.stock=(self.stock-q)
            print("no. of bikes to be ranted",q)
            print("total price for your rented bikes",q*1000)
            print("available bikes",self.stock)
while True:
    obj=bikeshop(1000)
    uc=int(input('''
    1 for display available bikes
    2 for renting bikes
    3 for exit
    '''))

    if uc==1:
        obj.displaybikeinfo()
    elif uc==2:
        n=int(input("enter the no. of bikes to be rent:--"))
        obj.rentbike(n)
    else:
        break