#!/bin/sh
# */AIPND/intropylab-classifying-images/run_models_batch_hints.sh
#                                                                             
# PROGRAMMER: Jennifer S.
# DATE CREATED: 02/08/2018                                  
# REVISED DATE: 05/14/2018  - created for check_images_hints.py 
# PURPOSE: Runs all three models to test which provides 'best' solution.
#          Please note output from each run has been piped into a text file.
#
# Usage: sh run_models_batch_hints.sh    -- will run program from commandline
#  
python check_images_hints.py --dir pet_images/ --arch resnet  --dogfile dognames.txt > resnet.txt
python check_images_hints.py --dir pet_images/ --arch alexnet --dogfile dognames.txt > alexnet.txt
python check_images_hints.py --dir pet_images/ --arch vgg  --dogfile dognames.txt > vgg.txt
