#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND/intropylab-classifying-images/create_pet_image_labels.py
#                                                                             
# PROGRAMMER: Jennifer S.                                                   
# DATE CREATED: 02/16/2018                                  
# REVISED DATE:             <=(Date Revised - if any)                         
# PURPOSE: Creating Pet Image Labels code example from AIPND 
#
#   Example call:
#    python create_pet_image_labels.py 
##

# Imports only listdir function from OS module 
from os import listdir  


# Main program function defined below
def main():
    # USES OS module
    # Retrieve the filenames from folder pet_images/
    filename_list = listdir("pet_images/")
    
    # Print 10 of the filenames from folder pet_images/
    print("\nPrints 10 filenames from folder pet_images/")
    for idx in range(0, 10, 1):
        print("%2d file: %-25s" % (idx + 1, filename_list[idx]))

    # USES Dictionary
    # Creates empty dictionary named pet_dic
    pet_dic = dict()
    
    # Determines number of items in dictionary
    items_in_dic = len(pet_dic)
    print("\nEmpty Dictionary pet_dic - n items=", items_in_dic)
    
    # Adds new key-value pairs to dictionary ONLY when key doesn't already exist
    keys = ["beagle_0239.jpg", "Boston_terrier_02259.jpg"]
    values = ["beagle", "boston terrier"]
    for idx in range(0, len(keys), 1):
        if keys[idx] not in pet_dic:
            pet_dic[keys[idx]] = values[idx]
        else:
            print("** Warning: Key=", keys[idx], 
                  "already exists in pet_dic with value =", pet_dic[keys[idx]])
    
    #Iterating through a dictionary printing all keys & their associated values
    print("\nPrinting all key-value pairs in dictionary pet_dic:")
    for key in pet_dic:
        print("Key=", key, "   Value=", pet_dic[key])
        
    # USES String Functions 
    # Sets pet_image variable to a filename 
    pet_image = "Boston_terrier_02259.jpg"
    
    # Sets string to lower case letters
    low_pet_image = pet_image.lower()
    
    # Splits lower case string by _ to break into words 
    word_list_pet_image = low_pet_image.split("_")
    
    # Create pet_name starting as empty string
    pet_name = ""
    
    # Loops to check if word in pet name is only
    # alphabetic characters - if true append word
    # to pet_name separated by trailing space 
    for word in word_list_pet_image:
        if word.isalpha():
            pet_name += word + " "
            
    # Strip off starting/trailing whitespace characters 
    pet_name = pet_name.strip()
    
    # Prints resulting pet_name
    print("\nFilename=", pet_image, "   Label=", pet_name)
        
        
# Call to main function to run the program
if __name__ == "__main__":
    main()