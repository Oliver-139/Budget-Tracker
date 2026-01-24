#print("Welcome! This is version 1 of my Budget planner.")
#Monthly_Income = input("What is your current income per month?")
#Monthly_Budget = input("What is your current monthly budget?: ")
#print(f"Your monthly income is £{Monthly_Income} and your budget is {Monthly_Budget}")

print("Now lets dive into your monthly spendings!")


categories = []
print("Please name some of the categories that are apart of your monthly expenses")
while True:
    category_name = input("Please enter an expense category or type 'done' to finish:")

    if category_name.lower() =="done":
        break

    else: categories.append(category_name)


expenses = {}
for item in categories:
    print(f"What is the price of {item}?")
    amount = float(input())
    expenses[item] = amount
    
print(f"{expenses}")