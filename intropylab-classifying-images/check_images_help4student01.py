#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# *j-staab/AIPND/intropylab-classifying-images/check_images_help4student01.py
#                                                                             
# PROGRAMMER: Jennifer S.
# DATE CREATED: 01/30/2018                                  
# REVISED DATE: 02/27/2018  - reduce scope of program
# PURPOSE: Helps students with coding issues
#
# Use argparse Expected Call with <> indicating expected user input:
#      python check_images.py --dir <directory with images> --arch <model>
#             --dogfile <file that contains dognames>
#   Example call:
#    python check_images_solution.py --dir pet_images/ --arch vgg --dogfile dognames.txt
##

# Imports python modules
import argparse
from time import time, sleep
from os import listdir

# Imports classifier function for using CNN to classify images 
from classifier import classifier 

# Main program function defined below

def main():
    # TODO: 1. Define start_time to measure total program runtime by
    # collecting start time
    start_time = time()
    sleep(15)
    # TODO: 2. Define get_input_args() function to create & retrieve command
    # line arguments
    in_arg = get_input_args()
    # Student code below with Error - extra " after in_arg.dogfile 
    #print("Command Line Arguments:\n  dir =", in_arg.dir, "\n   arch =", in_arg.arch, "\n  dogfile =", in_arg.dogfile")
    # Fixing student code
    print("Command Line Arguments:\n  dir =", in_arg.dir, "\n   arch =", in_arg.arch, 
          "\n  dogfile =", in_arg.dogfile)

# Functions defined below
def get_input_args():
    """
    Retrieves and parses the command line arguments created and defined using
    the argparse module. This function returns these arguments as an
    ArgumentParser object.
    Parameters:
     None - simply using argparse module to create & store command line arguments
    Returns:
     parse_args() -data structure that stores the command line arguments object  
    """
    # Creates parse 
    parser = argparse.ArgumentParser()

    # Creates 3 command line arguments args.dir for path to images files,
    # args.arch which CNN model to use for classification, args.labels path to
    # text file with names of dogs.
    parser.add_argument('--dir', type=str, default='pet_images/', 
                        help='path to folder of images')
    parser.add_argument('--arch', type=str, default='vgg', 
                        help='chosen model')
    parser.add_argument('--dogfile', type=str, default='dognames.txt',
                        help='text file that has dognames')

    # returns parsed argument collection
    return parser.parse_args()
                
# Call to main function to run the program
if __name__ == "__main__":
    main()