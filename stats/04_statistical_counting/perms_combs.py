'''
Factorial determines cardinality/magnitude of a set of outcomes
'''

def factorial(num):
    prod = 1
    for n in range(2, (num+1)) :
        prod *= n
    return prod 



'''
Factorial Breakout Slide 10

There are ten people standing in a line for beignets at the world famous cafe du monde in New Orleans. How many different ways could the ten people be arranged in the queue?
>> 10! = 3628800

Given that the line was formed organically (i.e, people got into line as they arrived without any organization or coordination), what is the probability that they are standing in the queue in alphabetical order. Assume everyone has a different last name?
>> 1 / 10!
'''



'''
Permutations
P(n, k) = n! / (n - k)!
nPk
'''

'''
You have 10 students and you are conducting a science fair where 4 students will win 1st, 2nd, etc. How many different arrangements of those 4 winners is possible?

P(10, 4) = 10! / (10 - 4)!

10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1
= --------------------------------------
                 6 * 5 * 4 * 3 * 2 * 1

10 * 9 * 8 * 7  = 5040

'''

'''
Code the permutations(n, k) function.

P(n, k) = n! / (n - k)!
'''
def perm(n, k):
    return int(factorial(n) / factorial(n-k))

# print(perm(10, 4))


'''Computationally better permutations func'''
# def perm(n, k):
# 	perm = 1
# 	for i in range(n, n-k, -1):
# 		perm *= i
# 	return perm


'''
Five pets, and you have 5 pet beds. What are all the ways that you arrange those five pets in their beds.
'''

base_5 = ['bat', 'cat', 'frog', 'eel', 'hamster']

