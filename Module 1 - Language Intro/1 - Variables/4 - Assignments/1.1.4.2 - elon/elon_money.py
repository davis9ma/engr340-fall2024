"""
This problem requires you to calculate compounding interest and final value of a  US treasury deposit based upon
current interest rates (that will be provided). Your analysis should return the final value of the investment
after a 10-year and 20-year period. The final values should be stored in the variables "ten_year_final"
and "twenty_year_final", respectively. Perform all your calculations in this file. Do not perform the calculations by hand
and simply write in the final result.

Prompt: On October 27th, 2022, Elon Musk purchased Twitter for $44B in total, with reportedly $33B of his own money. Since
that time, it appears this investment has not worked out. If Elon has instead bought $44B of US Treasury Bonds, how much
would his investment be worth in 10-year and 20-year bonds? Assume the 10-year bonds pay 3.96%,
the 20-year bonds pay 4.32%, with each compounding annually.
"""

### all your code below ###

principal = (33 * (10**9))
r1 = 3.96
r2 = 4.32
n1 = 10
n2 = 20

print("Principal value is $", principal)
print("10 year rate is ",r1)
print("20 year rate is ",r2)

# final answer for 10-year
ten_year_final = principal * ((1 + (r1 / 100)) ** n1)

print("10-year bond worth is $", round(ten_year_final,2)) # I looked up and used the round function to get this into the right format

# final answer for 20-year
twenty_year_final = principal * ((1 + (r2 / 100)) ** n2)

print("20-year bond worth is $", round(twenty_year_final,2)) # I looked up and used the round function to get this into the right format
