#expense tracker

expensesList = []  #lsit of expenses
print("Welcome To Expense Tracker..!")

while True:
    print("===Menu===")
    print("1. Add Expense")
    print("2.View all expenses")
    print("3. View total expenses")
    print("4. Exit")

    choice = int(input("Enter your choice : "))

    if(choice == 1):
        date = input("enter your date : ")
        category =input(" enter the category(food,makeup,travle) :")
        description=input("enter expense description : ")
        amount = float(input("enter total amount : ") )
        
        expense = {
            "date" : date,
            "category" : category,
            "description" : description,
            "amount" : amount
        }
        expensesList.append(expense)
        print(" \n Expenses added succesfully..!")


    elif(choice == 2):
            if(len(expensesList)== 0):
                print("firstly add expenses ")
            else:
                print(" === your expense ===")

                count = 1
                # for each in expenses:
                #     print(f"expense number {count} --> {each['date']}, {each['category']}, {each['description']}, {each['amount']}")
                #     count = count + 1

                for  each in expensesList:
                   print(f"expense number {count} --> {each['date']}, {each['category']}, {each['description']}, {each['amount']}") 
                   count = count + 1

    elif(choice == 3):
        total = 0
        for each in expensesList:
            total = total + each["amount"]

        print("\n total expense = ",total)

    elif(choice==4) :
        print("EXIT")
        break
    else :
        print("invalid choice ")
