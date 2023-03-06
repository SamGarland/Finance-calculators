# This programme (1) deinfes the function calculator, in which the user can: make a calculation or
# read equations from a file, (2) calls the function.

#(1)
#---- Calculator ----#
def calculator():
    
    # Initiates option menu loop.
    
    while True:
        
        choice = input("""What would you like to do?
c - make a calculation
re - read equations for file
e - exit 
:""")
        choice = choice.lower().strip()
        
        # decides if user choice is valid. If not requests repeated attempt. 
    
        if choice != "c" and choice != "e" and choice != "re":
            print(f"You entered {choice}. That's not right! Try again...\n")
        
        else:  
                
                # If "c", asks user for 2 numbers and operator.
                # Performs calculation and writes to file "calculations.txt"
                # Guards against invalid numbers and operations.
                
                if choice == "c": 
                    
                        try:
                            while True:
                                num_1 = int(input("Please enter a number: "))
                                num_2 = int(input("Please enter a second number: ")) 
                                
                                op = input("""Enter the operation you would like to perfom?
add - "+"
subtract - "-"
multiply - "x"
divide - "/"
power - "p"
main menu - "e"
: """)
                                op.lower().strip()
                                
                                if op == "e":
                                    break
                                elif op != ("+") and op != ("-") and op != ("x") and op != ("/") and op != ("p"):
                                    print(f"You entered {op}. This is not one of the operations available. Try again.")
                                else:
                                
                                    calc = 0
                                    
                                    if op == "+":
                                        calc = num_1 + num_2
                                    elif op == "-":
                                        calc = num_1 - num_2
                                    elif op == "*":
                                        calc = num_1 * num_2
                                    elif op == "/":
                                        calc = num_1 / num_2
                                    elif op == "p":
                                        calc = num_1 ** num_2
                                    
                                    print(f"Your calculation of {num_1} {op} {num_2} is {float(calc)}")
                                
                                    with open("calculations.txt", "a+") as file:
                                        file.write(f"Your calculation of {num_1} {op} {num_2} is {float(calc)}\n")
                                    
                                    file.close()
                            
                        except ValueError:
                            print("Sorry, that's not a valid number... Please try again.")
                            
                elif choice == "re":
                    
                    # if "re" is selected:
                    # This request the user for a file and opens and reads the calculations line by line from it. 
                    # It guards against the file not existing. And allows the user multiple attempts.
                    
                    while True:
                        
                        new_file = None
                        
                        new_file = input("""Enter the name of the file you want to open (or "e" to main menu):""")
                        
                        if new_file == "e":
                                break
                        else:
                            try:
                                
                                with open(new_file, "r") as new_file:
                                    
                                    lines = new_file.readlines()
                                    
                                    for line in lines:
                                        print(f"\n{line}")
                                        
                            except FileNotFoundError as error:
                                
                                print("\nSorry, that file doesn't exist...\n")
                                
                            finally:
                                if new_file is not None:
                                    try:
                                        new_file.close()
                                    except AttributeError:
                                        continue
                                
                elif choice == "e":
                    
                    # This exits the programme.
                    
                    try:
                        new_file.close()
                        print("Goodbye!")
                        break
                    except UnboundLocalError:
                        print("Goodbye!")
                        break

# (2) Fuction call
calculator()
