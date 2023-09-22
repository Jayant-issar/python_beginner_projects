logo = '''    __
               (_()  \        WELCOME TO THE AUTION !!!
          \__/  ||    \  \__/
          (oo)  /)       (oo)
         //~~\\//       //~~\\
         \\__/\/   _____\\__//_____
          |/\|    |                |
    _____ |||| ___|                |______
   ______(_)(_)___|________________|_______'''

print(logo)
bidders_data = []

def auction_mechanism():
    name = input("what is your name?\n")
    price = int(input("what is your bid?\n"))
    bidders_data.append({"name":name, "bid":price})

bidding_going_on = True

while bidding_going_on:
    auction_mechanism()
    yes_or_no = input("is there someone else too enter yes to give him chance to bid\n").lower()
    if yes_or_no == "yes":
        bidding_going_on
        #clear()
    else:
        bidding_going_on = False




for n in bidders_data:
   max_bid = 0
   nth = bidders_data.index(n)
   if int(bidders_data[nth]["bid"]) > max_bid:
       int(bidders_data[nth]["bid"]) == max_bid
   else:
       max_bid = max_bid
    








