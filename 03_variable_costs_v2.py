from re import sub
import pandas


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

        quantity = num_check("Quantity:", "The amount must be a whole number more than zero", int)

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


#Get user data 
product_name = not_blank("Product name: ", "The product name cannot be blank")

#loop to get component, quantity and price 

variable_expenses = get_expenses("variable")
variable_frame = variable_expenses[0]
variable_sub = variable_expenses[1]

# *** Printing Area ***
print()

print(variable_frame)

print()

print("Variable costs: ${:.2f}".format(variable_sub))
