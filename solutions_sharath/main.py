# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def calculate_number_of_bill(building_height):
    bill_height = .11 * 0.001
    number_bills = 1
    number_days = 1

    while number_bills * bill_height < building_height:
        number_bills *= 2
        number_days += 1
    return number_days


def bounce_calculate(initial_height):
    dampening_factor = 3 / 5
    height = initial_height
    for i in range(10):
        height *= dampening_factor
        print("Height: ", round(height, 4))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("The number of days: ", calculate_number_of_bill(442))
    bounce_calculate(100)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
