from collections import Counter

portfolio = [
    ('GOOG', 100, 490.1),
    ('IBM', 50, 91.1),
    ('CAT', 150, 83.44),
    ('IBM', 100, 45.23),
    ('GOOG', 75, 572.45),
    ('AA', 50, 23.15)
]

total_shares = Counter()

total_shares_old = {}

for names, shares, price in portfolio:
    total_shares[names] += shares

for name, share, price in portfolio:
    total_shares_old[name] = share

