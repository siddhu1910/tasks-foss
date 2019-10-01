#code to read and search the key words from given file in google from CLI
file=input("enter file name: ")
#enter the name of file present in your directory
b=open(file,"r")
c=b.read()
d=c.split()
print(d)
#the key words got printed on your terminal
#now install googler from CLI by commands 1)sudo add-apt-repository ppa:twodopeshaggy/jarun and 2)sudo apt-get update && sudo apt-get install googler
#type googler on your terminal and press enter
#now enter your desired words from given text file in double quotes and press enter
#you can see the top results with index numbers...press the requiured index number to go the required page
#this may helps to check whether given file is copied from any websites 
