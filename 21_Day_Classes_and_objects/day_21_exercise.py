print("\n### Exercise 21 ###")
print("------------------")

from statistics import *

print("Level 1\n-------")

class Statistics:
    def __init__(self, data):
        self.data = data

    def count(self):
        return len(self.data)

    def sum(self):
        return sum(self.data)

    def min(self):
        return min(self.data)

    def max(self):
        return max(self.data)

    def range(self):
        return self.max() - self.min()

    def mean(self):
        return round(mean(self.data))

    def median(self):
        return median(self.data)

    def mode(self):
        md = mode(self.data)

        count_dict = {}
        for age in self.data:
            if age in count_dict:
                count_dict[age] += 1
            else:
                count_dict[age] = 1

        return md, count_dict[md]

    def std(self):
        return round(pstdev(self.data), 1)

    def var(self):
        return round(pvariance(self.data), 1)

    def freq_dist(self):
        freq = {}
        for age in self.data:
            if age in freq:
                freq[age] += 1
            else:
                freq[age] = 1

        freq_percent = []
        for value, count in freq.items():
            percentage = count / len(self.data) * 100
            freq_percent.append((percentage, value))

        return sorted(freq_percent, reverse=True)


ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

data = Statistics(ages)

print('Count:\t', data.count())
print('Sum:\t', data.sum())
print('Min:\t', data.min())
print('Max:\t', data.max())
print('Range:\t', data.range())
print('Mean:\t', data.mean())
print('Median:\t', data.median())
print('Mode:\t', data.mode())
print('Standard Deviation:\t', data.std())
print('Variance:\t', data.var())
print('Frequency Distribution:\t', data.freq_dist())




print("\n\nLevel 2\n-------")

class PersonAccount:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = []
        self.expenses = []

    def add_income(self, amount, description):
        self.incomes.append((amount, description))

    def add_expense(self, amount, description):
        self.expenses.append((amount, description))

    def total_income(self):
        total = 0
        for income in self.incomes:
            total += income[0]

        return total

    def total_expense(self):
        total = 0
        for expense in self.expenses:
            total += expense[0]

        return total

    def account_balance(self):
        return self.total_income() - self.total_expense()

    def account_info(self):
        return(f'Name: {self.firstname} {self.lastname}\n'
               f'Total income:\t {self.total_income()}\n'
               f'Total expenses:\t {self.total_expense()}\n'
               f'Account balance: {self.account_balance()}')


account = PersonAccount('Samindi', 'Mendis')
account.add_income(3500, 'Salary')
account.add_income(1500, 'Freelance Work')

account.add_expense(650, 'Rent')
account.add_expense(200, 'Groceries')

print(account.account_info())