"""
For investments over $1M it can be typically assumed that they will return 5% forever.
Using the [2022 - 2023 JMU Cost of Attendance](https://www.jmu.edu/financialaid/learn/cost-of-attendance-undergrad.shtml),
calculate how much a rich alumnus would have to give to pay for one full year (all costs) for an in-state student
and an out-of-state student. Store your final answer in the variables: "in_state_gift" and "out_state_gift".

Note: this problem does not require the "compounding interest" formula from the previous problem.

"""

### Your code here ###

in_state_cost = 30792 # Cost of total in-state payment
out_of_state_cost = 47882 # Cost of total out-of-state payment
interest = 5

print("In-State cost is $", in_state_cost) # displays the in-state tuition value
print("Out-of-State cost is $", out_of_state_cost) # displays the out-of-state tuition value
print("Interest value is ", interest,"%") # displays interest rate

print() # prints an empty line for readability

in_state_gift = (in_state_cost/(interest/100)) # Calculates the total gift required

print("Total In-State gift value is $", in_state_gift )# displays in-state gift value

out_state_gift = (out_of_state_cost/(interest/100)) # calculates the total gift required

print("Total Out-of-State gift value is $", out_state_gift) # displays the out-of-state gift value