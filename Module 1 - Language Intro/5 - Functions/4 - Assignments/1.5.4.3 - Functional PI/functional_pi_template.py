import math


def my_pi(target_error):
    """
    Implementation of Gauss–Legendre algorithm to approximate PI from https://en.wikipedia.org/wiki/Gauss%E2%80%93Legendre_algorithm

    :param target_error: Desired error for PI estimation
    :return: Approximation of PI to specified error bound
    """

    ### YOUR CODE HERE ###
    a = 1
    b = 1 / (math.sqrt(2))
    t = 1 / 4
    p = 1
    ans = 0
    while math.pi - ans > target_error:
        # if a variable has n, the variable is from previous iteration (old). If not, it is current (new).
        an = a  # store old a
        bn = b  # store old b
        a = (an + bn) / 2  # new a is old a + old b, divided by two
        b = math.sqrt(an * bn)  # new b is old a times old b, square rooted
        pn = p  # store old p
        p = 2 * pn  # new p is 2 times old p
        tn = t  # store old t
        t = tn - pn * (math.pow(a - an, 2))
        ans=(math.pow(a + b,2))/(4*t)
    # change this so an actual value is returned
    return (math.pow(a + b,2))/(4*t)




desired_error = 1E-10

approximation = my_pi(desired_error)

print("Solution returned PI=", approximation)

error = abs(math.pi - approximation)

if error < abs(desired_error):
    print("Solution is acceptable")
else:
    print("Solution is not acceptable")
