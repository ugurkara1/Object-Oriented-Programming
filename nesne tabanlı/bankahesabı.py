#BankAccount isminde bir sınıf tanımlayınız
#Üretilen her bir nesne owner isminde bir özelliğe sahip olmalıdır.BankaAccount("Sadık Turan")
#Üretilen her bir nesne balance isminde bir özelliğe sahip olup başlangıçta 0.0 değerinde olmalıdır
#Üretilen her bir nesne için deposit metodu oluşturan ve dışarıdan yatırlacak miktar bilgisini alıp balance 
#üzerine ekleyin ve balance miktarını geriye döndürün
#üretilen her bir nesne için withdraw metodu oluşturun ve dışarıdan çekilecek miktar bilgisini alıp balance
#değerinden çıkarıp geriye döndürün

#hesap=BankAccount("Uğur Kara")
#hesap.owner=>Sadık Turan
#hesap.balance=>0.0
#hesap.deposit(1000)=>1000.0
#hesap.withdraw(500)=>500.0
class BankAccount:
    def __init__(self,name):
        self.owner=name
        self.balance=0.0
    def getBalance(self):
        return self.balance

    def deposit(self,amount):#eklenen para
        self.balance+=amount
        return self.balance
    def withdraw(self,amount):#çekilen tutar
        self.balance-=amount
        return self.balance
hesap=BankAccount("Uğur Kara")
print(hesap.getBalance())
hesap.deposit(1000)
print(hesap.getBalance())
hesap.withdraw(500)
print(hesap.getBalance())