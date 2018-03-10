#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND/intropylab-classifying-images/command_line_arguments.py
#                                                                             
# PROGRAMMER: Jennifer S.                                                    
# DATE CREATED: 02/16/2018                                  
# REVISED DATE:             <=(Date Revised - if any)                         
# PURPOSE: Argparse example from AIPND 
#
#   Example call:
#    python command_line_arguments.py --dir my_folder/ --num 0
##

# Imports argparse python module
import argparse

# Main program function defined below
def main():
    # Creates Argument Parser object named parser
    parser = argparse.ArgumentParser()
    
    # Argument 1: that's a path to a folder
    parser.add_argument('--dir', type = str, default = 'my_folder/', 
                        help = 'path to the folder my_folder') 

    # Argument 2: that's an integer
    parser.add_argument('--num', type = int, default = 1, 
                        help = 'Number (integer) input') 

    # Assigns variable in_args to parse_args()
    in_args = parser.parse_args()

    # Accesses values of Arguments 1 and 2 by printing them
    print("Argument 1:", in_args.dir, "  Argument 2:", in_args.num)

                       
# Call to main function to run the program
if __name__ == "__main__":
    main()