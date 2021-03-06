#import libraries
import pandas
import math

# *** Functions go here ***

#checks that input is either a float orr an 
# integer that is more than zero. Takes in custom error message.
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


#Checks that user has entered yes / no to a question 
def yes_no(question):



    to_check = ["yes", "no"]

    valid = False 
    while not valid:

        response = input(question).lower()

        for var_item in to_check:
            if response == var_item:
                return response
            elif response == var_item[0]:
                return var_item
        
        print("Please enter either yes or no...\n")

#Checks that string response is not blank
def not_blank(question, error):

    valid = False
    while not valid: 
        response = input(question)

        if response == "":
            print("{}. \nPlease try again. \n".format(error))

        return response

#currency formatting function
def currency(x):
    return"${:.2f}".format(x)

#Gets expenses, returns list which has the data frame and sub total
def get_expenses(var_fixed):
    
    item_list = []
    quantity_list = [] 
    price_list = [] 

    variable_dict = {
        "Item": item_list,
        "Quantity": quantity_list,
        "Price": price_list
    }

    item_name = ""
    while item_name.lower() != "xxx":

        print()
        #get name, quantity and item
        item_name = not_blank("Item name:", "The component name cannot be blank.")
        if item_name.lower() == "xxx":
            break

        if var_fixed == 'variable':
            quantity = num_check("Quantity: ", "The amount must be a whole number", int)

        else:
            quantity = 1

        price = num_check("How much for a single item? $", "The price must be a number more than zero", float)

        #Add item, quantity and price to list 
        item_list.append(item_name)
        quantity_list.append(quantity)
        price_list.append(price)

    expense_frame = pandas.DataFrame(variable_dict)
    expense_frame = expense_frame.set_index('Item')

    #Calculate cost of each component
    expense_frame['Cost'] = expense_frame['Quantity'] * expense_frame['Price']

    #Find sub total 
    sub_total = expense_frame["Cost"].sum()

    #Currency Formatting (uses currency function)
    add_dollars = ['Price', 'Cost']
    for item in add_dollars:
        expense_frame[item] = expense_frame[item].apply(currency)

    return [expense_frame, sub_total]

#Prints expense frames
def expense_print(heading, frame, subtotal):
    print()
    print("**** {} Costs ***".format(heading))
    print(frame)
    print()
    print("{} Costs: {: .2f}".format(heading,subtotal))
    return ""

def profit_goal(total_costs):

    #Initialise variables and error message
    error = "Sorry, please enter a valid profit goal\n:"

    valid = False
    while not valid:

        #Ask for profit goal...
        response = input("What is your profit goal? (eg $500 or %50):")

        #check if first character is $...
        if response[0] == "$":
            profit_type = "$"
            #get amount (everything after the $)
            amount = response[1:]

        #checks if last character is %...
        elif response [-1] == "%":
            profit_type = "%"
            #Get amount (everything before the %)
            amount = response[:-1]

        else:
            #set response to amount for now
            profit_type = "unknown"
            amount = response
        
        try: 
            #Check amount is a number more than zero...
            amount = float(amount)
            if amount <= 0:
                print(error)
                continue
        
        except ValueError:
            print(error)
            continue
        
        if profit_type == "unknown" and amount >= 100:
            dollar_type = yes_no("Do you mean ${:.2f}?, y/n".format(amount))


            #Set profit type based on user answer above
            if dollar_type == "yes":
                profit_type = "$"
            else:
                profit_type = "%"

        elif profit_type == "unknown" and amount <100:
            percent_type = yes_no("Do you mean {}%?, y/n".format(amount))
            if percent_type == "yes":
                profit_type = "%"
            else:
                profit_type = "$"

        #return profit goal to main routine
        if profit_type == "$":
            return amount
        else: 
            goal = (amount / 100) * total_costs
            return goal

def round_up(amount, var_round_to):


    return math.ceil(amount / var_round_to) * var_round_to

def instructions():
    
    show_help = yes_no("Do you want to see the instructions?")

    if show_help == "yes":
        print()
        print("*** Fundraising Calculator Instructions ***")
        print()
        print("This program will help you to:")
        print()
        print("- ")

    return ""    


# *** Main Routine goes here ***
#ask user if they want instructions
want_instructions = instructions()

#Get user data 
product_name = not_blank("Product name: ", "The product name cannot be blank")
how_many = num_check("How many items will you be producing?"," The number of items must be a whole number more than zero", int)


print()
print("Please enter your variable costs below...")

#Get varuabke costs
variable_expenses = get_expenses("variable")
variable_frame = variable_expenses[0]
variable_sub = variable_expenses[1]

print()
have_fixed = yes_no("Do you have fixed costs (y / n) ?")

if have_fixed == "yes":
    #Get fixed costs
    fixed_expenses = get_expenses("fixed")
    fixed_frame = fixed_expenses[0]
    fixed_sub = fixed_expenses[1]         
else:
    fixed_sub = 0                   

#work out total costs and profit target
all_costs = variable_sub + fixed_sub
profit_target = profit_goal(all_costs)

#Calculates toal sales needed to reach goal
sales_needed = all_costs + profit_target

#Ask user for rounding 
round_to = num_check("Round to nearest...? $", "Can't be 0", int)

#Calculate recommended price
selling_price = sales_needed / how_many
print("Selling Price (unrounded: ${:.2f}".format(selling_price))

recommended_price = round_up(selling_price, round_to)

#Find Total Costs

#Ask user for profit goal

#Calculate recommended price

#Write data to file
#Change frames to strings
variable_txt = pandas.DataFrame.to_string(variable_frame)
fixed_txt = pandas.DataFrame.to_string(fixed_frame)

product_heading = "***** {} *****".format(product_name)
variable_costs_heading = "\n--- Variable Costs ---"

if have_fixed == "yes":
    fixed_costs_heading = "\n--- Fixed Costs ---"
else:
    fixed_costs_heading = ""

sales_advice_heading = "\n--- Sales Advice ---"

profit_target = "Profit Target: ${:.2f}".format(profit_target)
sales_needed = "Total Sales Needed: ${:.2f}".format(sales_needed)
recommended_price = "Recommended Price: ${:.2f}".format(recommended_price)

var_costs_subtotal = "\n Variable Costs Subtotal: ${:.2f}".format(variable_sub)

if have_fixed == "yes":
    fixed_costs_subtotal = "\n Fixed Costs Subtotal: ${:.2f}".format(fixed_sub)
else:
    fixed_costs_subtotal = ""

#list holding stuff to print / write to file 
to_write = [product_heading, variable_costs_heading, variable_txt, var_costs_subtotal, fixed_costs_heading, fixed_txt, fixed_costs_subtotal, sales_advice_heading, profit_target, sales_needed, recommended_price]

#Write to file...
#create file to hold data(add .txt extension)
file_name = "{}.txt".format(product_name)
text_file = open(file_name, "w+")

#heading
for item in to_write:
    text_file.write(item)
    text_file.write("\n\n")




#close file 
text_file.close()

#Print Stuff
for item in to_write:
    print(item)
    print()

#*** Printing Area ***

# print()
# print("*** Fund Raising  - {} ***".format(product_name))
# print()
# expense_print("Variable", variable_frame, variable_sub)

# if have_fixed == "yes":
#     expense_print("Fixed", fixed_frame[["Cost"]], fixed_sub) 

# print()
# print("*** Total Costs: ${: .2f} ***".format(all_costs))
# print()

# print()
# print("*** Profit and Sales Targets ***")
# print("Profit Target:${: .2f}".format(profit_target))
# print("Total Sales: ${: .2f}".format(all_costs + profit_target))

# print()
# print("*** Pricing ***")
# print("Minimum Price: {:.2f}".format(selling_price))
# print("Recommended Price: ${:.2f}".format(recommended_price))

