valid_categories = ["food", "entertainment", "utilities", "transport", "other"]

def get_monthly_income():
    while True:
        try:
            income = float(input("What is your current income per month?"))
            if income < 0: #makes sure the income ia bigger than 0, if its not - loops until it is 
                print("Income cannot be a negative number") #continues until it is true
                continue
            return income
        except ValueError:
            print("Enter a valid number") #this results if the user types something that isnt a letter

def get_monthly_budget(income):
    while True:
        try:
            budget = float(input("What is your current monthly budget?:"))
            if budget < 0: #makes sure the budget is higher than 0, otherwise it loops until the condition is fulfilled
                print("Monthly Budget cannot be a negative number") #just in case the user types a negative number
                continue
            if budget > income:
                print("Your budget cannot be greater than the income") #makes sure whatever the budget it, it cannot exceed the income otherwise error message
                continue
            return budget
        except ValueError:
            print("Please enter a valid number") #must be a number above 0, otherwise previous error message gets triggered

def get_expenses():
    expenses = {}
    print("Please enter your expenses (type 'done' to finish).")
    while True:
        name = input("Enter expense name:").strip()
        if name.lower() =="done": #done can be typed in any series of capitalisation. until done is typed, user is repeatedly prompted
            break
        while True:
            date = input("Enter date (YYYY-MM-DD): ").strip()
            parts = date.split("-")
            if len(parts) == 3 and all(p.isdigit() for p in parts):
                break
            print("Invalid date format. Please enter YYYY-MM-DD.")

        while True:
            try: 
                amount = float(input(f"What is the price of {name}?")) #converts to float so it can be used later on
                if amount <=0:
                    print("Price must be greater than 0.")
                    continue
                expenses[name] = amount
                break
            except ValueError:
                print("Please enter a valid number for the price")
        while True:
            category = input("Enter category(food, entertainment, utilities, transport, other):").strip(). lower() #takes away spaces and allows for all capitalisation
            if category in valid_categories:
                break
            else:
                print("Invalid category. Please choose from the listed options: food, entertainment, utilities, transport and other!") 

        
        expenses[name] = {
        "price": amount,
        "category": category
        }
    return expenses 

def calculate_total(expenses): #this basically just calculates the total and saves it for later when it is all reported back to you 
    total = 0 #this is the beginning total amount
    for value in expenses.values():
        total+=value["price"]
    return total
    
def handle_savings(remaining_budget):
    savings = 0 
    choice = input("Would you like to add any of the income into the savings pot?")
    if choice == "yes":
        while True: #if the choice is no then it just skips all this and returns the savings and the required budget
            try:
                amount = float(input("Enter your amount to allocate"))
                if amount < 0:
                    print("Savings cannot be negative")
                    continue
                if amount > remaining_budget:
                    print("You cannot save more than you currently have. Please try again")
                    continue
                savings = amount 
                remaining_budget -= savings
                break
            except ValueError:
                print("Enter a valid number")
    return savings, remaining_budget


def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded")
        return
    print("Name Date Category Amount")
    for name, exp in expenses.items():
        print(name, exp["date"], exp["category"], exp["price"])

def filter_expenses(expenses):
    category = input("Enter category to filter (food, entertainment, utilities, transport, other): ").strip().lower()
    if category not in valid_categories:
        print("Invalid category")
        return
    found = False
    for name, exp in expenses.items():
        if exp["category"] == category:
            print(name, exp["date"], exp["price"])
            found = True
    if not found:
        print("No expenses found in this category")

def main():
    print("Welcome to your expense tracker!")

    income = get_monthly_income()
    budget = get_monthly_budget(income)
    expenses = {}

    while True:
        print("----- Menu -----")
        print("1. Add expense")
        print("2. View all expenses")
        print("3. Filter expenses by category")
        print("4. Calculate total expenses")
        print("5. View the remaining budget and savings")
        print("6. Exit")

        choice = input("Select an option (1-6): ").strip()

        if choice == "1":
            new_expenses = get_expenses()
            expenses.update(new_expenses)
            print("Expense(s) added successfully!")

        elif choice == "2":
            view_expenses(expenses)

        elif choice == "3":
            filter_expenses(expenses)

        elif choice == "4":
            total = calculate_total(expenses)
            print("Total expenses: £" + str(total))

        elif choice == "5":
            total_spent = calculate_total(expenses)
            remaining_budget = budget - total_spent
            savings, remaining_budget = handle_savings(remaining_budget)
            print("Total spent: £" + str(total_spent))
            print("Savings: £" + str(savings))
            print("Remaining budget: £" + str(remaining_budget))

        elif choice == "6":
            print("Exiting Expense Tracker. Goodbye!")
            break

        else:
            print("Invalid option. Please choose 1-6.")

if __name__ == "__main__":
    main()



