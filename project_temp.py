class bank:
    
    def main(self):
        self.PIN =809012
        self.history_balance=[]
        self.balance=0
        try:
          self.user_name=input("please enter your NAME: ")
          self.user_branch=input("please enter your Bank branch NAME: ")
          self.acc=int(input("please enter your account number: "))
          self.pin=int(input("please enter your password: "))
        except ValueError:
          print("please enter correct value")
        

        if self.pin==self.PIN:
         # def menu():
          print("Login Sucessfully")
          print("************Welcome to the ATM machine*************")    
          print("---------------------------------------------------")   
          print("**********Select the number to proceed*************")   
          print("---------------------------------------------------")   
          print("  1.  ----------> ACCOUNT Details")   
          print("  2.  ----------> Balance check") 
          print("  3.  ----------> Deposit") 
          print("  4.  ----------> Withdrawl") 
          print("  5.  ----------> PIN change") 
          print("  6.  ----------> Account History")
          print("  7.  ----------> EXIT")
        else:
         print("Incorrect Password")
         exit()
         
             

    def selection_from_user(self):
         
          while True:
           try:
             
            self.coustmer_selection= int(input("         Please Select your option here           "))            
            match self.coustmer_selection :
              
             
             
              case 1:
               print(f"Account number is : {self.acc}")
               print(f"NAME : {self.user_name}")
               print(f"bank branch {self.user_branch}")
              case 2:
               print(f"your current balance : {self.balance}")
              case 3:
               deposit_amount = float(input("Please enter an amount"))  
               self.balance+=deposit_amount
               hist=f" deposited  : {deposit_amount}"
               self.history_balance.append(hist)
               print(f"Amount deposit sucessfully and current balance : {self.balance}")    
              case 4:
               withdrawl_amount  = float(input("Please enter an amount : "))
               if withdrawl_amount<=self.balance:
                 
                 self.balance -=withdrawl_amount
                 print(f"sucessfully withdrawl {withdrawl_amount} and your remaining balance is : {self.balance} ")
                 histw=f"debited : {withdrawl_amount}"
                 
                 self.history_balance.append(histw)                
                 
               else:
                 print("Insufficient funds ")
               
              case 5:
               old_pin=int(input("Please enter your old pin"))
               if old_pin==self.PIN:
                new_pin=int(input("Please enter your new pin"))
                self.PIN = new_pin
                histpin =f"PIN changed"
                self.history_balance.append(histpin)
  
               else:
                print("please enter the correct pin")
              case 6:
               for i in self.history_balance:
                 
                print(i)
              case 7:
               break
           
               # exit()
              case _:
               print("please enter")
         
            
             
            
            print("please enter the correct one")
           
           
           except ValueError:
             print("please enter the correct one")      
     
b1=bank()     
b1.main()    
  
  
b1.selection_from_user()
 


      