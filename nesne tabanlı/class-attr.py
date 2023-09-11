class User:
    
    active_users=0

    def __init__(self,first,last,age):
        self.first=first
        self.last=last
        self.age=age
        User.active_users+=1

    def full_name(self):
        return f"{self.first} {self.last}"

print(User.active_users) 
userA=User("Sadık","Turan",37)
userB=User("Sena","Turan",20) 
print(User.active_users) 
