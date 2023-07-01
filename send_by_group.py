import pandas as pd

# Load the CSV file
data = pd.read_csv("spend.csv")


# Define the categories based on the merchant in the 'Description' field
def categorize(description: str):
    """
    Make tweak in these if/else branch based on your spending.

    And as a habit start adding tags when you paying.

    Ultimately use those tags to create group and your spending patters.
    """
    description = description.lower()
    if "bigbasket" in description:
        return "Groceries"
    elif (
        "biryani" in description
        or "gokhana" in description
        or "take out" in description
        or "dine in" in description
        or "upi lite" in description
        or "cafe" in description
        or "eat out" in description
    ):
        return "Eating Out"

    elif (
        "subscription" in description
        or "playstore" in description
        or "netflix" in description
    ):
        return "Subscriptions"
    elif "amazonsellerservices" in description or "flipkart" in description:
        return "Online Shopping"
    elif "badminton" in description:
        return "Sports and Fitness"
    elif (
        "recharge" in description
        or "electricity" in description
        or "petrol" in description
        or "bill" in description
    ):
        return "Utilities"
    elif "rent" in description:
        return "Rent"
    else:
        return "Misc"


# Apply the categorization function to the 'Description' column
data["Category"] = data["Description"].apply(categorize)

# Group by the 'Category' and sum the 'Debit' column to get the total spend in each category
spends = data.groupby("Category")["Debit"].sum()

# Sort spends in descending order
spends = spends.sort_values(ascending=False)

# Display the category with the highest spending
max_spending_category = spends.idxmax()
max_spending_value = spends.max()

print(spends)

print(
    f"You have spent the most on {max_spending_category}, with a total of {max_spending_value}."
)
