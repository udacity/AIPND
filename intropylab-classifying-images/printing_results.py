#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND/intropylab-classifying-images/printing_results.py
#                                                                             
# PROGRAMMER: Jennifer S.                                                    
# DATE CREATED: 04/13/2018                                  
# REVISED DATE:             <=(Date Revised - if any)                         
# PURPOSE: Printing using lambda function & string formatting example from AIPND 
#
#   Example call:
#    python printing_results.py 
##

# Imports python modules

# Main program function defined below
def main():
    # Defining results_stats_dic
    results_stats_dic =  {'n_dogs_img': 30, 'n_match': 35,
                          'n_correct_dogs': 30, 'n_correct_notdogs': 10,
                          'n_correct_breed': 28, 'n_images': 40, 
                          'n_notdogs_img': 10, 'pct_match': 87.5,
                          'pct_correct_dogs': 100.0, 
                          'pct_correct_breed': 93.33333333333333, 
                          'pct_correct_notdogs': 100.0} 
    
    # Defines model
    model = "vgg"
    
    # Defines lambda function for spliting on separator, capitalizing first
    # word and putting spaces in between words. This is similar to the 
    # capwords function in String module except it replaces the sep with
    # blank spaces AND expects an input separator. 
    capwords2 = lambda string, sep: (' ').join(x.capitalize() 
                for x in string.split(sep))
    
    # NO FORMAT
    # Prints summary statistics (numbers) and model architecture type
    print("\n\nNO format - Print Example:")
    print("*** Results Summary for CNN Model Architecture", model.upper(), 
          "***")
    print("            N Images: ", results_stats_dic['n_images'])
    print("        N Dog Images: ", results_stats_dic['n_dogs_img'])
    print("    N Not-Dog Images: ", results_stats_dic['n_notdogs_img'])
    print(" ")
    print("           PCT Match: ", round(results_stats_dic['pct_match'], 1))
    print("    PCT Correct Dogs:", 
          round(results_stats_dic['pct_correct_dogs'], 1))
    print("   PCT Correct Breed: ",
          round(results_stats_dic['pct_correct_breed'], 1))
    print("PCT Correct Not Dogs:",
          round(results_stats_dic['pct_correct_notdogs'], 1))


    # OLD STRING FORMAT see following link:
    # https://docs.python.org/2/library/stdtypes.html#string-formatting
    # Prints summary statistics(numbers & Percentages)& model architecture type
    print("\n\nOLD format - Print Example:")
    print("*** Results Summary for CNN Model Architecture", model.upper(), 
          "***")     
    
    # Prints Counts first
    for key in results_stats_dic:
        if key[0] == 'n' and key[2] in ('i', 'd', 'n'):
            print("%20s: %3d" % (capwords2(key,"_"), 
                                 results_stats_dic[key]))
    # Prints Percentages second
    print(" ")
    for key in results_stats_dic:
        if key[0] == "p":
            print("%20s: %5.1f" % (capwords2(key, "_"),
                                   results_stats_dic[key]))


    # NEW STRING FORMAT see following link:
    # https://docs.python.org/3/library/string.html#format-string-syntax
    # Prints summary statistics (numbers) and model architecture type
    print("\n\nNEW format - Print Example:")
    print("*** Results Summary for CNN Model Architecture", model.upper(), 
          "***")             

    # Prints Counts first
    for key in results_stats_dic:
        if key[0] == 'n' and key[2] in ('i', 'd', 'n'):
            print("{:>20}: {:3d}".format(capwords2(key,"_"),
                                         results_stats_dic[key]))
    # Prints Percentages second
    print(" ")
    for key in results_stats_dic:
        if key[0] == "p":
            print("{:>20}: {:5.1f}".format(capwords2(key, "_"), 
                  results_stats_dic[key]))
    


# Call to main function to run the program
if __name__ == "__main__":
    main()