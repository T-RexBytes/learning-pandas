import pandas as pd

df = pd.read_csv("data.csv")

total_money = df["amount"].sum()
print(f"Total Money Spend is : {total_money}")

print(df.groupby("category")["amount"].sum())

max_row = df.loc[df["amount"].idxmax()] #idxmax() gave the max spend amount and catagory row location
highest_amount = max_row["amount"]
highest_category = max_row["category"]
highest_note = max_row["note"]
print(f"The Highest Amount Ever Spent is : {highest_amount} in category '{highest_category}' on '{highest_note}'")

df["date"] = pd.to_datetime(df["date"]) #make the date datatype form str to pandas datetime object
months = [
	"January", "February", "March", "April", "May", "June",
	"July", "August", "September", "October", "November", "December"
]
month = int(input("Enter The Number of the Month : "))
if 1 <= month <= 12:
    monthly_expense = df[df["date"].dt.month == month]
    total = monthly_expense["amount"].sum()
    print(f'Total Expense in {months[month-1]} is : {total}')
else:
    print("Invalid month number!")
    
    
avg_spend = df["amount"].mean()
print(f"Your Average Spending is : {avg_spend:.2f}")


print(df.sort_values(by="amount", ascending=False)) #sortvalue() makes the data sort 
 