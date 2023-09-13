# report.py
#
# Exercise 2.4
import csv


def read_portfolio(filename):
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


