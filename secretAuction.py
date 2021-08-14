
# from replit import clear

print("welcome to the secret auction program.")

bid_book = {}

bidding_finished = False


def highest_bidder(bid_record):
    highest_bid = 0
    winner = ""
    for person in bid_record:
        amount = int(bid_record[person])
        if amount > highest_bid:
            highest_bid = amount
            winner = person
    print(f"The winner is {winner} with a bid of ${highest_bid}.")


while not bidding_finished:
    bidder = input("What is your name? ")
    bid = input("How much do you want to bid? $")

    bid_book[bidder] = bid

    should_continue = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
    if should_continue == "no":
        bidding_finished = True
        highest_bidder(bid_book)
    elif should_continue == "yes":
        # clear()
        continue
    else:
        print("!!enter correct choice!!")
