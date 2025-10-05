#This program runs a sandwich ordering service like 'Subway'
def bread_selection():
    bread_list = ["White", "Brown", "Italian", "Germany"]
    count=0
    print("We have the following breads:")
    while count < len(bread_list):
        print(count+1,"",bread_list[count])
        count+=1
    bread_selected=int(input("WHich bread do you want? Enter a number: "))
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


#main program
print("Welcome to Sam's Sandwich Shop")
bread_choice=bread_selection()
print(f"Your selected  bread: {bread_choice}")
meat_choice=meat_selection()
print(f"Your selected meat was: {meat_choice}")
cheese_choice=cheese_selection()
print(f"Your selcted cheese was: {cheese_choice}")