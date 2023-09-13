# pcost.py
#
# Exercise 1.27

def portfolio_cost(filename):
    cost = 0.0
    try:
        f = open(filename, 'rt')
    except FileNotFoundError:
        print("file not found", filename)
    else:
        with f:
            headers = next(f)
            for shares in f:
                row = shares.split(',')
                try:
                    cost += int(row[1]) * float(row[2])
                except ValueError:
                    print("Bad row", row)
    return cost
