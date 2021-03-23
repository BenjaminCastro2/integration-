# Benjamin K Casto

# I wanted to create a program that gives out the regulations,tips for cathcing the fish and any aditional information for anglers located  in the inshore areas of SWFl.
# The user would insert the name of the a certain fish , then thy would be asked what they would like to know.
#The user could then awnser by asking for season, regulations,tips,area, or info.

# The information for the fish was taken from: myfwc.com/fishing/saltwater/recreatonal/

#i need to figure out ow to make it so that the first question the program ask is "whats your species?" then after choosing your species it would as questions acorinly.

#types of snapper

#snapper = (mangrove_snapper, lane_snapper, Mutton_snapper, Cubera_snapper)line did not work need to find out how to make one variable be equal to multiple things

#type_of_snapper = int(input("Enter type of snapper "))
#print(mangrove snapper)or(lane snapper)or(Mutton snapper)or(Cubera snapper)         want to make it so the user types the type of snapper then questions are based upon the species

mangrove_snapper = int(input("Enter length of Mangrove Snapper "))
daily_limit_of_mangrove_snapper = input("Enter amount of Mangrove Snapper caught")
print( mangrove_snapper >= 10)and((daily_limit_of >= 5))

lane_snapper =int(input("Enter length of Lane Snapper "))
daily_limit_of_lane_snapper = input("Enter amount of Lane Snapper caught")
print( lane_snapper >= 8)and((daily_limit_of_lane >= 5))

Mutton_snapper =int(input("Enter length of Mutton Snapper "))
daily_limit_of_lane_snapper = input("Enter amount of Mutton Snapper caught")
print( Mutton_snapper >= 18)and((daily_limit_of_Mutton >= 5))

Cubera_snapper =int(input("Enter length of Cubera Snapper "))
daily_limit_of_lane_snapper = input("Enter amount of Cubera Snapper caught")
print( Mutton_snapper >= 12)and((daily_limit_of_Mutton >= 5))

amount_of_snapper_per_person = input("amount of people fishing ")
print(int(float(amount_of_snapper_per_person) * 5))

#total amount of snapper

#total_weight_of_fish = input("totalt weight of fish ?" )
#amount_of_people_fishing = input("How many people are fishing ? ")    output did not work need to figure it out
#print(total_weight_of_fish)/(amount_of_people_fishin)

print(300 / 3) # what i am trying to do in the dode above. I want to divide the total weight of the fish by the amount of people

(2**3) # this does not really apply ro what i am trying to do

# if a fish is bittenin half and u decide to keep that fish if u catch 15.5 fish you technicall acording to regulations caught 16 fish
print(15.5//3 )

#snapper_caught = int(input("Enter amount "))
#peolpe_fishing = int(input("total amount of people fishing "))     getting error
#print(snapper_caught // people_fishing)
                     
print(10 % 3)
 #would be = to one

amount_of_snapper_caught = int(input("Amount of snapper caught "))
limit_of_snapper = 5
remainder_of_snapper_to_be_caught = (amount_of_snapper_caught % 5)
print(remainder_of_snapper_to_be_caught)
# now need it to make it so user can pick number higher then 5

amount_of_fish_over_Limit = int(input("amount of fish over "))
limit = 5
fish_that_need_to_be_returned = (amount_of_fish_over_Limit -5)                               












