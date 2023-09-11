#class Product:
 #   def __init__(self):
 #       self.name="Samsung s10"
  #      self.price=2000
   #     print("product nesnesi oluşturuldu")
#p1=Product()
#p2=Product()
#print(p1.name,p2.name)
#print(p1.price,p2.price)
class Product:
    def __init__(self,name,price):#self için parametre göndermiyoruz
        self.name=name
        self.price=price
        print("product nesnesi oluşturuldu")

p1=Product("samsung s10",5000)
p2=Product("ıphone 12",8000)

print(p1.name,p2.name)
print(p1.price,p2.price)
