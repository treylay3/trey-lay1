#To-Do List

#Initialize
foodList=["Tacos", "Burger", "Curry", "Ramen", "Jerk Chicken", "Pasta"]
#Function
#Chores Intro: prints instructions on how to use chores List
def foodIntro():
    print("This is a list of your foods to try. Answer the questions to add foods mark completed ones and view your list and remove old foods youve eaten. You can also exit at any time.")

#Main


while True:
    action=str(input("What do you want to do? \n1=Add a food \n2=View food List \n3=Mark a food as Completed \n4=Remove a food \n5=quit \n6=clear list \n7=sort list by alphabet "))
    if action=="1":
        foodList.append(input("What food do you want to add?"))
    elif action=="2":
        print(foodList)
    elif action=="3":
        food=input("What food did you complete?")
        i=foodList.index(food)
        foodList[i]=food+" X"
    elif action=="4":
        foodremoved=input("What food do you want to remove?")
        foodList.remove(foodremoved)
    elif action=="5":
        break
    elif action=="6":
        foodList.clear()
    elif action=="7":
        foodList.sort()
    
    
