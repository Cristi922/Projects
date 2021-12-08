# ========================== Repeated String ==========================

# s = "abcacabcacabcacabcacabcacabcacabcacabcacabcacabcac"
# n = 8
#
# # You have a string of letters that repeat infinitely defined as s
#
# # How many times does the letter a repeat in the first n letters
#
#
#
# print(s.count("a") * (n // len(s)) + s[:n % len(s)].count("a"))




from array import *

T = [[11, 12, 5, 2], [15, 6, 10], [10, 8, 12, 5], [12,15,8,6]]

print(T[0])

print(T[1][2])

























# ========================== CLOUD HOPPING ==========================

# There are clouds with index 0 and index 1
    # Clouds with index 0 can be jumped, clouds with index 1 cannot be jumped

# The player can jump on on clouds that have index 0
    # The player can jump 1 or 2 indexes.

# c = [0, 0, 1, 0, 0, 1, 0]
#
# count = 0
# i = 0
#
# while i < len(c) - 1:
#     if i+2 < len(c) and c[i+2] != 1:
#         count = count + 1
#         i = i + 2
#     else:
#         count = count + 1
#         i = i + 1
#     print(count)


# ========================== SECOND HACKERRANK PROBLEM HIKER STEPS ==========================

# # Function gets two arguments steps and path
#
# path = "UDDDUDUU"
# # The hiker starts at sea level
# # If he steps downhill he gets -1 compared to sea level he enters a valley
#
# height = 0
# valley = 0
# for steps in path:
#     if steps == "D":
#         height = height - 1
#     elif steps == "U":
#         height = height + 1
#     if steps == "U" and height == 0:
#         valley = valley + 1
# print(valley)
#
# # if steps < 1:
# #     valley = valley + 1
#     # If he is under sea level he is in a valley
#     # If he reaches sea level he is out of the valley
#         # If the last step he took was uphill than he got out of the valley
#         # Count the valley
#
# # If he steps uphill he gets + 1 compared to sea level he gets to a mountain
#     # While he is above sea level he is in a mountain
#     # When he is at sea level he is out of the mountain.
#
#
# # Find out through how many valleys he has been through





# ========================== FIRST HACKERRANK PROBLEM, COUNT SOCKS ==========================

# # def sockMerchant(n, ar):
# # Declare a variable that represents number of socks
# n = int
# # Declare an array that has the colors of socks represented by integers
# # [1, 1, 2, 2, 3, 3, 2, 4]
#
# ar = [1, 1, 2, 2, 2, 2, 3, 3, 3, 4]
# # Sort the aray of integers
#
# sorted_ar = sorted(ar)
#
# count = 0
# a = range(len(sorted_ar))
# i = 0
#
# # if the first index is equal to the second index, add 1 to count
# # if the second index is equal to third index, don't add 1 to count, and start iterating again from the third index.
# # if third index is equal to forth index, add 1 to count
#
# # while i < len(sorted_ar) - 1:
# #     if sorted_ar[i] == sorted_ar[i + 1]:
# #         count = count + 1
# #         if i < len(sorted_ar) - 2:
# #             if sorted_ar[i + 1] == sorted_ar[i + 2]:
# #                 i = i + 1
# #
# #     i = i + 1
# # print(count)
#
#
#
#
# # See how many identical pairs of the same integer there are using dictionaries
#     # See where how many identical values there are
#     # Add the integer to a counter
# # Divide number by to using modulo
# # Add result to count
#
# sorted_socks = {}
#
# for i in sorted_ar:
#     sorted_socks[i] = 0
#
# for i in sorted_ar:
#     sorted_socks[i] = sorted_socks[i] + 1
#
# count = 0
#
# for (key) in sorted_socks:
#     count = int(sorted_socks[key] / 2) + count
#     # print(sorted_socks[key])
#     print(count)







# dictOfWords = { i : 5 for i in listOfStr }


# print(list_of_socks)
# print(list_of_socks[0])
