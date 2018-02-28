#!/bin/sh
# */AIPND/intropylab-classifying-images/run_models_batch_solution.sh
#                                                                             
# PROGRAMMER: Jennifer S.
# DATE CREATED: 02/08/2018                                  
# REVISED DATE: 02/27/2018 - reduce scope of program
# PURPOSE: Runs all three models to test which provides 'best' solution.
#          Please note output from each run has been piped into a text file.
#
# Usage: sh run_models_batch_solution.sh  -- will run program from commandline
#  
python check_images_solution.py --dir pet_images/ --arch resnet  --dogfile dognames.txt > resnet_solution.txt
python check_images_solution.py --dir pet_images/ --arch alexnet  --dogfile dognames.txt > alexnet_solution.txt
python check_images_solution.py --dir pet_images/ --arch vgg  --dogfile dognames.txt > vgg_solution.txt
