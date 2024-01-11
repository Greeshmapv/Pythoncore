class Bank:
    def getroi(self):
        return 10
class SBI(Bank):
    def getroi(self):
        return 7
class ICICI(Bank):
    def getroi(self):
        return 8
b1=Bank()
b2=SBI()
b3=ICICI()
print("bank rate of intrest:",b1.getroi())
print("SBI rate of intrest:",b2.getroi())
print("ICICI rate of intrest:",b3.getroi())