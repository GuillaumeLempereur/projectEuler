#Problem 150

"""
Resolution by Kadane's algorithm adapted to this problem
# Kadane's algo
def max_subarray(A):
    max_ending_here = max_so_far = A[0]
    for x in A[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far


>> not possible


Let think about the PB:
the last line is <0 otherwise you would not take it


new algo:

for each element i; for each space



try to approximate the sum of adjacent element: a%A+b%A+c%A = (a+b+c)%A+ x*A !!! Find this x

"""



