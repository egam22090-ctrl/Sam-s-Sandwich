import datetime

#This program runs a sandwich ordering service like 'Subway'
def bread_selection():
    bread_list = ["White", "Brown", "Italian", "Germany"]
    count=0
    print("We have the following breads:")
    while count < len(bread_list):
        print(count+1,"",bread_list[count])
        count+=1
    bread_selected=int(input("Which bread do you want? Enter a number: "))
    return bread_list[bread_selected-1]

def meat_selection():
    meat_list = ["None","Pork", "Turkey", "Chicken", "Meatballs"]
    count=0
    print("We have the following meats:")
    while count < len(meat_list):
        print(count+1,"",meat_list[count])
        count+=1
    meat_selected=int(input("Which bread do you want? Enter a number: "))
    return meat_list[meat_selected-1]

def cheese_selection():
    cheese_list = ["None","Old English", "Pale Triangle", "Mozzerela", "Cheddar"]
    count=0
    print("We have the following cheeses:")
    while count < len(cheese_list):
        print(count+1,"",cheese_list[count])
        count+=1
    cheese_selected=int(input("Which cheese do you want? Enter a number: "))
    return cheese_list[cheese_selected-1]

def salads_selection():
    salad_list = ["Lettuce", "Tomato", "Carrot", "Cucumber", "Onions"]
    count = 0
    print('We have the following veggies, select as many as you want')
    while count< len(salad_list):
        print(count, " ",salad_list[count])
        count+=1
    print("Press ENTER when you have finished choosing your salads")
    veg_added = "" #will hold a string of more than one time
    selected_salad= " " #prompts the user to enter a number in to a selected sald\ad

    while selected_salad != "" : #if enter is not pressed it will keep prompting you to select
        selected_salad = input(f"You have selected:{veg_added}\nWhat salad do you want? ")
        if selected_salad != "":
            selected_salad=int(selected_salad)
            #this variable keeps adding on each selected item from salad list
            veg_added=veg_added + " " + salad_list[selected_salad]
    return veg_added.strip() #removes empty space at start of the string





#main program
def output_textfile(first_name, cell_phone,sandwich_order):
    date_time=datetime.datetime.now()
    outFile=open("sams_sandwich.txt","a")
    print(f"\n***Order for {first_name} - {cell_phone}: ***")
    outFile.write(f"\nDate of booking: {date_time}")
    for item in sandwich_order:
        print(item)
        outFile.write(f"\n End of order: {date_time}")
        outFile.write("\n")
        outFile.write("\n")



print("Welcome to Sam's Sandwich Shop")
bread_choice=bread_selection()
print(f"Your selected  bread: {bread_choice}")
meat_choice=meat_selection()
print(f"Your selected meat was: {meat_choice}")
cheese_choice=cheese_selection()
print(f"Your selcted cheese was: {cheese_choice}")
salad_choice=salads_selection()
print(f"Your selected salads were: {salad_choice}")