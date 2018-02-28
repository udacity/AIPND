#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND/intropylab-classifying-images/check_images.py
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
    # TODO: Define overall_start_time to measure total program run time by
    # collecting start time:
    overall_start_time = None
    
    # TODO: Define get_input_args() function to get parsed commandline
    # arguments
    in_arg = get_input_args()
    
    # TODO: Define get_labels() function to create a dictionary with 
    # key=filename and value=file label to be used to check the accuracy of the
    # classifier function
    answers_dic = get_labels()

    # TODO: Define results_stats_dic to be an empty dictionary it will hold the 
    # final statistics on each run
    results_stats_dic = None

    # TODO: Define range in the for loop below so that runs the designated 
    # number of trial runs based upon the input arguments.
    # Loop that uses classifier to checks images, adjust classifiers results
    # dependent upon whether image 'is a dog' or 'is NOT a dog', calculates
    # the results statistics (% correct) & prints trial runs results statistics
    for idx in range(0, 0, 1):
        # IF you want to compute runtime on trials create start time measure
        # here
        
        # TODO: Define classify_images() function to create a results 
        # dictionary by classifying images using model in_arg.arch, and
        # comparing those classifications to the actual answers in answers_dic.
        result_dic=classify_images()
    
        # TODO: Define adjust_results4_isadog() function to adjusts the results
        # dictionary to determine if classifier correctly classified images as
        # 'a dog' or 'not a dog'. This demonstrates if model can correctly
        # classify dog images as dogs (regardless of breed)
        adjust_results4_isadog()
    
        # TODO: Define calculates_results_stats() function to calculate
        # results of run and puts statistics in results_stats_dic
        calculates_results_stats()

        # TODO: Define print_run_results_stats() function to print run summary
        # results and incorrect classifications of dogs and breeds if requested
        # IF you are computing runtime on trials you would need to input your
        # trial start time measure into this function
        print_run_results_stats()
    
    # TODO: Define print_overall_summary() function to prints Overall
    # Summary displaying Average percentages & other statistics
    print_overall_summary()
    
    # TODO: Define overall_end_time to measure total program run
    # time by collecting end time
    overall_end_time = None
    
    # TODO: Define tot_time to computes overall run time in
    # seconds & prints it in hh:mm:ss format
    tot_time = None
    print("\n  Total Elapsed Run Time:", tot_time)
    

# TODO: Define all the function below. Notice that the input paramaters
# and return values have been left in the function headers along with
# some instruction regarding the function. This is to provide guidance
# for acheiving a solution similar to the instructor provided solution.
# If Feel free to ignore this guidance as long as you are able to acheive
# the desired outcome with this lab.

# get_input_args() - Handles retrieving and parsing the commandline 
# arguments created and defined using argparse module. This function 
# returns these arguments.
# @return parser.parse_args() - collection of commandline arguments 
def get_input_args():
    pass


# get_labels(labels_dir) - Creates a dictionary of labels based upon the  
# filenames of the image files. This will be used to check the accuracy of 
# the image classifier model.
# @param labels_dir - The (full) path to the folder of images that are to be
#                     classified by pretrained CNN models
# @return labels_dic - Dictionary with key = filename value = label  
def get_labels():
    pass


# classify_images(images_dir, true_label_dic, model) - Creates a dictionary of 
# labels based upon the classification that is returned by the pretrained CNN 
# model whose architecture is defined by the input parameter model.
#
# PLEASE NOTE: You will be using the classifier() function defined in 
#  classifier.py within this function classify_images(). The proper use of the
#  classifier() function can be found in test_classifier.py Please refer to
#  this program prior to using the classifier() function to classify the 
#  images using a pretrained CNN model architecture.
# @param images_dir - The (full) path to the folder of images that are to be
#                     classified by pretrained CNN models
# @param true_label_dic - Dictionary that contains the true labels that
#                     that classify what's in the image key = filename & 
#                     value = true label (lowercase with spaces) 
# @param model - pretrained CNN whose architecture is indicated by this 
#                parameter, choices are: resnet, alexnet, vgg
# @return results_dic - Dictionary with key = image filename  
#                      value = list[real answer, classifier answer, 1/0] 
#                      where 1 = exact match between real and classifer labels 
#                      and 0 = no exact match
def classify_images():
    pass


# adjust_results4_isadog(results_dic, dogsfile) -  Adjusts the results 
# dictionary to determine if classifier correctly classified images 'as a dog'
# or 'not a dog' especially when not an exact match. Demonstrates if model 
# architecture correctly classifies dog images even if it gets dog breed wrong
# @param results_dic - Dictionary with key = image filename  
#             value = list[real answer, classifier answer, 1/0, 1/0*, 1/0**] 
#             For 1/0 where 1 = exact match between real and classifer labels &  
#             0 = no exact match.  1/0* and 1/0** added by this function.
#             For 1/0* where 1 = Real image is a dog & 0 = Real Image is NOT a 
#             dog.  For 1/0** 1 = Classifier classifies image to be a dog &
#             0 = Classifier classifies image as NOT a dog.
# @param dogsfile - text file that contains names of all dogs from ImageNet 
#                   1000 labels (used by classifier model) and dogn names from
#                   CU dog image dataset. This file has one dog name per line
#                   dog names are all in lowercase with spaces separating the 
#                   distinct words of the dogname. 
def adjust_results4_isadog():
    pass


# calculates_results_stats(results_dic, results_stats) -  Calculates statistics
# of the results of the run using classifier's model architecture on 
# classifying images. Then puts the results in a dictionary (results_stats) so 
# that you can record multiple runs to determine 'best' model the 
# key = statistic's name & value = statistic's value stored in a list for each 
# run.
# @param results_dic - Dictionary with key = image filename  
#             value = list[real answer, classifier answer, 1/0, 1/0*, 1/0**] 
#             For 1/0 where 1 = exact match between real and classifer labels &  
#             0 = no exact match. For 1/0* where 1 = Real image is a dog & 
#             0 = Real Image is NOT a dog.  For 1/0** 1 = Classifier classifies
#             image to be a dog & 0 = Classifier classifies image as NOT a dog.
# @param results_stats - Dictionary with key = statistic's name value = 
#                      statistics value - this is a list to hold values for
#                      each suscessive run [stat_run1, stat_run2, ...]
def calculates_results_stats():
    pass


# print_run_results_stats(results_dic, results_stats, run, print_incorrect_dogs
#                         =False, print_incorrect_breed=False, start_trial=-99)
# Prints summary statistics on each run and then prints incorrectly classified 
# dogs and incorrectly classified dog breeds if user indicates those printouts,
# also keeps record of trial run time if user indicates they want this 
# information
# PLEASE NOTE: This is the function you will pass in the trial's start time
#   IF you decide to compute average time each trial takes to run - for the
#   solution we computed average trial time.
# @param results_dic - Dictionary with key = image filename
#             value = list[real answer, classifier answer, 1/0, 1/0*, 1/0**] 
#             For 1/0 where 1 = exact match between real and classifer labels &  
#             0 = no exact match. For 1/0* where 1 = Real image is a dog & 
#             0 = Real Image is NOT a dog.  For 1/0** 1 = Classifier classifies
#             image to be a dog & 0 = Classifier classifies image as NOT a dog.
# @param results_stats - Dictionary with key = statistic's name value = 
#                      statistics value - this is a list to hold values for
#                      each suscessive run [stat_run1, stat_run2, ...]
# @param run - Run that the is being completed 
# @param start_trial - time trial run started to compute average trial time
#                      defaults to -99 so no trial time is computed otherwise
#                      expects start time from start of trial using time.time()
# @param print_incorrect_dogs - Boolean - True prints incorrectly classified 
#                               dog images default = False (no print) 
# @param print_incorrect_breed - Boolean - True prints incorrectly classified 
#                               dog breeds default = False (no print)
def print_run_results_stats():
    pass


# print_overall_summary(results_stats) -  Prints summary statistics over ALL
# runs and average run time if requested  
# @param results_stats - Dictionary with key = statistic's name value = 
#                      statistics value - this is a list to hold values for
#                      each suscessive run [stat_run1, stat_run2, ...]
def print_overall_summary():
    pass


                       
# Call to main function to run the program.
main()

