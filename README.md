# Bank Spending

To check how much do I spend.

### Install Python Requirements

```
pip install -r requirements.txt
```

### JSON to CSV

My gives me XML file, which I convert to JSON and ultimately to the desired CSV format.

I create it in CSV so that I can load in Google Sheet and create graphs of my spending.

```
python3 bank_json_to_csv.py
```

It gives me `spend.csv` file.

### Categorizing Spending

This tells me which categories I spend the most. Currently I have these categories.

* Rent
* Groceries
* Eating Out
* Utilities
* Subscriptions
* Sports and Fitness
* Misc

Feel free to create your own categories by tweaking send_by_group.py file.

```
python3 send_by_group.py
```

#### Result

You will get the output like this.

```txt
Category
Rent                  1XX0.00
Eating Out            1XX7.00
Online Shopping        5X9.00
Misc                   4X0.00
Groceries              2X7.39
Subscriptions          2X0.03
Utilities              1X4.03
Sports and Fitness     3X0.00
```

Spend wisely!