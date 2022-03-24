import sys
from restaurantData import *


def main(args):
    #welcome the user
    print_welcome()
    
    #read the data
    list_of_food = read_types()
    list_of_restaurants = read_restaurants()

    #interact with the user
    select = ""
    while len(select) == 0:
        user_input = str(input(
        "\nWhat type of food would you like to eat?\nType the beginning of that food type and press enter to see if "
        "it's here.\n")).lower()

        food_match = []
        for food in list_of_food:
            if str(food).startswith(user_input):
                food_match.append(food)

        for food in food_match:
            print(food)

        if len(food_match) == 1:
            select_type = str(input(
            "\nThe only matching type for the specified input is " + food_match[0] + ". \nDo you want to look at " +
            food_match[0] + " restaurants? Enter y for yes and n for no\n")).lower()

        if select_type == 'y':
            select = food_match[0]
            print("\nSelected Food Type: " + select)

            #get a list of restaurants
            selected_restaurants = list_of_restaurants[select]
            for restaurant in selected_restaurants:
                print("--------------------------")
                print("Name: " + restaurant[0])
                print("Price: " + restaurant[1])
                print("Rating: " + restaurant[2])
                print("Address: " + restaurant[3])
                print("--------------------------\n")

            repeat_loop = str(input("\nDo you want to find other restaurants? Enter y for yes and n for no.\n")).lower()
            if repeat_loop == 'y':
                select = ""



def read_types():
    different_types =[]
    for type in types:
        different_types.append(type)
    return different_types

def read_restaurants():
    type_to_restaurant = {}
    for restaurant in restaurant_data:
        if restaurant[0] not in type_to_restaurant:
            restaurants = []
            restaurants.append(restaurant[1:])
            type_to_restaurant[restaurant[0]] = restaurants
        else:
            type_to_restaurant[restaurant[0]].append(restaurant[1:])

    return type_to_restaurant


def print_welcome():
    print("                *               ")
    print("  *             *            *  ")
    print("  *             *            *  ")
    print("  *             *            *  ")
    print(" ***           ***          *** ")
    print("*****         *****        *****")
    print("********************************")
    print("********************************")
    print("********************************")
    print("********************************")
    print("________________________________")
    print("*                              *")
    print("*                              *")
    print("* Welcome to CyBot Restaurant! *")
    print("*                              *")
    print("*______________________________*")


if __name__ == '__main__':
    main(sys.argv)