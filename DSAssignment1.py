#Author - Brandon Redman 100797644
#Python sorting program


import time
import random

#class that defines attributes for each product
class productData():
    def __init__(self, ID,Name,Price,Cat):
        self.ID = int(ID)
        self.Name = Name
        self.Price = float(Price)
        self.Cat = Cat
    
    def __gettr__(self):
        return self.ID
    

 #function that updates the data based on the ID number provided   
def updateData(arr):
    
    try:

        ID = int(input("Enter the ID of the product to Update: "))
        #checks if ID already exists in the array and 
        #allows you to continue if it does exist
        for item in arr:
            if item.ID == ID:
                updatedID = int(input("Enter the updated ID: "))
                updatedName = input("Enter the updated Name: ")
                updatedPrice = float(input("Enter the updated Price: "))
                updatedCat = input("Enter the updated Category: ")
            else:
                print("ID does not exist...Choose different ID")
                break

    except:
        print("Make sure you have entered the correct information")

    #checks the array for the given id and updates its values
    for i in range (0, len(arr)-1):
        if arr[i].ID == ID:
            arr[i].ID = updatedID
            arr[i].Name = updatedName
            arr[i].Price = updatedPrice
            arr[i].Cat = updatedCat

#inserts a new product into the array
def insertData(arr):

    try:

        newID = int(input("Enter the new product ID: "))
        #checks if ID already exists in the array and 
        #allows you to continue if it does not exist
        for item in arr:
            if item.ID == newID:
                print("ID already exists...Choose different ID")
                break
            
        newName = input("Enter the new product Name: ")
        newPrice = float(input("Enter the new product Price: "))
        newCat = input("Enter the new product Category: ")
        arr.append(productData(newID, newName, newPrice, newCat))
    except:
        print("Make sure you have entered the correct information!")

#function that deletes a product in the array based on the ID provided    
def delData(arr):

    try:

        delID = int(input("Enter ID of the product you wish to delete: ")) 

    except:
        print("Make sure you have entered the correct information!")

    for i in range(0, len(arr)-1):
        if arr[i].ID == delID:
            del arr[i]

#Function that finds a product based on the ID that is provided
def searchData(arr):

    try:

        searchID = int(input("Enter ID of the product to search for: ")) 

    except:
        print("Make sure you have entered the correct information!")
    
    for item in arr:
        if item.ID == searchID:
            print(f'ID: {item.ID} | Name: {item.Name} | Price: {item.Price} | Category: {item.Cat}')
    
#Sorting algorithm
def insertionSort(arr):
    for item in range(1, len(arr)):
        key = arr[item]
        j = item - 1

        while j>=0 and key.Price < arr[j].Price:
            arr[j+1] = arr[j]
            j=j-1
        
        arr[j+1] = key

#function that loads the data from the text file
def loadData():
    file = open("product_data.txt", "r")
    while True:
        #splits each file line into 4 portions
        data = file.readline()
        formData = data.split(',')
        if not data:
            break
        
        #appends the array with the class object created from the split data
        dataArray.append(productData(formData[0], formData[1], formData[2], formData[3]))
    file.close()

i=1
dataArray = [] #initialize array
loadData() #loads the data

#main program loops options to choose from
while i>0:

    #input option to select
    optionSelect = input('Press 1 for Insert, 2 for Update, 3 for Delete, 4 for Search, 5 for Average Sort time, 6 for Worst Sort time, 7 for Best Sort time, 8 for print, x to exit: ')
    #options to select from
    if optionSelect == '1':
        insertData(dataArray)
    elif optionSelect == '2':
        updateData(dataArray)
    elif optionSelect == '3':
        delData(dataArray)
    elif optionSelect == '4':
        searchData(dataArray)
    elif optionSelect == '5':
        random.shuffle(dataArray) #shuffles list in case it is already sorted
        start = time.time()
        insertionSort(dataArray)
        end = time.time()
        print("Average time complexity: ", end-start) #prints time complexity
    elif optionSelect == '6':
        insertionSort(dataArray)
        dataArray.reverse()
        start = time.time()
        insertionSort(dataArray)
        end = time.time()
        print("Worst time complexity: ", end-start) #prints time complexity
    elif optionSelect == '7':
        insertionSort(dataArray)
        start = time.time()
        insertionSort(dataArray)
        end = time.time()
        print("Best time complexity: ", end-start) #prints time complexity
    elif optionSelect == '8':
        #prints current list
        for item in dataArray:
            print(f'ID: {item.ID} | Name: {item.Name} | Price: {item.Price} | Category: {item.Cat}')
    else:
        print("Exiting Program...")
        i=0

        
