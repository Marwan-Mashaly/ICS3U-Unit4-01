#!/usr/bin/env python3

# Created by Marwan Mashaly
# Created on October 2019
# This program lets user to add total of number of loops made


def main():
    # This function lets user to add total of number of loops made
    sum = 0
    
    # input
    num = input("Enter number for loop: ")
    print("")
    # process & output
    try:
        int_check = int(num)
        while(int_check > 0):
            sum += int_check
            int_check -= 1
            print("The sum is", sum)
            
    except Exception:
        print("Invalid number")
    finally:
        print("")
        print("Thanks for trying")


if __name__ == '__main__':
    main()
