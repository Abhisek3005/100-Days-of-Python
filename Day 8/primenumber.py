def prime_number(value):
    is_prime=True
    for number in range(2,value):
        if value%number==0:
        
         is_prime=False
            
    if is_prime:
         print("its a prime number")
    else:
      print("its not a prime number")     
   
 #driver code       
value=int(input("enter a number \n"))
prime_number(value)

    








