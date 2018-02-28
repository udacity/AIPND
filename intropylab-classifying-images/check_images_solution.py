#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND/intropylab-classifying-images/check_images_solution.py
#                                                                             
# PROGRAMMER: Jennifer S.
# DATE CREATED: 01/30/2018                                  
# REVISED DATE: 02/27/2018  - reduce scope of program
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
    # measures total program run time by collecting start time:
    overall_start_time = time()
    
    # gets parsed commandline arguments
    in_arg = get_input_args()
    
    # Create a dictionary with key=filename and value=file label to be used to
    # check the accuracy of the classifier function
    answers_dic = get_labels(in_arg.dir)

    # Creates dictionary to hold final statistics on each run
    results_stats_dic = dict()
     
    # Loop that uses classifier to checks images, adjust classifiers results
    # dependent upon whether image 'is a dog' or 'is NOT a dog', calculates
    # the results statistics (% correct) & prints trial runs results statistics
    for idx in range(0, in_arg.trials, 1):
        # measures trial time
        start_time_trial = time()
        
        # Create a results dictionary by classifying images using model 
        # in_arg.arch, and comparing those classifications to the actual
        # answers in answers_dic. 
        result_dic=classify_images(in_arg.dir, answers_dic, in_arg.arch)
    
        # Adjusts the results dictionary to determine if classifier correctly 
        # classified images as 'a dog' or 'not a dog'. This demonstrates if 
        # model can correctly classify dog images as dogs (regardless of breed)
        adjust_results4_isadog(result_dic, in_arg.dogfile)
    
        # Calculates results of run and puts statistics in results_stats_dic
        calculates_results_stats(result_dic, results_stats_dic)

        # Prints run summary results and incorrect classifications of dogs
        # and breeds if requested
        print_run_results_stats(result_dic, results_stats_dic, idx, 
                                start_time_trial, True, True)
    
    # Prints Overall Summary displaying Average percentages & other statistics
    print_overall_summary(results_stats_dic)
    
    # Measure total program run time by collecting end time:
    overall_end_time = time()
    
    # Computes overall run time in seconds & prints it in hh:mm:ss format
    tot_time = overall_end_time - overall_start_time
    print("\n  Total Elapsed Run Time:",
          str(int((tot_time/3600)))+":"+str(int((tot_time%3600)/60))+":"
          +str(int((tot_time%3600)%60)) )
    

# Functions defined below
    
# get_input_args() - Handles retrieving and parsing the commandline 
# arguments created and defined using argparse module. This function 
# returns these arguments.
# @return parser.parse_args() - collection of commandline arguments 
def get_input_args():
    # Creates parse 
    parser = argparse.ArgumentParser()

    # Creates 4 commandline arguments args.dir for path to images files,
    # args.arch which CNN model to use for classification, args.labels path to
    # text file with names of dogs, args.trails number of times to run 
    # classifier on the set of images.
    parser.add_argument('--dir', type=str, default='pet_images/', 
                        help='path to folder of images')
    parser.add_argument('--arch', type=str, default='vgg', 
                        help='chosen model')
    parser.add_argument('--dogfile', type=str, default='dognames.txt',
                        help='text file that has dognames')
    parser.add_argument('--trials', type=int, default=1,
                        help='Number of repeat runs')

    # returns parsed argument collection
    return parser.parse_args()


# get_labels(labels_dir) - Creates a dictionary of labels based upon the  
# filenames of the image files. This will be used to check the accuracy of 
# the image classifier model.
# @param labels_dir - The (full) path to the folder of images that are to be
#                     classified by pretrained CNN models
# @return labels_dic - Dictionary with key = filename value = label  
def get_labels(labels_dir):
   # Creates list of files in directory
   in_files=listdir(labels_dir)
   
   # Processes each of the files to create a dictionary where the key
   # is the filename and the value is the picture label (below).

   # Creates empty dictionary for the labels
   labels_dic=dict()
   
   # Processes through each file in the directory, extracting only the words
   # of the file that contain the label name
   for idx in range(0,len(in_files), 1):
       
       # Skips file if starts with . (like .DS_Store of Mac OSX) because it 
       # isn't an image file, processes each file name by extracting only the
       # letters from filename to create the label
       if in_files[idx][0] != ".":
           
           # Uses split to extract words of file label 
           image_name=in_files[idx].split("_")
       
           # Creates temporary label variable to hold the label name extracted 
           image_label=""
           
           # processes each of the character strings split by '_' that are in 
           # list image_name, such that if all letters in the string are 
           # characters then it makes them lowercase and separates the words
           # of the label by blanks
           for word in image_name:
               if word.isalpha():
                   image_label += word.lower() + " "
                   
           # strips off trailing whitespace
           image_label=image_label.strip()
           
           # if filename doesn't already exist in dictionary add it and it's
           # label - otherwise print an error message because duplicate files
           if in_files[idx] not in labels_dic:
              labels_dic[in_files[idx]]=image_label 
           else:
               print("Warning: Duplicate files exist in directory", 
                     in_files[idx])

   # returns dictionary of labels
   return(labels_dic)


# classify_images(images_dir, true_label_dic, model) - Creates a dictionary of 
# labels based upon the classification that is returned by the pretrained CNN 
# model whose architecture is defined by the input parameter model.
#
# PLEASE NOTE: You will be using the classifier() function defined in 
#  classifier.py within this function classify_images(). The proper use of the
#  classifier() function can be found in test_classifier.py Please refer to
#  this program prior to using the classifier() function to classify the 
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
def classify_images(images_dir, true_label_dic, model):
   # Creates dictionary that will have all the results key = filename
   # value = list [trueAnswer, ModelClassification, Correct(1=yes,0=no)]
   results_dic=dict()

   # Process all the files in the labels_dict - use images_dir to give fullpath
   for key in true_label_dic:
       
       # Runs classifier function to classify the images
       model_class=classifier(images_dir+key, model)
       
       # Processes the results  so they can be compared with true answers
       model_class=model_class.lower()
       model_class=model_class.strip()
       
       # defines true answer and trys to find it using find() string function
       truth = true_label_dic[key]
       found=model_class.find(truth)
       
       # If found (0 or greater) then make sure true answer wasn't found within
       # another word and thus not really found, if truely found then add to 
       # results dictionary and set correct=1 else set as correct=0(wrong)
       if found >= 0:
           if ( (found == 0 and len(truth)==len(model_class)) or
                ( ( (found == 0) or (model_class[found - 1] == " ") )  and
                  ( (found + len(truth) == len(model_class)) or   
                    (model_class[found + len(truth): found+len(truth)+1] in 
                     (","," ") ) ) )
              ):
               if key not in results_dic:
                   results_dic[key]=[truth, model_class, 1]
           else:
               if key not in results_dic:
                   results_dic[key]=[truth, model_class, 0]
       # if not found set results dictionary with correct=0(wrong)
       else:
           if key not in results_dic:
               results_dic[key]=[truth, model_class, 0]
               
   # Return results dictionary
   return(results_dic)
       

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
def adjust_results4_isadog(results_dic, dogsfile):
    # Reads in dognames from file - one name per line
    infile= open(dogsfile,"r")

    # Creates dognames dictionary for quick matching to results_dic labels from
    # real answer & classifier's answer
    dognames_dic=dict()

    # Reads in dognames one line at a time
    line = infile.readline()
 
    # Processes each line in file until reaching EOF (end-of-file)
    while line != "":

        # Process line by striping newline & adding dogname to dictionary
        line = line.rstrip()
        if line not in dognames_dic:
            dognames_dic[line]=1
        else:
            print("**Warning: Duplicate dognames", line)            

        # Reads in next line in file
        line = infile.readline()

    #closes file when complete
    infile.close()
    
    # Processes through results_dic to append whether(1) or not(0) REAL
    # answer Images were of Dogs and then whether(1) or not(0) the Classifier 
    # classified Images to be Dogs images.
    for key in results_dic:

        # Real answer IS image of Dog (e.g. found in dognames_dic)
        if results_dic[key][0] in dognames_dic:
            
            # Classifier answer IS image of Dog (e.g. found in dognames_dic)
            if results_dic[key][1] in dognames_dic:
                results_dic[key].extend((1,1))
                
            # Classifier answer IS NOT image of dog (e.g. NOT in dognames_dic)
            else:
                results_dic[key].extend((1,0))
            
        # Real answer IS NOT a Dog image (e.g. NOT found in dognames_dic)
        else:
            # Classifier answer IS image of Dog (e.g. found in dognames_dic)
            if results_dic[key][1] in dognames_dic:
                results_dic[key].extend((0,1))
                
            # Classifier answer IS NOT image of Dog (e.g. NOT in dognames_dic)
            else:
                results_dic[key].extend((0,0))


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
def calculates_results_stats(results_dic, results_stats):
    # 1st run has empty dictionary, initialize all stats into empty dictionary
    if len(results_stats) == 0:
        # sets counters for computing statistics to zero in dictionary where
        # key = statistic name value = statistic value - this is stored as a 
        # list where each run is stored [stat_run1, stat_run2, ..]   
        results_stats['n_dogs_img'] = [0]
        results_stats['n_exact_match'] = [0]
        results_stats['n_correct_dogs'] = [0]
        results_stats['n_correct_notdogs'] = [0]
        results_stats['n_correct_breed'] = [0]        

    # Isn't first run keys already in dictionary just extend the list
    else:    
        # sets counters for computing statistics in a dictionary where 
        # key = statistic name value = statistic value - this is stored as a
        # list where each run is stored [stat_run1, stat_run2, ..]    
        results_stats['n_dogs_img'] += [0]
        results_stats['n_exact_match'] += [0]
        results_stats['n_correct_dogs'] += [0]
        results_stats['n_correct_notdogs'] += [0]
        results_stats['n_correct_breed'] += [0]
    
    # calculates index that user is at in adding results stats per run
    idx = len(results_stats['n_dogs_img']) - 1
    
    # process through the results dictionary
    for key in results_dic:
        # Exact matches 
        if results_dic[key][2] == 1:
            results_stats['n_exact_match'][idx] += 1
            
            # Real Image/Classed as a Dog (& exact match)
            if results_dic[key][3] == 1:
                results_stats['n_correct_breed'][idx] += 1
        
        # Real Image is a Dog
        if results_dic[key][3] == 1:
            results_stats['n_dogs_img'][idx] += 1
            
            # Classifier classifies image as Dog (& real is dog)
            if results_dic[key][4] == 1:
                results_stats['n_correct_dogs'][idx] += 1
                
        # Real Image is NOT a Dog
        else:
            # Classifiere classifies image as NOT a Dog(& real isn't a dog)
            if results_dic[key][4] == 0:
                results_stats['n_correct_notdogs'][idx] += 1

    # 1st Run so must create keys for these statistics for calculation that use
    # counters above to calculate statistics
    if 'n_images' not in results_stats:
        results_stats['n_images'] = [len(results_dic)]
        results_stats['n_notdogs_img'] = [results_stats['n_images'][idx] - 
                      results_stats['n_dogs_img'][idx]] 

        # Calculates % correct for exact matches, dogs, not dogs, & breeds match
        results_stats['pct_exact_match'] = [(results_stats['n_exact_match'][idx]/
                     results_stats['n_images'][idx])*100.0]
        results_stats['pct_correct_dogs'] = [(results_stats['n_correct_dogs'][idx]/
                     results_stats['n_dogs_img'][idx])*100.0]    
        results_stats['pct_correct_breed'] = [(results_stats['n_correct_breed'][idx]/
                          results_stats['n_dogs_img'][idx])*100.0]

        # Handles cases where no 'not a dog' images were submitted 
        if results_stats['n_notdogs_img'][idx] > 0:
            results_stats['pct_correct_notdogs'] = [(results_stats['n_correct_notdogs'][idx]/
                     results_stats['n_notdogs_img'][idx])*100.0]
        else:
            results_stats['pct_correct_notdogs'] = [0.0]
            
    # Isn't 1st run so alreayd has keys for these statistics calculations that
    # use counters above to calculate statistics
    else:
        results_stats['n_images'] += [len(results_dic)]
        results_stats['n_notdogs_img'] += [results_stats['n_images'][idx] - 
                      results_stats['n_dogs_img'][idx]] 

        # Calculates % correct for exact matches, dogs, not dogs, & breeds match
        results_stats['pct_exact_match'] += [(results_stats['n_exact_match'][idx]/
                     results_stats['n_images'][idx])*100.0]
        results_stats['pct_correct_dogs'] += [(results_stats['n_correct_dogs'][idx]/
                     results_stats['n_dogs_img'][idx])*100.0]    
        results_stats['pct_correct_breed'] += [(results_stats['n_correct_breed'][idx]/
                          results_stats['n_dogs_img'][idx])*100.0]

        # Handles cases where no 'not a dog' images were submitted 
        if results_stats['n_notdogs_img'][idx] > 0:
            results_stats['pct_correct_notdogs'] += [(results_stats['n_correct_notdogs'][idx]/
                     results_stats['n_notdogs_img'][idx])*100.0]
        else:
            results_stats['pct_correct_notdogs'] += [0.0]
 

# print_run_results_stats(results_dic, results_stats, run, start_trial=-99,
#                         print_incorrect_dogs=False, print_incorrect_breed=False)
# Prints summary statistics on each run and then prints incorrectly classified 
# dogs and incorrectly classified dog breeds if user indicates those printouts,
# also keeps record of trial run time if user indicates they want this information
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
def print_run_results_stats(results_dic, results_stats, run, start_trial = -99,
                            print_incorrect_dogs=False, 
                            print_incorrect_breed=False):
    # Prints summary statistics on Run
    print("\n\nRESULTS - Run",run+1,":")
    for key in results_stats:
        if key[0] == "n":
            print("%20s: %3d" % (key, results_stats[key][run]))
        elif key[0] == "p":
            print("%20s: %5.1f" % (key, results_stats[key][run]))
    
    # if computing trial times 
    if start_trial!=-99:
        end_trial=time()
        trial_tm = end_trial - start_trial
        # if first run initiate list
        if run == 0:
            results_stats['run_time'] = [trial_tm]
                    
        # Not first run add to list
        else:
            results_stats['run_time'] += [trial_tm]
                    
        # print trial results in hh:mm:ss format
        print("      Trial Run Time: ", str(int((trial_tm/3600)))+":"+
              str(int((trial_tm%3600)/60))+":"+str(int((trial_tm%3600)%60)) )

    # IF print_incorrect_dogs == True and there were images incorrectly 
    # classified as dogs or vs versa - print out these cases
    if (print_incorrect_dogs and ((results_stats['n_correct_dogs'][run] 
           + results_stats['n_correct_notdogs'][run]) != 
           results_stats['n_images'][run]) ):
        print("\nINCORRECT Dog/NOT Dog assignments:")

        # process through the results dictionary
        for key in results_dic:

            # Real Image is a Dog - Classified as NON DOG
            if results_dic[key][3] == 1 and results_dic[key][4] == 0:
                print("Real: %-26s   Classifier: %-30s" % (results_dic[key][0],
                                                          results_dic[key][1]))
                    
            # NOT a Dog - Classified as DOG
            if results_dic[key][3] == 0 and results_dic[key][4] == 1:
                print("Real: %-26s   Classifier: %-30s" % (results_dic[key][0],
                                                          results_dic[key][1]))

    # IF print_incorrect_breed == True and there were dogs whose breeds 
    # were incorrectly classified - print out these cases                    
    if (print_incorrect_breed and (results_stats['n_correct_dogs'][run] !=
           results_stats['n_correct_breed'][run]) ):
        print("\nINCORRECT Dog Breed Assignment:")

        # process through the results dictionary
        for key in results_dic:

            # Real Image is a Dog, classified as dog but wrong breed
            if (results_dic[key][3] == 1 and results_dic[key][4] == 1 and
                   results_dic[key][2] == 0):
                print("Real: %-26s   Classifier: %-30s" % (results_dic[key][0],
                                                          results_dic[key][1]))


# print_overall_summary(results_stats) -  Prints summary statistics over ALL
# runs and average run time if requested  
# @param results_stats - Dictionary with key = statistic's name value = 
#                      statistics value - this is a list to hold values for
#                      each suscessive run [stat_run1, stat_run2, ...]
def print_overall_summary(results_stats):
    # Prints summary statistics over ALL runs
    print("\n\nSUMMARY RESULTS OVER",len(results_stats['n_images']),"RUNS:")
    print("%20s: %3d" % ('n_images', results_stats['n_images'][0]))
    print("%20s: %3d" % ('n_dogs_img', results_stats['n_dogs_img'][0]))
    print("%20s: %3d" % ('n_notdogs_img', results_stats['n_notdogs_img'][0]))
    
    # sets average trial runtime counter to -99 just in case wasn't computed
    avg_tm = -99
    
    for key in results_stats:
        # computes statistics for percentage calculations
        if key[0] == "p":
            # Compute length of list
            n = len(results_stats[key])
                        
            # Compute Average value 
            avg = sum(results_stats[key])/n
            
            # Compute Variance of list
            sum_diff_sq = 0
            for num in results_stats[key]:
                sum_diff_sq += (num - avg)**2
                
            # handles cases of 1 trial since avg = single value var = 0
            if n > 1:
                variance = sum_diff_sq /(n-1)
            else:
                variance = 0
            
            # Compute Confidence interval
            # Compute standard error => std_dev/n**1/2 or (var/n)**1/2
            se = (variance / n)**(1/2)
            
            # Compute upper & lower 99% confidence interval assumes normal dist
            upper99 = avg + (2.58 * se)
            lower99 = avg - (2.58 * se)
            
            # Caps upper 99%CI at 100% (logical upper limit)
            if upper99 > 100.0:
                upper99 = 100.0
            
            # Caps lower 99%CI at 0% (logical lower limit)
            if lower99 < 0.0:
                lower99 = 0.0
            
            # Prints summary statistics
            print("%20s Avg: %5.1f  Var: %6.2f  99CI: %5.1f to %5.1f" % 
                  (key.upper(), avg, variance, upper99, lower99))   
            
        # computes average trial run time if it was calculated
        elif key[0] == "r":
            avg_tm = sum(results_stats[key])/len(results_stats[key])
            
    # prints average trial run time if it was calculated in hh:mm:ss format
    if avg_tm != -99:
        print("      Avg Trial Run Time: ", str(int((avg_tm/3600)))+":"+
                     str(int((avg_tm%3600)/60))+":"+str(int((avg_tm%3600)%60)))
            

                       
# Call to main function to run the program.
main()

