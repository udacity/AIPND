#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND/intropylab-classifying-images/check_images_hints.py
#                                                                             
# TODO: 0. Fill in your information in the programming header below
# PROGRAMMER:
# DATE CREATED:
# REVISED DATE:             <=(Date Revised - if any)
# PURPOSE: This Version of check_images.py is designed to provide students with
#          more "hints" regarding the solution. This version is specifically 
#          for students that are:
#          - NEW to using Python and programming in general,
#          - Less comforatable with programming in Python, and/or
#          - Have less time to devote to this Lab.
#          For a more challenging lab - edit check_images.py instead of this 
#          file. Additionally, if you get stuck working on the more 
#          challenging check_images.py file; you are encouraged to refer
#          back to this check_images_hints.py file for some helpful hints.
#
#          Check images & report results: read them in, predict their
#          content (classifier), compare prediction to actual value labels
#          and output results
#          
#
# Use argparse Expected Call with <> indicating expected user input:
#      python check_images_novice.py --dir <directory with images> --arch <model>
#             --dogfile <file that contains dognames>
#   Example call:
#    python check_images_hints.py --dir pet_images/ --arch vgg --dogfile dognames.txt
##

# Imports python modules
import argparse
from time import time, sleep
from os import listdir

# Imports classifier function for using CNN to classify images 
from classifier import classifier 

# Imports print functions that check the lab
from print_functions_for_lab_checks import *

# Main program function defined below
def main():
    # TODO: 1. Define start_time to measure total program runtime by
    # collecting start time
    start_time = None
    
    # TODO: 2. Define get_input_args() function to create & retrieve command
    # line arguments
    in_arg = get_input_args()
    
    # TODO: 3. Define get_pet_labels() function to create pet image labels by
    # creating a dictionary with key=filename and value=file label to be used
    # to check the accuracy of the classifier function
    answers_dic = get_pet_labels(in_arg.dir)

    # TODO: 4. Define classify_images() function to create the classifier 
    # labels with the classifier function uisng in_arg.arch, comparing the 
    # labels, and creating a dictionary of results (result_dic)
    result_dic = classify_images(in_arg.dir, answers_dic, in_arg.arch)
    
    # TODO: 5. Define adjust_results4_isadog() function to adjust the results
    # dictionary(result_dic) to determine if classifier correctly classified
    # images as 'a dog' or 'not a dog'. This demonstrates if the model can
    # correctly classify dog images as dogs (regardless of breed)
    adjust_results4_isadog(result_dic, in_arg.dogfile)

    # TODO: 6. Define calculates_results_stats() function to calculate
    # results of run and puts statistics in a results statistics
    # dictionary (results_stats_dic)
    results_stats_dic = calculates_results_stats(result_dic)

    # TODO: 7. Define print_results() function to print summary results, 
    # incorrect classifications of dogs and breeds if requested.
    print_results(result_dic, results_stats_dic, in_arg.arch, True, True)

    # TODO: 1. Define end_time to measure total program runtime
    # by collecting end time
    end_time = None

    # TODO: 1. Define tot_time to computes overall runtime in
    # seconds by replacing zero with a the mathematical calculation that 
    # computes overall runtime
    # The print statement prints Overall runtime in hh:mm:ss format
    tot_time = 0
    print("\n** Total Elapsed Runtime:",
          str(int((tot_time/3600)))+":"+str(int((tot_time%3600)/60))+":"
          +str(int((tot_time%3600)%60)) )



# TODO: 2.-to-7. Define all the function below. Notice that the input 
# paramaters and return values have been left in the function's docstrings. 
# This is to provide guidance for acheiving a solution similar to the 
# instructor provided solution. Feel free to ignore this guidance as long as 
# you are able to acheive the desired outcomes with this lab.

def get_input_args():
    """
    Retrieves and parses the command line arguments created and defined using
    the argparse module. This function returns these arguments as an
    ArgumentParser object. 
     3 command line arguements are created:
       dir - Path to the pet image files(default- 'pet_images/')
       arch - CNN model architecture to use for image classification(default-
              pick any of the following vgg, alexnet, resnet)
       dogfile - Text file that contains all labels associated to dogs(default-
                'dognames.txt'
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
    # TODO: 2. EDIT parse.add_argument statements BELOW to add type & help for:
    #          --arch - the CNN model architecture
    #          --dogfile - text file of names of dog breeds
    parser.add_argument('--arch', default = 'vgg' )
    parser.add_argument('--dogfile', default = 'dognames.txt' )


    # returns parsed argument collection
    return parser.parse_args()


def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels based upon the filenames of the image 
    files. Reads in pet filenames and extracts the pet image labels from the 
    filenames and returns these label as petlabel_dic. This is used to check 
    the accuracy of the image classifier model.
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by pretrained CNN models (string)
    Returns:
     petlabels_dic - Dictionary storing image filename (as key) and Pet Image
                     Labels (as value)  
    """
    # Creates list of files in directory
    in_files = listdir(image_dir)
    
    # Processes each of the files to create a dictionary where the key
    # is the filename and the value is the picture label (below).
 
    # Creates empty dictionary for the labels
    petlabels_dic = dict()
   
    # Processes through each file in the directory, extracting only the words
    # of the file that contain the pet image label
    for idx in range(0, len(in_files), 1):
       
       # Skips file if starts with . (like .DS_Store of Mac OSX) because it 
       # isn't an pet image file
       if in_files[idx][0] != ".":
           
           # Creates temporary label variable to hold pet label name extracted 
           pet_label = ""

           # TODO: 3. BELOW REPLACE pass with CODE that will process each 
           #          filename in the in_files list to extract the dog breed 
           #          name from the filename. Recall that each filename can be
           #          accessed by in_files[idx]. Be certain to place the 
           #          extracted dog breed name in the variable pet_label 
           #          that's created as an empty string ABOVE
           pass

           # If filename doesn't already exist in dictionary add it and it's
           # pet label - otherwise print an error message because indicates 
           # duplicate files (filenames)
           if in_files[idx] not in petlabels_dic:
              petlabels_dic[in_files[idx]] = pet_label
              
           else:
               print("Warning: Duplicate files exist in directory", 
                     in_files[idx])
 
    # returns dictionary of labels
    return(petlabels_dic)


def classify_images(images_dir, petlabel_dic, model):
    """
    Creates classifier labels with classifier function, compares labels, and 
    creates a dictionary containing both labels and comparison of them to be
    returned.
     PLEASE NOTE: This function uses the classifier() function defined in 
     classifier.py within this function. The proper use of this function is
     in test_classifier.py Please refer to this program prior to using the 
     classifier() function to classify images in this function. 
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
    # TODO: 4. EDIT and ADD code BELOW to do the following that's stated 
    #          in the comments below that start with "TODO: 4."
    # 
    # Creates dictionary that will have all the results key = filename
    # value = list [Pet Label, Classifier Label, Match(1=yes,0=no)]
    results_dic = dict()

    # Process all files in the petlabels_dic - use images_dir to give fullpath
    for key in petlabel_dic:
       
       # TODO: 4.a Set the string variable model_label to be the string that's 
       #           returned from using the classifier function instead of the   
       #           empty string below.
       #
       #  Runs classifier function to classify the images classifier function 
       # inputs: path + filename  and  model, returns model_label 
       # as classifier label
       model_label = ""

       # TODO: 4.b BELOW REPLACE pass with CODE to process the model_label to 
       #           convert all characters within model_label to lowercase 
       #           letters and then remove whitespace characters from the ends
       #           of model_label. Be certain the resulting processed string 
       #           is named model_label.
       #
       # Processes the results so they can be compared with pet image labels
       # set labels to lowercase (lower) and stripping off whitespace(strip)
       pass
       
       # defines truth as pet image label and trys to find it using find() 
       # string function to find it within classifier label(model_label).
       truth = petlabel_dic[key]
       found = model_label.find(truth)
       
       # If found (0 or greater) then make sure true answer wasn't found within
       # another word and thus not really found, if truely found then add to 
       # results dictionary and set match=1(yes) otherwise as match=0(no)
       if found >= 0:
           if ( (found == 0 and len(truth)==len(model_label)) or
                (  ( (found == 0) or (model_label[found - 1] == " ") )  and
                   ( (found + len(truth) == len(model_label)) or   
                      (model_label[found + len(truth): found+len(truth)+1] in 
                     (","," ") ) 
                   )      
                )
              ):            
               # TODO: 4.c REPLACE pass BELOW with CODE that adds the 
               #           filename (key) to results_dic dictionary for the 
               #           list (value) that contains the pet label (truth),
               #           the classifier label (model_label), and value that 
               #           indicates both pet label & classifier label match(1)
               #
               # Found pet label (truth) as stand-alone word(not within a word)
               # within classifier label (model_label) - is a match 
               pass


           # TODO: 4.d REPLACE pass BELOW with CODE that adds the 
           #           filename (key) to results_dic dictionary for the 
           #           list (value) that contains the pet label (truth),
           #           the classifier label (model_label), and value that 
           #           indicates pet label & classifier label don't match(0)
           #                   
           # Found within a word that composes the classifier label,  
           # like: 'fox' being found within 'foxhound' - not a match  
           else:
               pass


       # TODO: 4.e REPLACE pass BELOW with CODE that adds the 
       #           filename (key) to results_dic dictionary for the 
       #           list (value) that contains the pet label (truth),
       #           the classifier label (model_label), and value that 
       #           indicates pet label & classifier label don't match(0)
       #                   
       # if not pet label isn't found within classifier label - not a match
       else:
           pass 
               
    # Return results dictionary
    return(results_dic)



def adjust_results4_isadog(results_dic, dogsfile):
    """
    Adjusts the results dictionary to determine if classifier correctly 
    classified images 'as a dog' or 'not a dog' especially when not a match. 
    Demonstrates if model architecture correctly classifies dog images even if
    it gets dog breed wrong (not a match).
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List 
             (index)idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int)  where 1 = match between pet image and 
                            classifer labels and 0 = no match between labels
                    --- where idx 3 & idx 4 are added by this function ---
                    idx 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                            0 = pet Image 'is-NOT-a' dog. 
                    idx 4 = 1/0 (int)  where 1 = Classifier classifies image 
                            'as-a' dog and 0 = Classifier classifies image  
                            'as-NOT-a' dog.
     dogsfile - A text file that contains names of all dogs from ImageNet 
                1000 labels (used by classifier model) and dog names from
                the pet image files. This file has one dog name per line
                dog names are all in lowercase with spaces separating the 
                distinct words of the dogname. This file should have been
                passed in as a command line argument. (string - indicates 
                text file's name)
    Returns:
           None - results_dic is mutable data type so no return needed.
    """           
    # TODO: 5. EDIT and ADD code BELOW to do the following that's stated 
    #          in the comments below that start with "TODO: 5."
    # 
    # Creates dognames dictionary for quick matching to results_dic labels from
    # real answer & classifier's answer
    dognames_dic = dict()

    # Reads in dognames from file, 1 name per line & automatically closes file
    with open(dogsfile, "r") as infile:
        # Reads in dognames from first line in file
        line = infile.readline()

        # Processes each line in file until reaching EOF (end-of-file) by 
        # processing line and adding dognames to dognames_dic with while loop
        while line != "":

            # TODO: 5.a REPLACE pass with CODE remove the newline character from 
            #           the variable line  
            #
            # Process line by striping newline from line
            pass

            # TODO: 5.b REPLACE pass with CODE TO check if dogname(line) doesn't 
            #           exist within dognames_dic, then add the dogname(line) 
            #           to dognames_dic as the 'key' with the 'value' of 1. 
            #
            # adds dogname to dogsnames_dic if it doesn't already exist in dic
            pass 

            # Reads in next line in file to be processed with while loop
            # if this line isn't empty (EOF)
            line = infile.readline()
            
    
    
    # Add to whether pet labels & classifier labels are dogs by appending
    # two items to end of value(List) in results_dic. 
    # List Index 3 = whether(1) or not(0) Pet Image Label is a dog AND 
    # List Index 4 = whether(1) or not(0) Classifier Label is a dog
    # How - iterate through results_dic if labels are found in dognames_dic
    # then label "is a dog" index3/4=1 otherwise index3/4=0 "not a dog"
    for key in results_dic:

        # Pet Image Label IS of Dog (e.g. found in dognames_dic)
        if results_dic[key][0] in dognames_dic:
            
            # Classifier Label IS image of Dog (e.g. found in dognames_dic)
            # appends (1, 1) because both labels are dogs
            if results_dic[key][1] in dognames_dic:
                results_dic[key].extend((1, 1))

            # TODO: 5.c REPLACE pass BELOW with CODE that adds the following to
            #           results_dic dictionary for the key indicated by the 
            #           variable key - append (1,0) to the value. This indicates
            #           the pet label is-a-dog, classifier label is-NOT-a-dog. 
            #                              
            # Classifier Label IS NOT image of dog (e.g. NOT in dognames_dic)
            # appends (1,0) because only pet label is a dog
            else:
                pass

        # Pet Image Label IS NOT a Dog image (e.g. NOT found in dognames_dic)
        else:
            # TODO: 5.d REPLACE pass BELOW with CODE that adds the following to
            #           results_dic dictionary for the key indicated by the 
            #           variable key - append (0,1) to the value. This indicates
            #           the pet label is-NOT-a-dog, classifier label is-a-dog. 
            #                              
            # Classifier Label IS image of Dog (e.g. found in dognames_dic)
            # appends (0, 1)because only Classifier labe is a dog
            if results_dic[key][1] in dognames_dic:
                pass

            # TODO: 5.e REPLACE pass BELOW with CODE that adds the following to
            #           results_dic dictionary for the key indicated by the 
            #           variable key - append (0,1) to the value. This indicates
            #           the pet label is-NOT-a-dog, classifier label is-NOT-a-dog. 
            #                                              
            # Classifier Label IS NOT image of Dog (e.g. NOT in dognames_dic)
            # appends (0, 0) because both labels aren't dogs
            else:
                pass
            


def calculates_results_stats(results_dic):
    """
    Calculates statistics of the results of the run using classifier's model 
    architecture on classifying images. Then puts the results statistics in a 
    dictionary (results_stats) so that it's returned for printing as to help
    the user to determine the 'best' model for classifying images. Note that 
    the statistics calculated as the results are either percentages or counts.
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List 
             (index)idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int)  where 1 = match between pet image and 
                            classifer labels and 0 = no match between labels
                    idx 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                            0 = pet Image 'is-NOT-a' dog. 
                    idx 4 = 1/0 (int)  where 1 = Classifier classifies image 
                            'as-a' dog and 0 = Classifier classifies image  
                            'as-NOT-a' dog.
    Returns:
     results_stats - Dictionary that contains the results statistics (either a
                     percentage or a count) where the key is the statistic's 
                     name (starting with 'pct' for percentage or 'n' for count)
                     and the value is the statistic's value 
    """
    # TODO: 6. EDIT and ADD code BELOW to do the following that's stated 
    #          in the comments below that start with "TODO: 6."
    # 
    # creates empty dictionary for results_stats
    results_stats=dict()
    
    # Sets all counters to initial values of zero so that they can 
    # be incremented while processing through the images in results_dic 
    results_stats['n_dogs_img'] = 0
    results_stats['n_match'] = 0
    results_stats['n_correct_dogs'] = 0
    results_stats['n_correct_notdogs'] = 0
    results_stats['n_correct_breed'] = 0       
    
    # process through the results dictionary
    for key in results_dic:
        
        # Next 2 lines of CODE ONLY required for check_images_hints.py to allow
        # code to run while program is being built - breaks processing if 
        # results_dic isn't completely created
        if len(results_dic[key]) < 5:
            break
 
        # Labels Match Exactly
        if results_dic[key][2] == 1:
            results_stats['n_match'] += 1

        # TODO: 6.a REPLACE pass with CODE that counts how many pet images of
        #           dogs had their breed correctly classified. This happens 
        #           when the pet image label indicates the image is-a-dog AND 
        #           the pet image label and the classifier label match. You 
        #           will need to write a conditional statement that determines
        #           when the dog breed is correctly classified and then 
        #           increments 'n_correct_breed' by 1. Recall 'n_correct_breed' 
        #           is a key in the results_stats dictionary with it's value 
        #           representing the number of correctly classified dog breeds.
        #           
        # Pet Image Label is a Dog AND Labels match- counts Correct Breed
        pass
        
        # Pet Image Label is a Dog - counts number of dog images
        if results_dic[key][3] == 1:
            results_stats['n_dogs_img'] += 1
            
            # Classifier classifies image as Dog (& pet image is a dog)
            # counts number of correct dog classifications
            if results_dic[key][4] == 1:
                results_stats['n_correct_dogs'] += 1

        # TODO: 6.b REPLACE pass with CODE that counts how many pet images 
        #           that are NOT dogs were correctly classified. This happens 
        #           when the pet image label indicates the image is-NOT-a-dog 
        #           AND the classifier label indicates the images is-NOT-a-dog.
        #           You will need to write a conditional statement that 
        #           determines when the classifier label indicates the image 
        #           is-NOT-a-dog and then increments 'n_correct_notdogs' by 1. 
        #           Recall the 'else:' above 'pass' already indicates that the 
        #           pet image label indicates the image is-NOT-a-dog and 
        #          'n_correct_notdogs' is a key in the results_stats dictionary 
        #           with it's value representing the number of correctly 
        #           classified NOT-a-dog images.
        #           
        # Pet Image Label is NOT a Dog
        else:
            # Classifier classifies image as NOT a Dog(& pet image isn't a dog)
            # counts number of correct NOT dog clasifications.
            pass

    # Calculates run statistics (counts & percentages) below that are calculated
    # using counters from above.
    
    # calculates number of total images
    results_stats['n_images'] = len(results_dic)

    # calculates number of not-a-dog images using - images & dog images counts
    results_stats['n_notdogs_img'] = (results_stats['n_images'] - 
                                      results_stats['n_dogs_img']) 

    # TODO: 6.c REPLACE zero(0.0) with CODE that calculates the % of correctly
    #           matched images. Recall that this can be calculated by the
    #           number of correctly matched images ('n_match') divided by the 
    #           number of images. This result will need to be multiplied by
    #           100 to provide the percentage.
    #    
    # Calculates % correct for matches
    results_stats['pct_match'] = 0.0

    # TODO: 6.d REPLACE zero(0.0) with CODE that calculates the % of correctly
    #           classified dog images. Recall that this can be calculated by 
    #           the number of correctly classified dog images divided by the 
    #           number of dog images. This result will need to be multiplied by
    #           100 to provide the percentage.
    #    
    # Calculates % correct dogs
    results_stats['pct_correct_dogs'] = 0.0

    # TODO: 6.e REPLACE zero(0.0) with CODE that calculates the % of correctly
    #           classified breeds of dogs. Recall that this can be calculated 
    #           by the number of correctly classified breeds of dog divided by 
    #           the number of dog images. This result will need to be
    #           multiplied by 100 to provide the percentage.
    #    
    # Calculates % correct breed of dog
    results_stats['pct_correct_breed'] = 0.0

    # Calculates % correct not-a-dog images
    # Uses conditional statement for when no 'not a dog' images were submitted 
    if results_stats['n_notdogs_img'] > 0:
        results_stats['pct_correct_notdogs'] = (results_stats['n_correct_notdogs'] /
                                                results_stats['n_notdogs_img'])*100.0
    else:
        results_stats['pct_correct_notdogs'] = 0.0
        
    # returns results_stast dictionary 
    return results_stats


def print_results(results_dic, results_stats, model, 
                  print_incorrect_dogs = False, print_incorrect_breed = False):
    """
    Prints summary results on the classification and then prints incorrectly 
    classified dogs and incorrectly classified dog breeds if user indicates 
    they want those printouts (use non-default values)
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List 
             (index)idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int)  where 1 = match between pet image and 
                            classifer labels and 0 = no match between labels
                    idx 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                            0 = pet Image 'is-NOT-a' dog. 
                    idx 4 = 1/0 (int)  where 1 = Classifier classifies image 
                            'as-a' dog and 0 = Classifier classifies image  
                            'as-NOT-a' dog.
      results_stats - Dictionary that contains the results statistics (either a
                     percentage or a count) where the key is the statistic's 
                     name (starting with 'pct' for percentage or 'n' for count)
                     and the value is the statistic's value 
      model - pretrained CNN whose architecture is indicated by this parameter,
              values must be: resnet alexnet vgg (string)
      print_incorrect_dogs - True prints incorrectly classified dog images and 
                             False doesn't print anything(default) (bool)  
      print_incorrect_breed - True prints incorrectly classified dog breeds and 
                              False doesn't print anything(default) (bool) 
    Returns:
           None - simply printing results.
    """    
    # TODO: 7. EDIT and ADD code BELOW to do the following that's stated 
    #          in the comments below that start with "TODO: 7."
    # 
    # Prints summary statistics over the run
    print("\n\n*** Results Summary for CNN Model Architecture",model.upper(), 
          "***")
    print("%20s: %3d" % ('N Images', results_stats['n_images']))
    print("%20s: %3d" % ('N Dog Images', results_stats['n_dogs_img']))

    # TODO: 7.a REPLACE print("") with CODE that prints the text string 
    #          'N Not-Dog Images' and then the number of NOT-dog images 
    #          that's accessed by key 'n_notdogs_img' using dictionary 
    #          results_stats
    #
    print("")


    # Prints summary statistics (percentages) on Model Run
    print(" ")
    for key in results_stats:
        # TODO: 7.b REPLACE pass with CODE that prints out all the percentages 
        #           in the results_stats dictionary. Recall that all 
        #           percentages in results_stats have 'keys' that start with 
        #           the letter p. You will need to write a conditional 
        #           statement that determines if the key starts with the letter
        #           'p' and then you want to use a print statement to print 
        #           both the key and the value. Remember the value is accessed 
        #           by results_stats[key]
        #
        pass 
    
    # IF print_incorrect_dogs == True AND there were images incorrectly 
    # classified as dogs or vice versa - print out these cases
    if (print_incorrect_dogs and 
        ( (results_stats['n_correct_dogs'] + results_stats['n_correct_notdogs'])
          != results_stats['n_images'] ) 
       ):
        print("\nINCORRECT Dog/NOT Dog Assignments:")

        # process through results dict, printing incorrectly classified dogs
        for key in results_dic:

            # TODO: 7.c REPLACE pass with CODE that prints out the pet label 
            #           and the classifier label from results_dic dictionary    
            #           ONLY when the classifier function (classifier label) 
            #           misclassified dogs specifically: 
            #             pet label is-a-dog and classifier label is-NOT-a-dog 
            #               -OR- 
            #             pet label is-NOT-a-dog and classifier label is-a-dog 
            #           You will need to write a conditional statement that 
            #          determines if the classifier function misclassified dogs
            #          See 'Adjusting Results Dictionary' section in 
            #         '13. Classifying Labels as Dogs' for details on the 
            #          format of the results_dic dictionary. Remember the value
            #          is accessed by results_dic[key] and the value is a list
            #          so results_dic[key][idx] - where idx represents the 
            #          index value of the list and can have values 0-4.
            #
            # Pet Image Label is a Dog - Classified as NOT-A-DOG -OR- 
            # Pet Image Label is NOT-a-Dog - Classified as a-DOG
            pass


    # IF print_incorrect_breed == True AND there were dogs whose breeds 
    # were incorrectly classified - print out these cases                    
    if (print_incorrect_breed and 
        (results_stats['n_correct_dogs'] != results_stats['n_correct_breed']) 
       ):
        print("\nINCORRECT Dog Breed Assignment:")

        # process through results dict, printing incorrectly classified breeds
        for key in results_dic:

            # Pet Image Label is-a-Dog, classified as-a-dog but is WRONG breed
            if ( sum(results_dic[key][3:]) == 2 and
                results_dic[key][2] == 0 ):
                print("Real: %-26s   Classifier: %-30s" % (results_dic[key][0],
                                                          results_dic[key][1]))

                
                
# Call to main function to run the program
if __name__ == "__main__":
    main()
