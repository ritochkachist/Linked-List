# Margarita Chistiakova
# 4/3/2023
# Linked List Final

from LinkedList import LinkedList

myList = LinkedList()
print("Welcome to shopping list creation tool!\n")

choice = 0
while choice !=8:
  
  print("""Please choose one option from the menu below: 
  1. Add an item to the beginning of the shopping list
  2. Add an item to the end of a shopping list
  3. Remove an item from the beginning of the shopping list
  4. Remove an item from the end of the shopping list
  5. Check if the shopping list is empty
  6. Check if the shopping list contains a specific item
  7. Print the shoppping list
  8. Quit""")
  
  choice = int(input(" > "))
  
  if choice == 1:
    addtohead = input("Please enter the item that you want to place at the beginning of the shopping list: ")
    myList.addToHead(addtohead)
    print(f"The list with the added item: {myList}")
    
  elif choice == 2:
    addtoend = input("Please enter the item that you want to place at the end of the shopping list: ")
    myList.addToEnd(addtoend)
    print(f"The list with the added item: {myList}")
    
  elif choice == 3:
    myList.removeFromHead() 
    print(f"The list after the removal of the chosen item: {myList}")

  elif choice == 4:
    myList.removeFromEnd()
    print(f"The list after removal of the chosen item: {myList}")

  elif choice == 5:
    print(myList.isEmpty())
    
  elif choice == 6:
    containsitem = input("Please enter the item that you want to check if it is in the shopping list: ")
    print(myList.contains(containsitem))

  elif choice == 7:
    print(myList)

  elif choice == 8:
    print("Thank you for testing my program! Have a good day!")
    
  else:
    print("Error... Please restart the program.")
    
    
  


