

# **** ____________________ Assigment 16______________***

class Bank:

    bank_name = 'state bank'
 

    @classmethod
    def change_bank_name(cls,name):
        cls.bank_name = name

b1= Bank()
b2= Bank()


print(b1.bank_name)
print(b2.bank_name)

Bank.change_bank_name('natinal bank')

print(b1.bank_name)
print(b2.bank_name)