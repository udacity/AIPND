#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND/intropylab-classifying-images/check_images_v02.py
#                                                                             
# PROGRAMMER: Jennifer S.
# DATE CREATED: 01/30/2018                                  
# REVISED DATE: 02/27/2018  - reduce scope of program
# PURPOSE: Help student with coding bug in get_pet_labels()
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
    # Measures total program runtime by collecting start time
    start_time = time()
    
    # Creates & retrieves Command Line Arugments
    in_arg = get_input_args()

    # Creates Pet Image Labels by creating a dictionary 
    answers_dic = get_pet_labels(in_arg.dir)
    
    print("\n\nanswers_dic:")
    i = 0
    for key in answers_dic:
      i += 1
      print(i, "  key: ", key, "  value: ", answers_dic[key])
    
    # Measure total program runtime by collecting end time
    end_time = time()
    
    # Computes overall runtime in seconds & prints it in hh:mm:ss format
    tot_time = end_time - start_time
    print("\n** Total Elapsed Runtime:",
          str(int((tot_time/3600)))+":"+str(int((tot_time%3600)/60))+":"
          +str(int((tot_time%3600)%60)) )
    


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


def get_pet_labels(image_dir):
   """
    Creates a dictionary of pet labels based upon the filenames of the image 
    files. This is used to check the accuracy of the image classifier model.
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by pretrained CNN models (string)
    Returns:
     petlabels_dic - Dictionary storing image filename (as key) and Pet Image
                     Labels (as value)  
   """
   ## Needs to define petlabels_dic at top of program 
   petlabels_dic = dict()
    
   #AH Creates list of files in directory
   in_files = listdir(image_dir)
   
   getlabels_dic = dict()

   for idx in range(0, len(in_files), 1):
      if in_files[idx][0] !=".":
     
         image_name = in_files[idx].split("_")

         pet_label = ""
       
         for word in image_name:
         
            if word.isalpha():
               pet_label += word.lower() + " "
         
         pet_label = pet_label.strip()
     
         if in_files[idx] not in petlabels_dic:
            petlabels_dic[in_files[idx]] = pet_label
       
         else:
             print("Warning: Duplicate files exist in directory",
                   in_files[idx])
     
   return(petlabels_dic)
         
# Call to main function to run the program
if __name__ == "__main__":
    main()