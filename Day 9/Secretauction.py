import os

def clear():
    """Clears the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

# Example usage:
print("This is some output.")
#clear()  # This will clear the console screen.



from art import logo
print(logo)
bids={}
biding_finished =False
def find_highest_bidder(bidding_records):
    highest_bid = 0
    for bidder in bidding_records:
       bid_amount= int(bidding_records[bidder])
       if bid_amount > highest_bid:
           highest_bid = bid_amount
           winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")
while not biding_finished:
    name=input("What is your name : \n")
    price = int(input("What is your bid? $ \n"))
    bids[name]= price
    should_continue = input("Are ther any other bidders? Type 'yes' or 'no'. ")
    if should_continue == "no":
         biding_finished = True
         find_highest_bidder(bids)
    elif should_continue == "yes":
     clear()    

