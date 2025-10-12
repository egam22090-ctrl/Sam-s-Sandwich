import datetime

def force_number(message,lower,upper):
    while True:
        try:
            number =int(input(message))
            if number>=lower and number<=upper:
                break
            else:
                print(f"Please enter a number between {lower} - {upper}")
        except:
            print("Error- only type numbers please")
    return number

def force_name(message,lower,upper):
    while True: #This is an infinte loop
        name=str(input(message)).title() #Askimg for and storing the users name and adding a capital letter
        if len(name)>=lower and len(name)<=upper and name.isalpha():#Providing paramters for the length of the users name and ensuring it's alphabetical
            break  #the loop is broken if the condiition above is met
        else:
            print("Invalid name")#Sends the user an error message
    return name #returns a valid name back to the variable

def force_cellphone_number(message,lower,upper):
    while True:
        cellphone = str(input(message).strip())
        if len(cellphone)>= lower and len(cellphone) <= upper and cellphone.isnumeric():
            break
        else:
            print(f"Please enter a number between {lower} and {upper} digits")

#This program runs a sandwich ordering service like 'Subway'
def bread_selection():
    bread_list = ["White", "Brown", "Italian", "Germany"]
    count=0
    print("We have the following breads:")
    while count < len(bread_list):
        print(count+1,"",bread_list[count])
        count+=1
    bread_selected=force_number("Which bread do you want? Enter a number: ",1,len(bread_list))
    return bread_list[bread_selected-1]

def meat_selection():
    meat_list = ["None","Pork", "Turkey", "Chicken", "Meatballs"]
    count=0
    print("We have the following meats:")
    while count < len(meat_list):
        print(count+1,"",meat_list[count])
        count+=1
    meat_selected=force_number("Which meat do you want? Enter a number: ",1,len(meat_list))
    return meat_list[meat_selected-1]

def cheese_selection():
    cheese_list = ["None","Old English", "Pale Triangle", "Mozzerela", "Cheddar"]
    count=0
    print("We have the following cheeses:")
    while count < len(cheese_list):
        print(count+1,"",cheese_list[count])
        count+=1
    cheese_selected=force_number("Which cheese do you want? Enter a number: ",1,len(cheese_list))
    return cheese_list[cheese_selected-1]

def salads_selection():
    salad_list = ["Lettuce", "Tomato", "Carrot", "Cucumber", "Onions", "No Salads/Exit"]
    salad_choice=[] #empty list to hold the selected salads
    while True:
        sep= " , "
        salad_options=int(input(f"We have the following veggies, select as many as you want. {sep.join(salad_list)} \n Your choice: "))
        salad_choice.append(salad_list[salad_options-1]) #adding the selected salad to the empty list
        print(f"Your selected salds are {salad_choice}")
        if salad_options==salad_list[-1]:
            break
    return ",".join(salad_choice) #returns a string formatting the options


#main program
def output_textfile(first_name, cell_phone,sandwich_order):
    date_time=datetime.datetime.now()
    outFile=open("sams_sandwich.txt","a")
    print(f"\n***Order for {first_name} - {cell_phone}: ***")
    outFile.write(f"\nDate of booking: {date_time}")
    for item in sandwich_order:
        print(item)
        outFile.write(f"\n End of order: {date_time}") 
    print(f"***End of order : {date_time} ***\n")
    outFile.write("\n")
    outFile.write("\n")
    outFile.close()

first_name=force_name("What is your first name: ",2,15)
cell_phone=force_cellphone_number("What is your cellphone number: ",2,10)
bread_choice=bread_selection()
meat_choice=meat_selection()
cheese_choice=cheese_selection()
salad_choice=salads_selection()
sandwich_order=[]
sandwich_order.append(first_name)
sandwich_order.append(cell_phone)
sandwich_order.append(f"Bread: {bread_choice}")
sandwich_order.append(f"Meat: {meat_choice}")
sandwich_order.append(f"Cheese: {cheese_choice}")
sandwich_order.append(f"Salads:{salad_choice}")
output_textfile(first_name,cell_phone,sandwich_order) 

print("Welcome to Sam's Sandwich Shop")
bread_choice=bread_selection()
print(f"Your selected  bread: {bread_choice}")
meat_choice=meat_selection()
print(f"Your selected meat was: {meat_choice}")
cheese_choice=cheese_selection()
print(f"Your selcted cheese was: {cheese_choice}")
salad_choice=salads_selection()
print(f"Your selected salads were: {salad_choice}")