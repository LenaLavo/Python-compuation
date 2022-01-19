class Category:
  def __init__(self, category):
    self.ledger = []
    self.amount = 0
    self.category = category

  def check_funds(self, amount):
    #accepts an amount as an argument. It returns False if the amount is greater than the balance of the budget category and returns True otherwise
    if self.amount < amount:
      return False
    else:
      return True

  def deposit(self, amount, description = ""):
    #accepts an amount and description. If no description is given, it should default to an empty string
    self.ledger.append({"amount": amount, "description": description})
    self.amount += amount

  def withdraw(self, amount, description = ""):
    #amount passed in should be stored in the ledger as a negative number. If there are not enough funds, nothing should be added to the ledger
    if self.check_funds(amount) == True:
      self.ledger.append({"amount": -amount, "description": description})
      self.amount -= amount
      return True
    else:
      return False

  def transfer(self, amount, category):
    #accepts an amount and another budget category as arguments
    if self.check_funds(amount) == True:
      self.ledger.append({"amount": -amount,"description":"Transfer to "+category.category})
      category.ledger.append({"amount": amount,"description": "Transfer from " + self.category})
      self.amount -= amount
      category.amount += amount
      return True
    else:
      return False

  def get_balance (self):
    #returns the current balance of the budget category based on the deposits and withdrawals
    return self.amount

  def __str__(self):
    result=""
    result += self.category.center(30, "*") + "\n"

    for transaction in self.ledger:
      for key in transaction.keys():
        amount = transaction["amount"]
        if len(str(amount)) > 7:
          amount = str(amount[:7])
        cut_amount = str(format(float(amount),'.2f'))
      for value in transaction.values():
        description = transaction["description"]
        cut_description = (description[:23])

      result += cut_description + str(cut_amount).rjust(30 - len(cut_description)) + "\n"

    result += "Total: " + str(format(float(self.amount),'.2f'))

    return result


def create_spend_chart(categories):
  total = 0
  subtotals = []

  #calculate each total withdrawal per category then add to subtotals list
  for category in categories:
    withdrawals = []
    subtotal = 0
    withdrawals.append(category.category)
    for item in category.ledger:
      if item["amount"] < 0:
        subtotal += item["amount"]
    withdrawals.append(subtotal)
    total += subtotal
    subtotals.append(withdrawals)

  #change subtotal withdrawal amount to percentage
  for item in subtotals:
    item[1] = (item[1] / total) *100

  # Build percentages and 'o'
  bar = []
  y = 100
  while y > -1:
    bar.append(' ' * (3 - len(str(y))))
    bar.append(y)
    bar.append('|')
    for item in subtotals:
      if item[1] > y:
        bar.append(' o ')
      else:
        bar.append(' ' * 3)
    bar.append(' ')
    bar.append('\n')
    y -= 10
    space = (len(subtotals))*3 + 1

  #add header and join to string
  bar = 'Percentage spent by category\n' + ''.join([str(item) for item in bar])
  #add dashes
  bar += ' ' * 4 + '-' + '-' * len(subtotals) * 3 + '\n'

  # Build category labels
  labels = []
  x = 0
  length = len(max([item[0] for item in subtotals], key=len))
  for line in range(length):
    labels.append(' ' * 4)
    for item in subtotals:
      try:
        labels.append(' ')
        labels.append(item[0][x])
        labels.append(' ')
      except IndexError:
        labels.append(' ' * 2)
    labels.append(' \n')
    x += 1

  #add label as string
  bar += ''.join([item for item in labels])[:-1]

  return bar