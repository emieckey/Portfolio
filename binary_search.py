import csv
import string

# Open the CSV File and read it in.
f = open('countries.csv')
data = f.read()

# Split the data into an array of countries.
elementsList = data.split('\n')

# print length of the list
length = len(elementsList)
# print the first element
#print(elementsList[0])
# print the last elewjlkefat
print(elementsList[len(elementsList)-1])
# print all the elements
print(elementsList)

# Start your search algorithm here.
selectedCountry = input("What country from the list do you want: ")
beginningIndex = 0
endingIndex = len(elementsList)-1

Index = int((endingIndex+beginningIndex)/2)
while elementsList[Index] != selectedCountry:
    print(Index)
    if selectedCountry > elementsList[Index]:
        beginningIndex = Index
        # endingIndex = len(elementsList)-1
        Index = int((endingIndex+beginningIndex)/2)
    elif selectedCountry < elementsList[Index]:
        beginningIndex = beginningIndex
        endingIndex = Index
        Index = int((endingIndex+beginningIndex)/2)
    else:
        print(Index)
        break
print(Index)
