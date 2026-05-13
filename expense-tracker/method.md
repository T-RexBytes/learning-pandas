Expense Tracker - Functions and Methods Used

1. Load the CSV file
   - pd.read_csv("data.csv")

2. Show total money spent
   - df["amount"].sum()

3. Show category-wise spending
   - df.groupby("category")["amount"].sum()

4. Show the highest single expense
   - df["amount"].idxmax()
   - df.loc[...]

5. Show spending for a chosen month
   - pd.to_datetime(df["date"])
   - df["date"].dt.month
   - input()
   - df[df["date"].dt.month == month]

6. Show average daily spending
   - df["amount"].mean()

7. Sort expenses from highest to lowest
   - df.sort_values(by="amount", ascending=False)
