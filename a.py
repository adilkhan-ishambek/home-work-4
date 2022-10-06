class Password_manager():
    
    def __init__(self,name):
        self.name = name
        self.old_password = []

    def old_passwords(self):
        return self.old_password 

    def get_password(self):
        return self.old_password[-1] if len(self.old_password)!=0 else "Please, set password firstly"

    def set_password(self,password):
        self.old_password.append(password)

    def is_correct(self,check):
        return True if check==self.old_password[-1] else False

user1 = Password_manager("Qwerty")

print(user1.old_passwords())

user1.set_password("12345")
print(user1.get_password())

user1.set_password("12345")
user1.set_password("12345")
print(user1.get_password())
print(user1.old_passwords())

print(user1.is_correct("12345"))
print(user1.is_correct("12345"))