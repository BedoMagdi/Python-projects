from os import system
from restaurantData import *


def main(args):
    print_welcome()



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
    main(system.argv)