import math

"""
Use the Gauss-Legendre Algorithm to estimate Pi. Perform 10 approximation loops. Once complete, return the approximation.
:return:
"""

# a variable to hold your returned estimate for PI. When you are done,
# set your estimated value to this variable. Do not change this variable name
pi_estimate = 0

"""
Step 1: Declare and initialize all the values for the Gauss-Legendre algorithm
"""

# modify these lines to correct set the variable values
a = 1
b = 1 / (math.sqrt(2))
t = 1/4
p = 1

# perform 10 iterations of this loop
for i in range(1, 10):

    """
    Step 2: Update each variable based upon the algorithm. Take care to ensure
    the order of operations and dependencies among calculations is respected. You
    may wish to create new "temporary" variables to hold intermediate results
    """

    ### YOUR CODE HERE ###

    # if a variable has n, the variable is from previous iteration (old). If not, it is current (new).
    an = a # store old a
    bn = b # store old b
    a = (an + bn)/2 # new a is old a + old b, divided by two
    b = math.sqrt(an * bn) # new b is old a times old b, square rooted
    pn = p # store old p
    p = 2*pn # new p is 2 times old p
    tn = t # store old t
    t = tn - pn*(math.pow(a - an,2))

    # print out the current loop iteration. This is present to have something in the loop.
    print("Loop Iteration: ", i)
    it_est = (math.pow(a + b,2))/(4*t)
    print("Iteration Estimate: ", it_est)

"""
Step 3: After iterating 10 times, calculate the final value for PI
"""

# modify this line below to estimate PI
pi_estimate = (math.pow(a + b,2))/(4*t)

print("Final estimate for PI: ", pi_estimate)
print("Error on estimate: ", abs(pi_estimate - math.pi))
