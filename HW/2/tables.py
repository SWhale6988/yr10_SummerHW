repeat = True 

while repeat == True: #Makes sure the loop repeats
    table = input("Choose a times table") #Gets user input

    try: #Tests if the input is a string or not
        table = int(table)
    except ValueError: #If the try statement brings up an error
        print("Invalid choice")#Outputs invalid choice. Repeats as 'repeat' doesn't change
    else:
        repeat = False
        table = int(table) #Converts table into an interger
        for x in range(12): #Repeats 12 times
            #Outputs tables
            print(str(x+1) + " x " + str(table) + " = " + str(x+1*table))
            
