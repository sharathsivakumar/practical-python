# pcost.py
#
# Exercise 1.27

def portfolio_cost(filenames):
    cost = 0.0
    try:
        f = open(filename, 'rt')
    except FileNotFoundError:
        print("file not found", filename)
    else:
        with f:
            headers = next(f)
            for rownum,shares in enumerate(f):
                row = shares.split(',')
                try:
                    cost += int(row[1]) * float(row[2])
                except ValueError:
                    print(f'Bad row{rownum}:, {row}')
    return cost
