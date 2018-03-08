#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND/intropylab-classifying-images/timing_code.py
#                                                                             
# PROGRAMMER: Jennifer S.                                                    
# DATE CREATED: 02/16/2018                                  
# REVISED DATE:             <=(Date Revised - if any)                         
# PURPOSE: Timing Code example from AIPND 
#
#   Example call:
#    python timing_code.py 
##

# Imports time() and sleep() functions from time module
from time import time, sleep


# Main program function defined below
def main():
    # Sets start time 
    start_time = time()
    
    # Replace sleep(75) below with code you want to time
    sleep(75)
    
    # Sets end time
    end_time = time()

    # Computes overall runtime in seconds
    tot_time = end_time - start_time
    
    # Prints overall runtime in seconds
    print("\nTotal Elapsed Runtime:", tot_time, "in seconds.")
           
    # Prints overall runtime in format hh:mm:ss
    print("\nTotal Elapsed Runtime:", str( int( (tot_time / 3600) ) ) + ":" + 
          str( int(  ( (tot_time % 3600) / 60 )  ) ) + ":" + 
          str( int( ( (tot_time % 3600) % 60 ) ) ) )
                       
# Call to main function to run the program
if __name__ == "__main__":
    main()