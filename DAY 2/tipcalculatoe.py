print("Welcome to the tip calculator \n")
bill=(int(input(f"What was the total bill \n")))

per=(int(input("What percentage you like to give!10 , 12 ,15")))
          
cal=(per/100)*bill
person=(int(input(f"How many people split the bill \n")))
pay=bill+cal

each=pay/person
print(f"Each person should pay{each} ")