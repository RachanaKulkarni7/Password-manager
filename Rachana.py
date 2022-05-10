class BasePasswordManager: 
    old_passwords = ["Rachana"] 
    def get_password(self): 
         return self.old_passwords[-1] 
    def is_correct(self, password): 
        return self.get_password() == password
class PasswordManager(BasePasswordManager):
    def set_password(self, new_password):
        if self.get_level(new_password) > self.get_level() and len(new_password) >= 6: 
         self.old_passwords.append(new_password) 
        else: 
           print("Password can't be changed.")
    def get_level(self, password = None):  
         if password == None:
             password = self.get_password()
         if password.isalpha() or password.isnumeric():      
             level = 0  
         elif password.isalnum():   
             level = 1 
         else:
             level = 2
         return level

sb= BasePasswordManager()
print("Your old password is :", sb.get_password())
print("Is your current password matchs with old password :",sb.is_correct("Rachana"))
passwordManager = PasswordManager()
passwordManager.set_password("Rachana@123")
print("Your level is : ", passwordManager.get_level())         
    