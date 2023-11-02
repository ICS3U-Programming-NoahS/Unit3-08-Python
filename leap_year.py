#!/usr/bin/env python3

# Created by: Noah Smith
# Created on: Nov. 1st, 2023
# This program asks the user to enter a year
# then tells the user if it is a leap year


def main():
    # Get the year
    year_string = input("Enter a year: ")

    # Making sure the year is an integer
    try:
        year_int = int(year_string)

        # Check if the year is a leap year
        if year_int < 0:
            print("{} is not a valid year.".format(year_int))
        else:
            if year_int % 4 == 0:
                if year_int % 100 == 0:
                    if year_int % 400 == 0:
                        print("{} is a leap year.".format(year_int))
                    else:
                        print("{} is not a leap year.".format(year_int))
                else:
                    print("{} is a leap year.".format(year_int))
            else:
                print("{} is not a leap year.".format(year_int))
    except:
        print("{} is not an integer!".format(year_string))
    finally:
        print("Thanks for playing!")


if __name__ == "__main__":
    main()
