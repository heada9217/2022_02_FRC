# import libraries
import pandas

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
            elif response == var_item:
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


# *** Main Routine goes here *** 
#Get user data 
product_name = not_blank("Product name: ", "The product name cannot be blank")

#Get varuabke costs
variable_expenses = get_expenses("variable")
variable_frame = variable_expenses[0]
variable_sub = variable_expenses[1]

#Get fixed costs
fixed_expenses = get_expenses("fixed")
fixed_frame = fixed_expenses[0]
fixed_sub = fixed_expenses[1]

#Find Total Costs

#Ask user for profit goal

#Calculate recommended price

#Write data to file

#*** Printing Area ***

print(" **** Variable Costs ****")
print(variable_frame)
print()

print("Variable Costs: ${:.2f}".format (variable_sub))

print("*** Fixed Costs ***")
print(fixed_frame[['Cost']])
print()
print("Fixed Costs: ${: .2f}".format (fixed_sub))


