"""
For investments over $1M it can be typically assumed that they will return 5% forever.
Using the [2022 - 2023 JMU Cost of Attendance](https://www.jmu.edu/financialaid/learn/cost-of-attendance-undergrad.shtml),
calculate how much a rich alumnus would have to give to pay for one full year (all costs) for an in-state student
and an out-of-state student. Store your final answer in the variables: "in_state_gift" and "out_state_gift".

Note: this problem does not require the "compounding interest" formula from the previous problem.

"""

### Your code here ###

in_state_tuition = 13376 # Cost of in-state tuition & fees for 2022-2023
out_of_state_tuition = 30466 # Cost of out-of-state tuition & fees for 2022-2023
constant_fees = (5772+6268+1176+1968+2156+76) # Sum of fees for this period that remain constant

print("Constant fees for the year are $", constant_fees) # displays the constant fees
print("In-State tuition and fees are $", in_state_tuition) # displays the in-state tuition value
print("Out-of-State tuition and fees are $", out_of_state_tuition) # displays the out-of-state tuition value

print() # prints an empty line for readability

in_state_gift = in_state_tuition+constant_fees # sums the fees to get in-state gift value

print("Total In-State gift value is $", in_state_gift) # displays in-state gift value

out_state_gift = out_of_state_tuition+constant_fees # sums the fees to get out-of-state gift value

print("Total Out-of-State gift value is $", out_state_gift) # displays the out-of-state gift value
