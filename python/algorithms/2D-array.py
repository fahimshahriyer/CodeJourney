import sys
# Given a  2D Array, :

# 1 1 1 0 0 0
# 0 1 0 0 0 0
# 1 1 1 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# We define an hourglass in  to be a subset of values with indices falling in this pattern in 's graphical representation:

# a b c
#   d
# e f g
# There are  hourglasses in , and an hourglass sum is the sum of an hourglass' values.
# Input Format
# There are  lines of input, where each line contains  space-separated integers describing 2D Array ; 
# every value in  will be in the inclusive range of  to .

# Print the largest (maximum) hourglass sum found in .

A = [
    [1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [0, 0, 2, 4, 4, 0],
    [0, 0, 0, 2, 0, 0],
    [0, 0, 1, 2, 4, 0]
]

# A = []
# for arr_i in range(6):
#    arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
#    A.append(arr_t)

maxsum = 0

for row in range(len(A)-2):
    for column in range(len(A[row])-2):
        tl = A[row][column]
        tc = A[row][column+1]
        tr = A[row][column+2]
        mc = A[row+1][column+1]
        bl = A[row+2][column]
        bc = A[row+2][column+1]
        br = A[row+2][column+2]
        print(row,column)
        print(tl,tc,tr,mc,bl,bc,br)
        sum = tl+tc+tr+mc+bl+bc+br
        maxsum = max(sum, maxsum)


print(maxsum)