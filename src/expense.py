expenses=[]
def add_expense():
   title= input("Enter title:")
   amount=float(input("Enter amount:"))
   print("Adding expense...")
   expense = {
      "title":title,
      "amount":amount
}
   expenses.append(expense)
  
def view_expenses():
    print("Viewing expenses...")
    if not expenses:
       print("=======No expense found======") 
    else:
     i=0    
     for expense in expenses:
      i+=1
      print(f'{i}.{ expense["title"]}  Rs.{expense["amount"]}')
def delete_expense():
    print("Deleting expense...")

