



def swapFileData():
    fileName =  input("Enter the file name you want:- ")
    

fileName = open('Sample1.txt')
data = fileName.read()

fileName.close()

fileName2 =  input("Enter the file name you want to swap with:- ")
fileName2 = open('Sample2.txt')
data2 = fileName.read()

fileName2.close()

with open(fileName, 'w') as a:
    a.write(data2)


with open(fileName2, 'w') as a:
    a.write(data)


