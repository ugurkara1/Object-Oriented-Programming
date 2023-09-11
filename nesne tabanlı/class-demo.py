#commant isminde bir sınıf oluşturunuz
#comment sınıfı username,text,likes,dislikes isminde özelliklere sahip olun
#5 adet farklı comment oluşturup döngü yardımıyla yorumları ekrana yazdırınız

class Commant:
    def __init__(self,username, text, likes=0, dislikes=0):
        self.username=username
        self.text=text
        self.likes=likes
        self.dislikes=dislikes
c1=Commant("Ugurkara","güzel kurs",100,10)
c2=Commant("dilanyasar","beğendim",100,10)
c3=Commant("tugcekara","kötüydü")
c4=Commant("berenkara","youtube da var hemde parasız ")
c5=Commant("zilanyasar","çok beğendim")

comments=[c1,c2,c3,c4,c5]
for c in comments:
    print(f"{c.username}:{c.text}")
    print(f"likes:{c.likes}-dislikes:{c.dislikes}")
        