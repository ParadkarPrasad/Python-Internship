class Bank:


  def __init__(self, initial_amount=0.00):
    self.balance = initial_amount


  def log_transaction(self, transaction_string):
    with open("transaction.txt", "a") as file:
      file.write(f"{transaction_string}\t\t\tBalance: {self.balance}\n")


  def withdraw(self,amount):
    try:
      amount = float(amount)
    except ValueError:
      amount = 0
    if amount:
      self.balance = self.balance - amount
      self.log_transaction(f"Withdrew {amount}")

  def deposit(self,amount):
    try:
      amount = float(amount)

    except ValueError:
      amount= 0
    if amount:
      self.balance = self.balance + amount
      self.log_transaction(f"Deposited {amount}")

account = Bank(50.50)
while True:
  try:
    action = input("What kind of action you want to take?")
  except KeyboardInterrupt:
    print("\nLeaving the ATM\n")
    break
  if action in ["withdraw", 'deposit']:
    if action == 'withdraw':
      amount = input("How much you want to withdraw?")
      account.withdraw(amount)
    else:
      amount = input("How much you want to deposit?")
      account.deposit(amount)
    
    print("Your balance is", account.balance)
  else:
    print("Invalid action. Please try again.")