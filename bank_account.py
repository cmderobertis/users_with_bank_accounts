class BankAccount:
  
  all_accounts = []
  
  def __init__(self, interest_rate, balance=0):
    self.interest_rate = interest_rate
    self.balance = balance
    BankAccount.all_accounts.append(self)
  
  def deposit(self, amount):
    self.balance += amount
    return self
  
  def withdraw(self, amount):
    if self.balance > amount:
      self.balance -= amount
    else:
      print("Insufficient funds: Charging a $5 fee")
      self.balance -= 5
    return self
  
  def display_account_info(self):
    print(f"Balance: ${self.balance}")
    return self
  
  def yield_interest(self):
    if self.balance > 0:
      self.balance *= 1 + self.interest_rate
    return self
  
  @classmethod
  def print_all_info(cls):
    for account in cls.all_accounts:
      account.display_account_info()

acc1 = BankAccount(0.05, 500)
acc2 = BankAccount(0.1, 150)

# acc1.deposit(50).deposit(35).deposit(19).withdraw(400).yield_interest().display_account_info()
# acc2.deposit(100).deposit(100).withdraw(25).withdraw(25).withdraw(25).withdraw(25).yield_interest().display_account_info()

# BankAccount.print_all_info()