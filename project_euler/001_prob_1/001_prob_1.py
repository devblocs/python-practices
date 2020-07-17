"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

"""

def sum_list(num_range):
    sum_list = sum(num for num in range(0, num_range) if num%3 == 0 or num%5 == 0)
    return sum_list

num_range = 1000

print(f"Sum of all numbers between the range of 0 to {num_range} is {sum_list(num_range)}")
