#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND/intropylab-classifying-images/check_images_solution.py
#                                                                             
# TODO: Fillin your information in the programming header below
# PROGRAMMER:
# DATE CREATED:
# REVISED DATE:             <=(Date Revised - if any)
# PURPOSE: Check images & report results: read them in, predict their
#          content (classifier), compare prediction to actual value labels
#          and output results
#
# Use argparse Expected Call with <> indicating expected user input:
#      python check_images.py --dir <directory with images> --arch <model>
#             --dogfile <file that contains dognames>
#   Example call:
#    python check_images.py --dir pet_images/ --arch vgg --dogfile dognames.txt
##

# Imports python modules
import argparse
from time import time, sleep
from os import listdir

# Imports classifier function for using CNN to classify images 
from classifier import classifier 

# Main program function defined below
def main():
    # TODO: Define start_time to measure total program runtime by
    # collecting start time
    start_time = None
    
    # TODO: Define get_input_args() function to create & retrieve command
    # line arguments
    in_arg = get_input_args()
    
    # TODO: Define get_pet_labels() function to create pet image labels by
    # creating a dictionary with key=filename and value=file label to be used
    # to check the accuracy of the classifier function
    answers_dic = get_pet_labels()

    # TODO: Define classify_images() function to create the classifier labels with
    # the classifier function uisng in_arg.arch, comparing the labels, and
    # creating a dictionary of results (result_dic)
    result_dic = classify_images()
    
    # TODO: Define adjust_results4_isadog() function to adjust the results
    # dictionary(result_dic) to determine if classifier correctly classified
    # images as 'a dog' or 'not a dog'. This demonstrates if the model can
    # correctly classify dog images as dogs (regardless of breed)
    adjust_results4_isadog()

    # TODO: Define calculates_results_stats() function to calculate
    # results of run and puts statistics in a results statistics
    # dictionary (results_stats_dic)
    results_stats_dic = calculates_results_stats()

    # TODO: Define print_results() function to print summary results, incorrect
    # classifications of dogs and breeds if requested.
    print_results()

    # TODO: Define end_time to measure total program runtime
    # by collecting end time
    end_time = None

    # TODO: Define tot_time to computes overall run time in
    # seconds & prints it in hh:mm:ss format
    tot_time = None
    print("\n** Total Elapsed Run Time:", tot_time)



# TODO: Define all the function below. Notice that the input paramaters
# and return values have been left in the function headers along with
# some instruction regarding the function. This is to provide guidance
# for acheiving a solution similar to the instructor provided solution.
# If Feel free to ignore this guidance as long as you are able to acheive
# the desired outcome with this lab.
    
# get_input_args() - Handles retrieving and parsing the command line
# arguments created and defined using argparse module. This function 
# returns these arguments.
# 3 command line arguements are created:
# dir - Path to the pet image files(default- 'pet_images/')
# arch - CNN model architecture to use for image classification(default-
#        pick any of the following vgg, alexnet, resnet)
# dogfile - Text file that contains all labels associated to dogs(default-
#           'dognames.txt'
# @return parser.parse_args() - collection of commandline arguments 
def get_input_args():
    pass


# get_pet_labels(image_dir) - Creates a dictionary of pet labels based upon 
# the filenames of the image files. Reads in pet filenames and extracts the
# pet image labels from the filenames and returns these label as petlabel_dic
# This will be used to check the accuracy of the image classifier model.
# @param image_dir - The (full) path to the folder of images that are to be
#                     classified by pretrained CNN models
# @return petlabels_dic - Dictionary with key = filename value = label  
def get_pet_labels():
    pass


# classify_images(images_dir, petlabel_dic, model) - Creates classifier labels
# with classifier function, compares labels and creates a dictionary of 
# labels based upon this classification. The classification is returned by
# the pretrained CNN model whose architecture is defined by the input
# parameter model. Returns dictionary of both image labels and the comparison
# of them to each other.
#
# PLEASE NOTE: You will be using the classifier() function defined in 
#  classifier.py within this function. The proper use of the classifier()
#  function can be found in test_classifier.py. Please refer to this
#  program prior to using the classifier() function to classify images.
# @param images_dir - The (full) path to the folder of images that are to be
#                     classified by pretrained CNN models
# @param petlabel_dic - Dictionary that contains the pet image(true) labels
#                     that classify what's in the image key = filename & 
#                     value = pet image(true) label (lowercase with spaces) 
# @param model - pretrained CNN whose architecture is indicated by this 
#                parameter, choices are: resnet, alexnet, vgg
# @return results_dic - Dictionary with key = image filename  
#                      value = list[pet image label, classifier label, 1/0] 
#                      where 1 = match between pet image and classifer labels 
#                      and 0 = no match between labels
def classify_images():
   pass


# adjust_results4_isadog(results_dic, dogsfile) -  Adjusts the results 
# dictionary to determine if classifier correctly classified images 'as a dog'
# or 'not a dog' especially when not a match. Demonstrates if model
# architecture correctly classifies dog images even if it gets dog breed wrong
# @param results_dic - Dictionary with key = image filename  
#             value = list[pet image label, classifier label, 1/0, 1/0*, 1/0**] 
#             For 1/0 where 1 = match between pet image and classifer labels &  
#             0 = no match.  NOTE: 1/0* and 1/0** added by this function.
#             For 1/0* where 1 = pet image is a dog & 0 = pet Image is NOT a 
#             dog.  For 1/0** 1 = Classifier classifies image as a dog &
#             0 = Classifier classifies image as NOT a dog.
# @param dogsfile - text file that contains names of all dogs from ImageNet 
#                   1000 labels (used by classifier model) and dog names from
#                   the pet image files. This file has one dog name per line
#                   dog names are all in lowercase with spaces separating the 
#                   distinct words of the dogname. 
def adjust_results4_isadog():
    pass


# calculates_results_stats(results_dic) - Calculates statistics of the
# of the results of the run using classifier's model architecture on 
# classifying images. Then puts the results statistics in a dictionary 
# (results_stats) so that it's returned for printing to help determine the 
# 'best' model for classifying images. results_stats dictionary has 
# key = statistic's name & value = statistic's value  
# @param results_dic - Dictionary with key = image filename  
#             value = list[pet image label, classifier label, 1/0, 1/0*, 1/0**] 
#             For 1/0 where 1 = match between pet image and classifer labels &  
#             0 = no match.
#             For 1/0* where 1 = pet image is a dog & 0 = pet Image is NOT a 
#             dog.
#             For 1/0** 1 = Classifier classifies image as a dog &
#             0 = Classifier classifies image as NOT a dog.
# @return results_stats - Dictionary with key = statistic's name value = 
#                         statistics value
def calculates_results_stats():
    pass


# print_results(results_dic, results_stats, model,
#               print_incorrect_dogs = False, print_incorrect_breed = False) -
# Prints summary results on the classification and then prints incorrectly 
# classified dogs and incorrectly classified dog breeds if user indicates 
# they want those printouts (use non-default values)
# @param results_dic - Dictionary with key = image filename  
#             value = list[pet image label, classifier label, 1/0, 1/0*, 1/0**] 
#             For 1/0 where 1 = match between pet image and classifer labels &  
#             0 = no match.
#             For 1/0* where 1 = pet image is a dog & 0 = pet Image is NOT a
#             dog.
#             For 1/0** 1 = Classifier classifies image as a dog &
#             0 = Classifier classifies image as NOT a dog.
# @param results_stats - Dictionary with key = statistic's name value =
#                      statistics value 
# @param model - pretrained CNN whose architecture is indicated by this 
#                parameter, choices are: resnet, alexnet, vgg
# @param print_incorrect_dogs - Boolean - True prints incorrectly classified 
#                               dog images default = False(no print)
# @param print_incorrect_breed - Boolean - True prints incorrectly classified 
#                               dog breeds default = False(no print)
def print_results():
    pass

                
                
# Call to main function to run the program.
main()

