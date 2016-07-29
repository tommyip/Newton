"""
Conjugate calculator v0.1.0

===========================
Example:
Real part > 6
Imaginary part > 3
Result >> Z = 6 - i3
"""
real_error = True
i_error = True

while real_error:
    try:
        real_part = int(input("Real part > "))
        real_error = False
    except ValueError:
        print("Please enter a number!")

while i_error:
    try:
        i_part = int(input("Imaginary part > "))
        i_error = False
    except ValueError:
        print("Please enter a number!")

sign = '-' if i_part > 0 else '+'

print("Result >> {} {} i{}".format(real_part, sign, abs(i_part)))