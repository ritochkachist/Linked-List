class Node():  
  def __init__(self, data):
    self.data = data 
    self.next = None
 
  def __repr__(self):
    return repr(self.data)

class LinkedList():
  def __init__(self):
    self.head = None

  def __repr__(self):
    myList = []
    current = self.head
    while current != None:
      myList.append(current.data)
      current = current.next
    return str(myList)

  def addToHead(self, data):
    newNode = Node(data)
    newNode.next = self.head
    self.head = newNode
  
  def removeFromHead(self):
     if self.head == None:
      return "Empty List"
     else:
      value = self.head.data
      self.head = self.head.next
      return value

  def addToEnd(self, data):
    newNode = Node(data)
    if self.head == None:
      self.head = newNode
    else: 
      current = self.head
      while current.next != None:
        current = current.next
      current.next = newNode

  def removeFromEnd(self):
    current = self.head
    previous = self.head

    while current.next != None:
      previous = current
      current = current.next

    previous.next = None
    return current.data

  def isEmpty(self):
    if self.head == None:
      return "The list is empty"
    else:
      return "The list is not empty"

  def clear(self):
    self.head = None

  def contains(self, value):
    current = self.head
    while current != None:
      if current.data == value:
        return "The item is in the list"
      current = current.next
      
    return "The item is not in the list"
    
  def removeValue(self, value):
    inList = LinkedList.contains(self, value)
    if inList == False:
      return "The value is not in the list, so it cannot be removed"
    else:
      current = self.head
      previous = self.head
      while current.next != None and current.data != value:
        previous = current
        current = current.next
      previous.next = current.next
      return current.data
    

    
    
  
  