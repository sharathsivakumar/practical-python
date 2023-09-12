# mortgage.py

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
number_months = 0
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000
actual_payment = 0

while principal > 0:
    number_months += 1
    if extra_payment_start_month <= number_months <= extra_payment_end_month:
        actual_payment = payment + extra_payment
        principal = principal * (1 + rate / 12) - actual_payment
        total_paid = total_paid + payment

    else:
        principal = principal * (1+rate/12) - payment
        total_paid = total_paid + payment

print('Total paid', total_paid)
print('Total Months',number_months)