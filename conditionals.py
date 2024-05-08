#working with the if statement
userReply = input("Do you need to ship a package? (Enter yes or no) ")
if userReply == "yes":
    print("We can help you ship that package!")

#else statement
else:
    print("Please come back when you need to ship a package. Thank you.")

#working with the elif statement
userReply = input("Would you like to buy stamps, buy an envelope, or make a copy? (Enter stamps, envelope, or copy) ")
if userReply == "stamps":
    print("We have many stamp designs to choose from.")
elif userReply == "envelope":
    print("We have many envelope sizes to choose from.")
elif userReply == "copy":
    copies = input("How many copies would you like? (Enter a number) ")
    print("Here are {} copies.".format(copies))
else:
    print("Thank you, please come again.")

