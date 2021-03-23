# Benjamin K Casto

# I wanted to create a program that gives out the regulations,tips for cathcing the fish and any aditional information for anglers located  in the inshore areas of SWFl.
# The user would insert the name of the a certain fish , then thy would be asked what they would like to know.
# The user could then awnser by asking for season, regulations,tips,area, or info.

# The information for the fish was taken from: myfwc.com/fishing/saltwater/recreatonal/

program_on = True
if  program_on:
    print("Welcome to SWFl inshore species fishing information program!")

login = input("Enter your  Login.")
password = input("Enter your password.")
if login == "Bencastro2002" and password == "Castro2002":
    print("you have been signed in successfully into the app ")
else:
    print("The wrong information has been printed, please try again.")


fishing_license_price = int(15)
payment = int(input("your fishing license is 15 dollars, how much are you paying?"))
difference = payment - fishing_license_price
if difference < 0:
    print("amount due ${:,.2f}". format(-difference))

else:
    print("thank you, you will be getting back ${:,.2f}".format(difference))

#age = input("How old are you?")
#registered = input("Do you have fishing license?(yes,no)")
#if age < 16 or registered =='yes':
#    print("allowed to fish")
#else:
#    print("Requires license")

# not sure why it does not want to run

chunks_of_bait = input("how many fish have you used for bait? ")
print(int(float(chunks_of_bait) // 1))

lures = ["gulp","zman"]
lure_name = input("Enter lure name")
if not "lure_name" in lures:
    print("At this time we dont have information on this lure")

lure_question = input("Enter lure name to know how many fish you can catch per lure (zman,gulp)")
if lure_question == "zman":
    zman_lure = int(input("How many zmans do you have? "))
    print(zman_lure**2)
elif lure_question == "gulp":
    gulp_lure = int(input("How many gulp lures do you have? "))
    print(gulp_lure**2)

import math
import os
import random
import sys
import re
if __name__ == '__main__':
    zman_price = int(5)
zman_amount = float(input("How many packets of zman do you want to buy?: "))
total_cost_for_zman = zman_price * zman_amount
print("total_cost_for_zman: ", format(total_cost_for_zman, "0.2f"), sep='$')




if __name__ == '__main__':
    gulp_price = int(6)
gulp_amount = float(input("How many packets of gulp do you want to buy?: "))
total_cost_for_gulp = gulp_price * gulp_amount
print("total_cost_for_gulp: ", format(total_cost_for_gulp, "0.2f"), sep='$')

total_weight_of_fish_for_the_day = float(input("Enter weight of all the fish you harvested today"))
print(total_weight_of_fish_for_the_day <= 10)

#mangroves_kept = True
#legal_mangroves_kept = int(input("How many mangrove snapper did you harvest ?"))
#if legal_mangroves_kept > 10:
        #mangroves_kept = False
#print(legal_mangroves_kept)

fish_question = input("what species of fish that you have caught would you like to know if it is legal ?(mangrove,lane,mutton,cuberra,black drum,red drum, spotted trout,jack,mullet,goliath grouper,gag grouper,snook,flounder,tarpon)")
if fish_question == "mutton":
    mangrove_snapper = int(input("Enter length of Mangrove Snapper "))
    daily_limit_of_mangrove_snapper = input("Enter amount of Mangrove Snapper caught")
    print(mangrove_snapper >= 10) and ((daily_limit_of_mangrove_snapper >= 5))
elif fish_question == "lane":
    lane_snapper = int(input("Enter length of Lane Snapper "))
    daily_limit_of_lane_snapper = input("Enter amount of Lane Snapper caught")
    print(lane_snapper >= 8) and ((daily_limit_of_lane_snapper >= 5))
elif fish_question == "mutton":
    mutton_snapper = int(input("Enter length of mutton Snapper "))
    daily_limit_of_mutton_snapper = input("Enter amount of Mutton Snapper caught")
    print(mutton_snapper >= 18) and ((daily_limit_of_mutton_snapper >= 5))
elif fish_question == "cuberra":
    cuberra_snapper = int(input("Enter length of Cubera Snapper "))
    daily_limit_of_cuberra_snapper = input("Enter amount of Cuberra Snapper caught")
    print(cuberra_snapper >= 12) and ((daily_limit_of_cuberra_snapper >= 5))
elif fish_question == "black drum":
    black_drum = int(input("Enter length of black drum  "))
    daily_limit_of_black_drum = input("Enter amount of black drum caught")
    print(24 >= black_drum  >= 15 ) and ((daily_limit_of_black_drum >= 5))
elif fish_question == "red drum":
    red_drum = input("Red Drum Not allowed to harvest due to red tide  ")
    print(red_drum)
elif fish_question == "spotted trout":
    spotted_trout = input(" Spotted Trout not in season due to red tide ")
    print(spotted_trout)
elif fish_question == "snook":
    snook = input(" Snook is not in season due to yo red tide ")
    print(snook)
elif fish_question == "tarpon":
    tarpon = input("Only one tarpon can be harvested per year with the purchase of a 50$ tag")
    print(tarpon)
elif fish_question =="goliath grouper":
    goliath_grouper = input("Goliath Grouper are endangered species. Harvesting is prohibited")
    print(goliath_grouper)
elif fish_question == "mullet":
    mullet = input("up to a 100 pounds of mullet can be harvested")
    print(mullet)
elif fish_question == "jack":
    jack = input("up to a 100 pounds of jack can be harvested")
    print(jack)
elif fish_question == "gag grouper":
    gag_grouper = int(input("Enter length of Gag grouper  "))
    daily_limit_of_gag_grouper = input("Enter amount of black grouper caught")
    print( gag_grouper >= 24 ) and ((daily_limit_of_gag_grouper <= 2))
elif fish_question == "flounder":
    flounder = int(input("Enter length of flounder  "))
    daily_limit_of_flounder = input("Enter amount of flounder")
    print(flounder >= 12 ) and ((daily_limit_of_flounder <= 10))

    pb = int(input("what size fish did you catch(in innches)? "))
    old_pb = int(input("what was the size of your personal best fish(in innches)?"))
    print(pb == old_pb) and (pb == old_pb)

total_length = 0
amount_of_fish_caught = int(input("How many fish did you catch?"))
for x in range(amount_of_fish_caught):
    length_of_fish = int(input("How long is the fish?"))
    total_length += length_of_fish
print(total_length / amount_of_fish_caught)

amount_of_snapper_per_person = input("amount of people fishing ")
print(int(float(amount_of_snapper_per_person) * 5))

amount_of_snapper_caught = int(input("Amount of snapper caught "))
limit_of_snapper = 5
remainder_of_snapper_to_be_caught = (amount_of_snapper_caught % 5)
print(remainder_of_snapper_to_be_caught)


#fish_list = []
#fishlist.append()
 #n = int(input())
 #largest_fish = int(input())
 #second_fish = int(input())
 #second_largest_fish = 0
 #if second_fish < largest_fish:
    # second_largest_fish = second_fish
 #else:
    # second_largest_fish = largest_fish
    # largest_fish = second_fish
 #for x in range(n-2) :
     #rest_num = int(input())
    #if rest_num > largest_fish:
     #    second_largest_fish = largest_fish
    #     largest_fish = rest_num
   #elif rest_num > second_fish:
         #second_largest_fish = rest_num
 #print(largest_fish) and (second_largest_fish)

 # need to learn how to add list


for X in range(3):
    Name = input("Enter your name ")
    total = 0
    for Y in range(3):
        size_of_fish_caught = int(input("Whats the size of your fish?"))
        total = total +  size_of_fish_caught
        average = total/3
    print("Name:",Name )
    print("Average:",format(average,"0.2f"))
