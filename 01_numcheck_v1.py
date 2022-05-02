#Main routine goes here


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


get_int = num_check("how many?: ", 'Please enter a whole number larger than zero.', int)

get_cost = num_check("How much does it cost?: $", "Please enter a whole number larger than zero.", float)

print("You need: {} /n It costs: ${}".format(get_int,get_cost))
