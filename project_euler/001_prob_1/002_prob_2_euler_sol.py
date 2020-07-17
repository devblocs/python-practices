"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

Euler's Solution:

target=999
Function SumDivisibleBy(n)  
    p=target div n  
    return n*(p*(p+1)) div 2
EndFunction

Output SumDivisibleBy(3)+SumDivisibleBy(5)-SumDivisibleBy(15)
"""

def sum_divisible_by(num_range, num):
    result = num_range//num
    return num * (result * (result + 1))//2

num_range = 999
output = sum_divisible_by(num_range, 3) + sum_divisible_by(num_range, 5) - sum_divisible_by(num_range, 15)

print(f"Sum of all numbers between the range of 0 to {num_range} is {output}")

