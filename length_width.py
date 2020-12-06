#!/usr/bin/env python3

# Created by Ryan Chung Kam Chung
# Created in December 2020
# Checks if the inputted lengths and widths form a square


def main():
    # This function checks if the inputted lengths and widths form a square

    print("Give me a length and a width and "
          "I will tell you if it forms a square!")

    # Input
    length_string = input("Enter the length: ")
    width_string = input("Enter the width: ")

    # Process
    try:
        length = int(length_string)
        width = int(width_string)

        if length == width:
            print("These 2 measurements form a square!")
        else:
            print("These 2 measurements do not form a square!")

    except Exception:
        print("One or both of the inputted measurements are not valid")


if __name__ == "__main__":
    main()
