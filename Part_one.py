#Ask the user to enter their principal amount
principal_input = input ("Please enter your principal amount:")

#Ask the user to enter their yearly rate 
rate_input = input ("Please enter your yearly rate:")

#Ask the user to enter their term period, in years
term_input = input ("Please enter the term of the loan in years:")

#Convert all input strings to floats 
principal = float (principal_input)
rate = float (rate_input)
term = float (term_input)

#Calculate the interest amount
interest_amount = (principal*rate*term)/100

#Print the results 
print (" The total interest amount would be: $", interest_amount)
