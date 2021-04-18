"""My Integration Program based on fishing"""

__author__ = "Benjamin Castro"

"""I wanted to create a program that gives out the regulations, information and tips for catching fish.
 The program would go step by step with the user slowly preparing the user to go fishing. I decided to base
 my project on fishing because it is my passion.Pycharm detects many gramatical errors but in reality those are just names."""


# The information for the fish was taken from: myfwc.com/fishing/saltwater/recreational/
class Admin:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.add = first + " " + last

    def name(self):
        return '{} {}'.format(self.first, self.last)


class Contact(Admin):
    def __init__(self, first, last, email):
        super().__init__(first, last)
        self.email = email


class Professor:
    def introduction(self):
        print('Hello professor welcome to my integration project!')


class Benjamin:
    def introduction(self):
        print("Hello Benjamin welcome to your project!")


def fish():
    print("hello")


def main():
    """

    """
    fish()
    admin1 = Contact('Benjamin', 'Castro', 'benjamincastro2002@gmail.com')
    admin2 = Contact('Professor', 'Vanselow', 'Contact not available')

    print(admin1.add)
    print(admin1.email)
    print(admin2.add)
    print(admin2.email)

    professor_vanselow = admin2
    benjamin = admin1

    user_question = input("Who is using the app? ")
    if user_question == "Professor Vanselow":
        print(professor_vanselow)
    elif user_question == "Benjamin":
        print(benjamin)
    else:
        print("Welcome to my integration project")

    """In the lines of code above I inherited information from my first class to my second class.
    I did this in order to give the user information on professor Vanselow and me. I used the youtube channel Bitfumes
     to help me create this code. I also got help from professor Vansellow."""

    program_on = True
    if program_on:
        print("Welcome to SWFl inshore species fishing information program!")
        print("With this program you will get  fishing tips, fish regulations and much more!")

    login_info = False
    while not login_info:
        login = input("Enter your  Login ")
        password = input("Enter your password ")
        if login == "Bencastro2002" and password == "Castro2002":
            print("You have been signed in successfully into the app. ")
            login_info = True
        else:
            print("The wrong information has been printed, please try again.")
    """This line of code is created in order to log into the program."""

    pb = int(input("How long was your personal best fish in inches? "))

    print("While fishing in the state of Florida a fishing license is required")

    license_question = input("Do you have a fishing license? ")
    if license_question == "yes":
        print("Great we can move onto the next step!")
    elif license_question == "no":
        fishing_license_price = int(15)
        while True:
            try:
                payment = int(input("Your fishing license is going to cost 15 dollars, how much are you "
                                    "going to pay?"))

                break
            except ValueError:
                print("Error must be a number.")
        difference = payment - fishing_license_price
        if difference < 0:
            print("amount due ${:,.2f}".format(-difference))
        print("Thank you, you will be getting back ${:,.2f}".format(difference))
    else:
        print("Please print valid answer. ")
    """I use if and elif statements in order to s if the user has a license. If the user does not have
     a license it then gives them the opportunity buy one. I used hackerrank and based the way I
     find the difference."""

    print("Now that you have your licence we can discuss your fishing destination.")

    destination_question = input("Where do you plan to fish? ")
    if destination_question == "Cape Coral":
        print(" Cape Coral is a great place to fish. It is the city with the most canals in the world!")
        print("With many of them being brackish water. Snook, Tarpon , and jacks are  common species caught! ")
        print("We recommend that you fish the Cape Coral Yacht Club as their are always large Snook swimming by.")
    elif destination_question == "Naples":
        print("Naples is an awesome place to go fishing at! The Naples pier is a can't miss fishing spot.")
        print("We recommend to try the Naples pier during the summer.")
        print("Monster size Snook and Redfish that like to roam the beach during summer!")
    elif destination_question == "Pine Island":
        print("If you are looking to catch jack this is the perfect destination.")
        print("The brackish water makes a perfect home for theses fish.")
        print("Be ready for a strong fight, they are called canal tuna for a reason!!")
    elif destination_question == "Sanibel":
        print("When fishing at Sanibel you never know what you are going to get. It is an extraordinary place to fish.")
        print("At this location you have the possibility to catch any of the inshore species located in Florida!")
        print("Many people come to Sanibel to target the Goliath Grouper. This fish can grow up to 600 pounds!")
        print("They will be found by structure and a strong leader is recommended.")
    elif destination_question == "Boca Grande":
        print("Boca Grande is the tarpon capital of the world. During the summer you can see the tarpon rolling! ")
        print("From artificial to live bait you are bound to hook a fish. We recommend Gasparilla State Park.")
        print("There is a deep inlet here, perfect for catching big tarpon!")
    elif destination_question == "Captiva":
        print("If you wanna catch snook you have come to the right place! Yo have to go to blind pass ")
        print("Where you are guaranteed to catch a snook. We have found that live bait works the best.")
    elif destination_question == "Port Charlotte":
        print("Port Charlotte is the perfect location to target red and black drum.")
        print("We recommend you to try Port Charlotte pier. Just drop your line straight down and expect a hookup.")
        print("We recommend you to use crab or live shrimp for bait.")
    elif destination_question == "Punta Gorda":
        print("Punta gorda is a great location to catch spotted trout.")
        print("They will hit artificial and live bait.")
    else:
        print("Sorry at this time we don not have this location in our database.")
    """These lines of code where to inform th user on what location they are fishing at. It would give them tips 
    and tricks to catch fish. I used personal information and information on myfwc.com"""
    print(" Now that we know where you are going to fish we need to select the correct equipment.")
    print(" Having the correct gear is crucial when targeting fish.")

    fish_size_question = input("What size fish do you plan to target? ")
    if fish_size_question == "small":
        print("When targeting smaller size fish we recommend you use a 1000 to 3500 size reels")
        print("These are the perfect size reel size to handle small size fish")
        print("You can still enjoy a good fight with these sizes of reels.")
        print("For the rod we recommend an 7'6 medium fast action rod. You could also go for a smaller size.")
        print("This size rod is perfect for throwing small artificial and live bait.")
        print("For the line we recommend 15 pound braid. You dont wanna be using this set up for any fish larger.")
        print("You want about 175 yard of braid for your reel. You also want a 25 pound leader for this setup.")
        print("The leader should be around 3 feet long.")
    elif fish_size_question == "medium":
        print("When targeting medium size fish we recommend you use a 4000 to 5000 size reels")
        print("These are the perfect size reel size as handle medium size fish well.")
        print("For the rod we recommend an 7'6 medium heavy fast action rod.")
        print("This size rod is perfect for throwing  medium size artificial and live bait.")
        print("For the line we recommend 30 pound braid. ")
        print("You want about 175 yard of braid for your reel. You also want a 40 pound leader for this setup.")
        print("The leader should be 3 feet long.")
    elif fish_size_question == "large":
        print("When targeting large size fish we recommend you use a 6000 to 8000 size reels")
        print("These are the perfect  reel size to handle large fish.")
        print("For the rod we recommend an 7'6 medium heavy rod.")
        print("This size rod is perfect for throwing large size artificial and live bait.")
        print("For the line we recommend 40 pound braid. ")
        print("You want about 175 yard of braid for your reel. You also want a 60 pound leader for this setup.")
        print("The leader should be 3 feet long.")
    print("We recommend you using Penn and Florida Product brand reels.")
    """These lines of code where meant to inform the reader on what gear they should use.
    This was based n their response."""

    print("Penn and Florida products make great reels lets compare the drag to see which is better.")

    class Reel():
        favorites = []

        def __init__(self, brand, drag):
            self.drag = drag
            self.brand = brand

        def is_resistence(self):
            if self.drag > 100:
                return True
            return False

        def __str__(self):
            return f"{self.brand} is {self.drag} of drag resistance"

    penn = Reel("Penn battle 2", 30)
    fp = Reel("FP Osprey ", 30)
    print(penn == fp)
    """This line of code was meant to show that they had differend brands but they still had
    the same drag force. This wold make them the same."""

    print("Now that we have right gear for you, we need to decide on your bait.")
    print("When fishing inshore we can Use both live bait and artificial.")

    a_q = input("Are you going to be to be using artificial baits?  ")
    if a_q == "no":
        print("Sounds good lets move on to live bait then.")
    elif a_q == "yes":
        print("Awesome using artificial lures allows you to cover tons of area when fishing.")
        print("we recommend that you use gulp or zman lure when fishing. They have shown to catch tons of fish")
    while True:
        try:
            a_q = input("Are you going to be to be using artificial baits?  ")
            break
        except ValueError:
            print("Error, please respond yes or no")


    lure_question = input("Will you be using gulp or zman? ")
    if lure_question == "gulp":
        print("Gulp is a great artificial bait to throw. We recommend pairing it with a 1/2 ounce jig head")
        print("Any fish will strike this lure as it is scented to attract fish. ")
    elif lure_question == "zman":
        print("zman is an excellent choice. Snook absolutely demolish theses baits")
        print("We recommend pairing zmans with a 1 ounce jig head.")
    elif lure_question == "both":
        print("Gulp is a great artificial bait to throw. We recommend pairing it with a 1/2 ounce jig head")
        print("Any fish will strike this lure as it is scented to attract fish. ")
        print("zman is an excellent choice. Snook absolutely demolish theses baits")
        print("We recommend pairing zmans with a 1 ounce jig head.")
    elif "zman""gulp" not in lure_question:
        print("Sorry but at this time information on this lure is not available.")

    print("With our program you are able to buy both zman and gulp artificial baits.")

    zman_question = input("Would you like to buy zman artificial baits today? ")
    if zman_question == "yes":
        if __name__ == '__main__':
            zman_price = int(5)
        zman_amount = float(input("How many packets of zman do you want to buy?: "))
        total_cost_for_zman = zman_price * zman_amount
        print("Your total cos will be ", format(total_cost_for_zman, "0.2f"), sep='$')
    elif zman_question == "no":
        print("That is alright, thank you for your time!")

    gulp_question = input("Would you like to buy gulp artificial baits today? ")
    if gulp_question == "yes":
        if __name__ == '__main__':
            gulp_price = int(6)
        gulp_amount = float(input("How many packets of gulp do you want to buy?: "))
        total_cost_for_gulp = gulp_price * gulp_amount
        print("Your total cost will be ", format(total_cost_for_gulp, "0.2f"), sep='$')
    elif gulp_question == "no":
        print("That is alright, thank you for your time!")

    print("With our program we give the opportunity to win free gulp packs")
    free_gulp = input("Would you like to try to win free gulp packs? ")
    if free_gulp == "yes":
        import random
        gulp_chance = random.randint(0, 10)
        print("Congratulations you won:", gulp_chance)

    print("With artificial baits you can use them many times but they only last so many times.")

    lure_question2 = input("Enter lure name to know how many fish you can catch per lure. ")
    if lure_question2 == "zman":
        zman_lure = int(input("How many zmans do you have? "))
        print(zman_lure ** 2)
    elif lure_question2 == "gulp":
        gulp_lure = int(input("How many gulp lures do you have? "))
        print(gulp_lure ** 2)
    else:
        print("We do not have information about this lure at this time")

    print("Now its time to talk about actual bait such as live and cut bait.")
    print("We will start off with live bait")

    lv_bait = input("Will you be you be using live bait today? ")
    if lv_bait == "yes":
        type_lv_bait = input("What type of live bait will you be using? ")
        if type_lv_bait == "shrimp":
            print("Live shrimp is an excellent choice as everything eats shrimp.")
            print("With this bait you will have the best chance to catch a fish.")
        elif type_lv_bait == "bait fish":
            print("Bait fish is an excellent choice to catch bigger fish. we recommend you try using Mullet,Pin fish ")
            print("and Greenbacks as your main bait fish.")
        elif type_lv_bait == "crab":
            print("Crabs are an excellent choice when targeting fish such as Reddrum, Blackdrum, and Sheepshead.")
            print("These type of fish eat crustaceans and crabs are there favorite bait")
    elif lv_bait == "no":
        print("Ok no worries good luck with artificial. ")
    """Through if and elif statements I was able to take information from the user and give them
    tips and information"""

    print("Some times when you dont have live bait fish, you cut it into chunks.")
    chunks_of_bait = input("How many fish have you used for bait? ")
    print(int(float(chunks_of_bait) // 1))
    print("This is how many whole fish you have used.")

    print("Well now its time to have fun and go fishing")
    print("When you catch some fish come back for more information.")

    harvesting_question = input("Do you want to check and see if any of the fish you caught are legal? ")
    if harvesting_question == "yes":
        fish_question = input("What species of fish that you have caught would you like to know if it is legal ?")
        if fish_question == "Mangrove":
            mangrove_snapper = int(input("Enter length of Mangrove Snapper "))
            daily_limit_of_mangrove_snapper = input("Enter amount of Mangrove Snapper caught ")
            print(mangrove_snapper >= 10) and (daily_limit_of_mangrove_snapper >= 5)
        elif fish_question == "Lane":
            lane_snapper = int(input("Enter length of Lane Snapper "))
            daily_limit_of_lane_snapper = input("Enter amount of Lane Snapper caught ")
            print(lane_snapper >= 8) and (daily_limit_of_lane_snapper >= 5)
        elif fish_question == "Mutton":
            mutton_snapper = int(input("Enter length of mutton Snapper "))
            daily_limit_of_mutton_snapper = input("Enter amount of Mutton Snapper caught ")
            print(mutton_snapper >= 18) and (daily_limit_of_mutton_snapper >= 5)
        elif fish_question == "Cuberra":
            cuberra_snapper = int(input("Enter length of Cuberra Snapper "))
            daily_limit_of_cuberra_snapper = input("Enter amount of Cuberra Snapper caught ")
            print(cuberra_snapper >= 12) and (daily_limit_of_cuberra_snapper >= 5)
        elif fish_question == "Black drum":
            black_drum = int(input("Enter length of black drum  "))
            daily_limit_of_black_drum = input("Enter amount of Black drum caught ")
            print(24 >= black_drum >= 15) and (daily_limit_of_black_drum >= 5)
        elif fish_question == "Red drum":
            red_drum = int(input("Red Drum Not allowed to harvest due to red tide.  "))
            print(red_drum)
        elif fish_question == "Spotted trout":
            spotted_trout = int(input(" Spotted Trout not in season due to red tide. "))
            print(spotted_trout)
        elif fish_question == "Snook":
            snook = int(input(" Snook is not in season due to red tide. "))
            print(snook)
        elif fish_question == "Tarpon":
            tarpon = int(input("Only one tarpon can be harvested per year with the purchase of a 50$ tag."))
            print(tarpon)
        elif fish_question == "Goliath grouper":
            goliath_grouper = int(input("Goliath Grouper are endangered species. Harvesting is prohibited!"))
            print(goliath_grouper)
        elif fish_question == "Mullet":
            mullet = int(input("up to a 100 pounds of mullet can be harvested."))
            print(mullet)
        elif fish_question == "Jack":
            jack = int(input("up to a 100 pounds of jack can be harvested."))
            print(jack)
        elif fish_question == "Gag grouper":
            gag_grouper = int(input("Enter length of Gag grouper  "))
            daily_limit_of_gag_grouper = input("Enter amount of black grouper caught")
            print(gag_grouper >= 24) and (daily_limit_of_gag_grouper <= 2)
        elif fish_question == "Flounder":
            flounder = int(input("Enter length of flounder  "))
            daily_limit_of_flounder = input("Enter amount of flounder")
            print(flounder >= 12) and (daily_limit_of_flounder <= 10)
        else:
            print('Sorry at this time we d not have information on this specie.')
    elif harvesting_question == "no":
        print("That is ok, nothing wrong with catch and release.")
    """Through information obtained from the user i was able to see if the fish they caught were legal.
    I used information from myfwc.com to get the fish regulations."""

    print("Wow you did a great job today! Now lets see your average length of fish!")

    total_length = 0
    amount_of_fish_caught = int(input("How many fish did you catch? "))
    for x in range(amount_of_fish_caught):
        length_of_fish = int(input("How long is the fish?"))
        total_length += length_of_fish
    print(total_length / amount_of_fish_caught)

    print("Fishing is fun  with friends. But it can be a drag when theres more then 3 friends.")
    friend_question = input("Will there be a total of three people fishing? ")
    if friend_question == "yes":
        print("awesome we will now record you and your friends information.")
        for X in range(3):
            name = input("Enter your name ")
            total = 0
            for Y in range(3):
                size_of_fish_caught = int(input("Whats the size of your fish?"))
                total += size_of_fish_caught
                average = total / 3
            print("Name:", name)
            print("Average:", format(average, "0.2f"))
        "I got the information from three friends and found the average."

    print("As fishermen our personal best fish is very important and we are always trying to beat our pb!")

    biggest_fish_td = int(input("What as the biggest fish caught today? "))
    if pb > biggest_fish_td:
        print(" you sadly did not beat your pb today.")
    elif pb < biggest_fish_td:
        print("congratulations you have a new personal best today!")

    print("Thank you for using our program hopefully we gave the information for you to suceed catching fish!")


if __name__ == "__main__":
    main()
