import pcost
import sys

if __name__ == '__main__':
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = 'Data/portfolio.csv'

    cost = pcost.portfolio_cost(filename)
    print('Total cost:', cost)