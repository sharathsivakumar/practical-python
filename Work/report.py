# report.py
#
# Exercise 2.4
import csv


def read_portfolio_tuple(filename):
    cost = 0.0
    portfolio = []
    try:
        f = open(filename, 'rt')
    except FileNotFoundError:
        print("File not found:",filename)
    else:
        with f:
            rows = csv.reader(f)
            headers = next(rows)
            for row in rows:
                try:
                    holding = (row[0], int(row[1]), float(row[2]))
                except ValueError:
                    print("Bad row:", row)
                else:
                    portfolio.append(holding)
    return portfolio

def read_prices(filename):
    portfolio = {}
    try:
        f = open(filename, 'r')
    except FileNotFoundError:
        print("File not found:",filename)
    else:
        with f:
            for rows in f:
                if len(rows.strip()) != 0:
                    row = rows.split(',')
                    print("Row:",row)
                    portfolio[row[0]] = float(row[1])
                else:
                    print("Empty row")
    return portfolio

portfolio =  read_portfolio_dict('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')

total_cost=0.0
purchase_cost = 0.0

for s in portfolio:
    total_cost


