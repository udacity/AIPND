#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND/intropylab-classifying-images/alternative-to-classify_images.py
#                                                                             
# PROGRAMMER: Jennifer S.
# DATE CREATED: 04/19/2018                                  
# REVISED DATE: 
# PURPOSE: Alternative Programming of classify_images function using in 
#          operation to simply function
#
#   Example call:
#    python alternative-to-classify_images.py
##

# Imports python modules
import argparse
from time import time, sleep
from os import listdir

# Imports classifier function for using CNN to classify images 
from classifier import classifier 

# Main program function defined below
def main():
    # Sets path to folder that contains the pet images
    in_dir = "pet_images/"
    
    # Sets CNN model architecture as vgg
    in_arch = "vgg"
    
    # Sets Pet Image Labels dictionary as answers_dic 
    answers_dic = {'Basenji_00963.jpg': 'basenji', 'Basenji_00974.jpg': 'basenji',
                   'Basset_hound_01034.jpg': 'basset hound', 'Beagle_01125.jpg': 'beagle',
                   'Beagle_01141.jpg': 'beagle', 'Beagle_01170.jpg': 'beagle',
                   'Boston_terrier_02259.jpg': 'boston terrier',
                   'Boston_terrier_02285.jpg': 'boston terrier', 
                   'Boston_terrier_02303.jpg': 'boston terrier', 'Boxer_02426.jpg': 'boxer',
                   'cat_01.jpg': 'cat', 'cat_02.jpg': 'cat', 'cat_07.jpg': 'cat', 
                   'Cocker_spaniel_03750.jpg': 'cocker spaniel',
                   'Collie_03797.jpg': 'collie', 'Dalmatian_04017.jpg': 'dalmatian',
                   'Dalmatian_04037.jpg': 'dalmatian', 'Dalmatian_04068.jpg': 'dalmatian',
                   'fox_squirrel_01.jpg': 'fox squirrel', 'gecko_02.jpg': 'gecko',
                   'gecko_80.jpg': 'gecko', 
                   'German_shepherd_dog_04890.jpg': 'german shepherd dog',
                   'German_shepherd_dog_04931.jpg': 'german shepherd dog',
                   'German_shorthaired_pointer_04986.jpg': 'german shorthaired pointer',
                   'Golden_retriever_05182.jpg': 'golden retriever',
                   'Golden_retriever_05195.jpg': 'golden retriever',
                   'Golden_retriever_05223.jpg': 'golden retriever',
                   'Golden_retriever_05257.jpg': 'golden retriever', 
                   'Great_dane_05320.jpg': 'great dane', 
                   'great_horned_owl_02.jpg': 'great horned owl', 
                   'Great_pyrenees_05367.jpg': 'great pyrenees', 
                   'Great_pyrenees_05435.jpg': 'great pyrenees',
                   'Miniature_schnauzer_06884.jpg': 'miniature schnauzer',
                   'polar_bear_04.jpg': 'polar bear', 'Poodle_07927.jpg': 'poodle',
                   'Poodle_07956.jpg': 'poodle', 'Rabbit_002.jpg': 'rabbit',
                   'Saint_bernard_08010.jpg': 'saint bernard', 
                   'Saint_bernard_08036.jpg': 'saint bernard', 'skunk_029.jpg': 'skunk'} 

    # Creates Classifier Labels with classifier function, Compares Labels, 
    # and creates a results dictionary USING an alternative coding of 
    # the classify_images() function where the operator 'in' is used 
    # instead of the find() function. This alternative provides a more 
    # simple solution
    result_dic = classify_images(in_dir, answers_dic, in_arch)
    
    # Prints results of result_dic where matches are printed first
    # then non-matches are printed next using NEW-Style print formatting
    n_match = 0
    n_NOTmat = 0
    print("\n\n\nMATCHES:")
    for key in result_dic:
      if result_dic[key][2] == 1:
         n_match += 1
         print("{:2d}. Pet: {:>26}  Classifier: {:>40}".format(n_match, result_dic[key][0],
               result_dic[key][1]) )
    print("\n\nNOT-A-MATCH:")
    for key in result_dic:
      if result_dic[key][2] == 0:
         n_NOTmat += 1
         print("{:2d}. Pet: {:>26}  Classifier: {:>40}".format(n_NOTmat, result_dic[key][0],
               result_dic[key][1]) )
    

# Functions defined below
def classify_images(images_dir, petlabel_dic, model):
    """
    Creates classifier labels with classifier function, compares labels, and 
    creates a dictionary containing both labels and comparison of them to be
    returned.
     PLEASE NOTE: This function uses the classifier() function defined in 
     classifier.py within this function. The proper use of this function is
     in test_classifier.py Please refer to this program prior to using the 
     classifier() function to classify images in this function 
     Parameters: 
      images_dir - The (full) path to the folder of images that are to be
                   classified by pretrained CNN models (string)
      petlabel_dic - Dictionary that contains the pet image(true) labels
                     that classify what's in the image, where its' key is the
                     pet image filename & it's value is pet image label where
                     label is lowercase with space between each word in label 
      model - pretrained CNN whose architecture is indicated by this parameter,
              values must be: resnet alexnet vgg (string)
     Returns:
      results_dic - Dictionary with key as image filename and value as a List 
             (index)idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int)   where 1 = match between pet image and 
                    classifer labels and 0 = no match between labels
    """
    # Creates dictionary that will have all the results key = filename
    # value = list [Pet Label, Classifier Label, Match(1=yes,0=no)]
    results_dic = dict()

    # Process all files in the petlabels_dic - use images_dir to give fullpath
    for key in petlabel_dic:
       
       # Runs classifier function to classify the images classifier function 
       # inputs: path + filename  and  model, returns model_label 
       # as classifier label
       model_label = classifier(images_dir+key, model)
       
       # Processes the results so they can be compared with pet image labels
       # set labels to lowercase (lower) and stripping off whitespace(strip)
       model_label = model_label.lower()
       model_label = model_label.strip()
      
       # Put separate terms that 'may' compose the classifier label into a list so
       # that each term is an item in the list.
       model_label_list = model_label.split(", ")
       
       # defines truth as pet image label 
       truth = petlabel_dic[key]
       
       # If the pet image label is found within the classifier label list of terms 
       # as an exact match to on of the terms in the list - then they are added to 
       # results_dic as an exact match
       if truth in model_label_list:
           results_dic[key] = [truth, model_label, 1]
            
       # For those that aren't an exact term match to a term - checks if the pet_label
       # is part of the term like: "poodle" matching to "standard poodle" OR 
       # "cat" matching to "tabby cat" 
       else:
           # Sets found to False - IF pet image label is FOUND as part of a term within
           # the list of classifier label terms then will be set to True
           found = False
           
           # For loop to iterate through each term from model_label_list - splitting the
           # the term into words where truth is compare to each word to see if there is
           # a match - if so they are added to results_dic as a match and found = True
           # and searching through the for loop is terminated using the break
           for term in model_label_list:

               # splits the term into a word list using split()
               word_list = term.split(" ")

               # if the pet image label hasn't been found AND it exists in the word list
               # like 'poodle' in ['standard', 'poodle'] or 'cat' in ['tabby', 'cat']
               # then found = True, the results are added to results_dic and break is
               # used to break out of the for loop since a match was found
               if (not found) and truth in word_list:
                   found = True
                   results_dic[key] = [truth, model_label, 1]
                   break 

           # If pet image label isn't found within the terms that exist in the list of labels
           # the classifier function produces then set match = 0 (not a match)
           if not found:
               results_dic[key] = [truth, model_label, 0]
                                  
    # Return results dictionary
    return(results_dic)
                
                
# Call to main function to run the program
if __name__ == "__main__":
    main()