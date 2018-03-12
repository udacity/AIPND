#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND/intropylab-classifying-images/data_structure.py
#                                                                             
# PROGRAMMER: Jennifer S.                                                    
# DATE CREATED: 02/16/2018                                  
# REVISED DATE:             <=(Date Revised - if any)                         
# PURPOSE: Data Struture for Results Code example from AIPND 
#
#   Example call:
#    python data_structure.py 
##

# Imports python modules


# Main program function defined below
def main():
    # Defining lists to populate dictionary 
    filenames = ["Beagle_01141.jpg", "Beagle_01125.jpg", "skunk_029.jpg" ]
    pet_labels = ["beagle", "beagle", "skunk"]
    classifier_labels = ["walker hound, walker foxhound", "beagle",
                         "skunk, polecat, wood pussy"]
    pet_label_is_dog = [1, 1, 0]
    classifier_label_is_dog = [1, 1, 0]

    # Defining empty dictionary
    results_dic = dict()
    
    # Populates empty dictionary with both labels &indicates if they match (idx 2)
    for idx in range (0, len(filenames), 1):
        # If first time key is assigned initialize the list with pet & 
        # classifier labels
        if filenames[idx] not in results_dic:
            results_dic[filenames[idx]] = [ pet_labels[idx], classifier_labels[idx] ]
 
        # Determine if pet_labels matches classifier_labels using find() string 
        # function - so if pet label is found within classifier label it's a match
        found = classifier_labels[idx].find(pet_labels[idx])
        
        # Key already exists because labels were added, append value to end of
        # list for idx 2 
        # if pet image label was FOUND then there is a match 
        if found >= 0:
            results_dic[filenames[idx]] += [ 1 ]
            
        # if pet image label was NOT found then there is no match
        else:
            results_dic[filenames[idx]] += [ 0 ]

    # Populates dictionary with whether or not labels indicate a dog image (idx 3&4)
    for idx in range (0, len(filenames), 1):
        # Key already exists, append value to end of list for idx 3 & 4
        # can use append() function instead of += to append to end of a list
        results_dic[filenames[idx]].append(pet_label_is_dog[idx])
        results_dic[filenames[idx]].append(classifier_label_is_dog[idx])
        
    # Iterates through the list to print the results for each filename
    for key in results_dic:
        print("\nFilename=", key, "\npet_image Label=", results_dic[key][0],
              "\nClassifier Label=", results_dic[key][1], "\nmatch=",
              results_dic[key][2], "\nImage is dog=", results_dic[key][3],
              "\nClassifier is dog=", results_dic[key][4]) 
        
        # Provides classifications of the results
        if sum(results_dic[key][2:]) == 3:
            print("*Breed Match*")
        if sum(results_dic[key][3:]) == 2:
            print("*Is-a-Dog Match*")
        if sum(results_dic[key][3:]) == 0 and results_dic[key][2] == 1:
            print("*NOT-a-Dog Match*")
            


# Call to main function to run the program
if __name__ == "__main__":
    main()