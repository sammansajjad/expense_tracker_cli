import menu
import expense
def main():
    while True:
     print("=== Expense Tracker CLI ===")
     print("Welcome!")
     menu.show_menu()
     choice=input("Enter your choice: ")
     if choice=="1":
        expense.add_expense()
     elif choice=="2":
        expense.view_expenses()
     elif choice=="3":
        expense.delete_expense() 
     elif choice=="0":
        break
     else:
        print("Invalid Input")    

if __name__ == "__main__":
    main()
