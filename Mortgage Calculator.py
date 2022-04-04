print("""Thanks for checking out my Mortgage Calculator!  This script is very straightforward.
If your credit score is over 750 it assumes you'll pay 10% of the total loan in down payment.
Between 650 and 750, 20%, and 30% otherwise.  The rest is just basic arithmetic, automated.  :-)""")
credit = int(input("Enter your credit score: "))
loan = int(input("Enteryour loan amount: "))
interest = float(input("Enter your interest rate as a decimal: "))
years = int(input("Enter number of years(10, 15, or 30): "))
if credit > 750:
    downPayment = loan * .1
elif credit < 750:
        downPayment = loan * .2

Rmdr = loan - downPayment
Rmdr = Rmdr * interest + Rmdr
monthly = Rmdr / years / 12
input(f"Your loan comes to a ${downPayment} down payment at ${monthly} per month on a {years} years fixed mortgage.")
