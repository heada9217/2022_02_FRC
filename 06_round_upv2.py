import math

from numpy import round_

def num_check(question, error, num_type):
    
    error = "Please enter a whole number greater than zero"


    valid = False
    while not valid:

        try: 
            response = num_type(input(question))

            if response <= 0:
                print(error)
            else:
                return response
        

        except ValueError:
            print(error)

def round_up(amount, var_round_to):


    return math.ceil(amount / var_round_to) * var_round_to

#Main Routine starts here
how_many = num_check("How many times? ", "Cant be 0", int)
total = num_check("Total Costs? ","More than zero", float)
profit_goal = num_check("Profit Goal?", "More than 0", float)
round_to = num_check("Round to nearest...? ", "Can't be 0", int)

sales_needed = total + profit_goal

print("Total: ${:.2f}".format(total))
print("Profit Goal: ${:.2f}".format(profit_goal))

selling_price = sales_needed / how_many
print("Selling Price (unrounded): ${:.2f}". format(selling_price))

recommended_price = round_up(selling_price, round_to)
print("Recommended Price: ${:.2f}".format(recommended_price))
