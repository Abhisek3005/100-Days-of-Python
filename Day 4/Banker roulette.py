import random
people_name=input("Give me Everbody's names,separated by comma\n" )
Separate=people_name.split(",") #it will put every name to  a list
print(Separate)
payer=random.randint(0,len(Separate)-1)
x=Separate[payer] # It will add the index number to the real value
print(x,"is going to buy the meal today")

#Exceptional
x=random.choice(Separate) # It will also print the output same as the above code
