#  Notes: Frequently Asked Questions for Classifying Images Lab
These notes pertain to Frequently Asked Questions (FAQ) for the **_2. Intro to Python_**, **_Lesson 6. Lab: Classify Images_** that were posted and addressed on AIPND slack. We recommend that you review these notes prior to starting the **_Classify Images Lab_** to help clarify potential points of confusion regarding the lab.
&nbsp;  
&nbsp;     
    
## Quick Links to Frequently Asked Questions 
* [GitHub AIPND Repository Link](https://github.com/udacity/AIPND)
* [Approaching and Completing the Lab](https://github.com/udacity/AIPND/blob/master/notes/lab_intro-to-python-lab.md#approaching-and-completing-the-lab)
* [Running the Lab on a Local Computer](https://github.com/udacity/AIPND/blob/master/notes/lab_intro-to-python-lab.md#running-the-lab-on-a-local-computer)
* [Files Required to Run **_check_images.py_** Locally](https://github.com/udacity/AIPND/blob/master/notes/lab_intro-to-python-lab.md#files-required-to-run-check_imagespy-locally)
* [Running Batch Files on Windows OS Locally](https://github.com/udacity/AIPND/blob/master/notes/lab_intro-to-python-lab.md#running-batch-files-on-windows-os-locally)
* [Forking the GitHub Respository for Solution display and debugging](https://github.com/udacity/AIPND/blob/master/notes/lab_intro-to-python-lab.md#forking-the-github-respository-for-solution-display-and-debugging)
* [Eliminating Syntax Errors with Text Editor/Integrated Development Environment](https://github.com/udacity/AIPND/blob/master/notes/lab_intro-to-python-lab.md#eliminating-syntax-errors-with-text-editorintegrated-development-environment)
* [Cutting and Pasting Code in the Classroom](https://github.com/udacity/AIPND/blob/master/notes/lab_intro-to-python-lab.md#cutting-and-pasting-code-in-the-classroom)
* [Indention of Python Code](https://github.com/udacity/AIPND/blob/master/notes/lab_intro-to-python-lab.md#indention-of-python-code)
* [Formatting Print Statements](https://github.com/udacity/AIPND/blob/master/notes/lab_intro-to-python-lab.md#formatting-print-statements)
* [Replacing Pass Statements](https://github.com/udacity/AIPND/blob/master/notes/lab_intro-to-python-lab.md#replacing-pass-statements)
* [Alternative Solution for **_11.Classifying Images - Part 1_**](https://github.com/udacity/AIPND/blob/master/notes/lab_intro-to-python-lab.md#alternative-solution-for-11-classifying-images---part-1)
&nbsp;  
&nbsp;     
  
## Approaching and Completing the Lab
This lab provides the student with the experience of solving a much larger, more complex problem using python. This lab will require the student write a few hundred lines of code as compared to the fewer lines of code needed to complete the quizzes of the lessons. This lab will increase a student's experience using python to solve a complex problem, especially for students that are newer to python and software engineering. Additionally, this lab should better prepare students for completing the project. The percent viewed of the lab has no bearing upon student graduation from the AIPND; therefore, students are free to use as much or as little _help_ as they need from the materials provided.

To best address all levels of experience with programming and python, the lab may contain more information than is needed to complete the lab for some more experienced students. The instructor suggests students focus on the top part of each section of the lab labeled **_Coding within the check_images.py_**. 

### **_Coding within the check_images.py_** provides:
* **_Code to Edit_** - The parts of **_check_images.py_** students will be editing for that section
* **_Expected Outcome_** - The expected outcome once the edits are completed and the program is _run_
* **_Checking your code_** - How to best check that the _edits_ provided the _expected outcome_. 

### All parts of the section after **_Coding within the check_images.py_** are there to provide:
* Additional information and code about the python modules that were used in the instructor solution
* Additonal Information about files and functions that were used in the instructor solution 
* The GitHub repository link in **_Code_** section to the _code_ displayed within that section
* The solutions video in **_Solutions Video_**

Be aware that some times more information is provided than will be used in the solution, as a means to provide complete examples that aren't necessarily the exact same as those that will be used in the lab solution. Additonally, the instructor solution breaks certain coding concepts into multiple lines of code as to provide a solution that is easier to understand to the _beginning_ programmer. The instructor solution also contains _data checks_ that verify the data is in proper format prior to it's use within the program.  These are left as examples to the student as techniques that can be used when dealing with _real_ data that may not conform to an expected format.
&nbsp;   
&nbsp;   
     
## Running the Lab on a Local Computer
While it is recommended that you work on the lab within the **_5. Lab Workspace_**, to run the lab on a local computer, you will have needed to have python 3.6 intalled on your computer. 
### Installing Anaconda 
The easiest way to install python and the appropriate python modules is to install [Anaconda](https://www.anaconda.com/download). You will also have found the directions to install Anaconda in **_2. Intro to Python_**, **_Lesson 5. Scripting_**, **_Section 3. Install Python Using Anaconda_**. 
### Installing PyTorch and torchvision
### Linux or OSX(Mac)
For this lab you will also need to install the python packages pytorch and torchvision.  If your local computer has a Linux or OSX (Mac) operating system look to [*Get Started.*](http://pytorch.org/) for installation instructions. 
### Windows 
Although not designed to run on a Windows operating system, the following have succeeded with installation for student and instructors.
#### Windows 7
```terminal
conda install -c peterjc123 pytorch-cpu
pip install torchvision
```
#### Windows 10
With acknowledgement to Giu of the April Cohort for providing the installation commands.
```terminal
conda install -c peterjc123 pytorch cuda90
pip install torchvision
```
With acknowledgement to Oliver E. of the April Cohort for providing alternative methods to run the pytorch and torchvision on Windows 10 using Linux environment. Other options are to install Windows Substyem for Linux (WSL) or VMware to install Linux on a virtual environment. For directions for [installation of WSL](https://docs.microsoft.com/en-us/windows/wsl/install-win10) and for [installation of VMware](http://partnerweb.vmware.com/GOSIG/Windows_10.html#installation). 
&nbsp;     
&nbsp;    
   
## Files Required to Run **_check_images.py_** Locally
The following files and folders need to be put in the same folder as the **_check_images.py_** python program on your local computer. You will find these files and folders within the [GitHub AIPND Repository](https://github.com/udacity/AIPND/tree/master/intropylab-classifying-images). There are more programs in the repository than you will need, these extra programs are there to provide the code within the lessons in a format that can be copied and pasted from.
### Needed Files:
* **pet_images**  (folder of 40 pet image)
* **classifier.py** (classifier function you will be using to classify the images)
* **dognames.txt** (file that contains all the valid dog names from the classifier function and the pet image files)
* **imagenet1000_clsid_to_human.txt** (dictionary that converts the classifier function ids to text labels)
* **run_models_batch.sh** (a bash script that will run check_images.py sequentially for all 3 model architectures and output their results to text files - on Unix/Linux/OSX/Lab Workspace from a terminal window)
* **run_models_batch.bat** (a batch script that will run check_images.py sequentially for all 3 model architectures and output their results to text files - on Windows from the Anaconda Prompt window)
* **test_classifier.py** (an example program that demonstrates how to use the classifier function)

Also be aware the instructor provided solution also exists within the GitHub repository as the file **_check_images_solution.py_** and the file **_run_models_batch_solution.sh_** can be used to run the instructor solution for all 3 model architectures in a Unix/Linux/OSX/Lab Workspace environment from a _terminal_ window. For Windows, you will be using the file **_run_models_batch_solution.bat_** from the _Anaconda Prompt_ window (see next [FAQ](https://github.com/udacity/AIPND/blob/master/notes/lab_intro-to-python-lab.md#running-batch-files-on-windows-os-locally) for details).
&nbsp;   
&nbsp;     
     
## Running Batch Files on Windows OS Locally
To run the files **_run_models_batch_** and **_run_models_batch_solution_** that run all 3 model architectures using **_check_images.py_** or **_check_images_solution.py_** on a Windows OS locally; you will need to use the files that end with the extention **_.bat_** instead of the extension **_.sh_**.  You will have also needed to have installed Anaconda on your computer (see following [FAQ](https://github.com/udacity/AIPND/blob/master/notes/lab_intro-to-python-lab.md#running-the-lab-on-a-local-computer) for details on Anaconda installation).
### Directions:
* Open the **Anaconda Prompt** - either from typing **_Anaconda Prompt_** within the search bar and selecting it _or_ by clicking on it once it's found within the **Anaconda** folder of programs.
* Navigate to the _folder_ within the **Anaconda Prompt** that contains the _Lab files_ including **_check_images.py_** and **_run_models_batch.bat_** using the command [_cd_](https://en.wikipedia.org/wiki/Cd_(command)).
* Type the command within the **Anaconda Prompt**:
```terminal
run_models_batch.bat
```
If instead you are running the instructor solution, **_check_images_solution.py_**, you will replace all instances of **_run_models_batch.bat_** from the _directions_ above with **_run_models_batch_solution.bat_**.
&nbsp;     
&nbsp;         
    
## Forking the GitHub Respository for Solution display and debugging
We recommend forking the [github repository for AIPND](https://github.com/udacity/AIPND) to display your solution and to allow for improved debugging support. See the following for directions on [joining GitHub](https://github.com/join?source=header-home) and for direction on [how to fork a GitHub repository](https://help.github.com/articles/fork-a-repo/). Additionally, forking the repository will enable you to more easily show AIPND instructors and students where you are having difficulty with coding the lab. One can always provide others a link to the code that seems to have errors within their fork.
&nbsp;   
&nbsp;   
    
## Eliminating Syntax Errors with Text Editor/Integrated Development Environment 
If you are experiencing a lot of syntax errors with your code, you may consider downloading your code and looking at it with your favorite text editor/IDE to help eliminate the syntax errors from your program.  Recall in **_2. Intro to Python_**, **_Lesson 5. Scripting_**, **_Section 6. Programming Environment Setup_** you were provided with a number of text editors that are available to use with python (like _Atom_, _Sublime Text_, _Notepad++_). Additionally, when you installed Anaconda, the Spyder IDE (Integrated Development Environment) for python should be available through the _Anaconda Navigator_. 
&nbsp;   
&nbsp;   
     
## Cutting and Pasting Code in the Classroom
If you cut and paste code directly from the classroom, it is very likely you will generate syntax errors with the single and double quotes. This is because the font type differences.  If you are going to cut and paste code from the classroom, you will need to erase and replace any copied double or single quotes.  Additionally, cutting and pasting code from the classroom may also result in issues regarding the proper code indention; therefore, it is not recommended to cut and paste code directly from the classroom.
&nbsp;    
&nbsp;   
     
## Indention of Python Code
Indention is used within Python to distinquish between blocks of code; whereas, with other programming languages, like Java and  C++,  they may have used curly brackets. The [PEP8 Style guide](https://www.python.org/dev/peps/pep-0008/) provides the standard for python code and is what has been used for the programs within the Github respository and the Lab workspace. The [PEP8 standard for indention](https://www.python.org/dev/peps/pep-0008/#indentation) is to use 4 spaces for each indention level. Not using 4 spaces for indention when editing **_check_images.py_**, will likely result in syntax errors. 

Be aware that using the _tab_ key within most text editors might not guarentee the proper 4 space indention.  Additionally, not all text editors (including the **_Lab Workspace_**) provide the proper 4 space indention as is used in the python programs within the repository for this lab.
&nbsp;     
&nbsp;    
    
## Formatting Print Statements
Beginning with the solutions video for **_10. Creating Pet Image Labels_** you will notice that the _%_ symbol has been used within the print statements to allow for a formated print statement using the _old-style_ of print formatting. Learning more about print formatting allows for nicer appearing output, but is not a requirement of this lab. 

One can learn more about formatting one's print statements using: 
* [_New-style_ of Print Formatting](https://docs.python.org/3/library/string.html#format-string-syntax) 
* [_Old-style_ of Print Formatting](https://docs.python.org/2/library/stdtypes.html#string-formatting)
* [printing_results.py](https://github.com/udacity/AIPND/blob/master/intropylab-classifying-images/printing_results.py) - provides examples of both styles of print formatting
&nbsp;     
&nbsp;        
       
## Replacing Pass Statements
When editing the functions provided in **_check_images.py_** you will need to replace the [_pass_](https://docs.python.org/3/tutorial/controlflow.html#pass-statements) statement with your code for that function. The pass statement does nothing, it's used so that the program will still run eventhough the functions have not been fully defined. 
&nbsp;    
&nbsp;     
    
## Alternative Solution for **_11. Classifying Images - Part 1_**
With acknowledgement to Shawn M. of the April Cohort for pointing out that the [_in_ operation](https://docs.python.org/3/library/stdtypes.html#common-sequence-operations) also handles string comparison. This led to the discovery of a more simple solution using the [_in_ operation](https://docs.python.org/3/library/stdtypes.html#common-sequence-operations). 

The [_in_ operation](https://docs.python.org/3/library/stdtypes.html#common-sequence-operations) can be used to find exact match of a string as compared to a list of different strings. Because the classifier function _can_ return a list of terms for a classification (like _classifier label_: "dalmatian, coach dog, carriage dog"); one can use python's [split](https://docs.python.org/3/library/stdtypes.html#str.split) function to split a returned list of terms into a list using the separator _", "_. This allows the use of the [_in_ operation](https://docs.python.org/3/library/stdtypes.html#common-sequence-operations) to determine if a _pet label_ is contained as an _exact_ match to one of the _classifier label's_ terms (like _pet label_: "**_dalmatian_**" matching _classifier label_: "**_dalmatian_**, coach dog, carriage dog"). 

There are cases when a _classifier label_ term that contains at least one word that does match one of our _pet labels_ like a _classifier term_ of "tabby **_cat_**" or "egyptian **_cat_**" matching to _pet label_ "**_cat_**" or _classifier term_ of "standard **_poodle_**" matching to _pet label_ "**_poodle_**". To address these cases one can use python's [split](https://docs.python.org/3/library/stdtypes.html#str.split) function to [split](https://docs.python.org/3/library/stdtypes.html#str.split) the _classifier label_ term into multiple words and then check for matches using the [_in_ operation](https://docs.python.org/3/library/stdtypes.html#common-sequence-operations). 

To see the alternative solution look at the github program [**_alternative-to-classify_images.py_**](https://github.com/udacity/AIPND/blob/master/intropylab-classifying-images/alternative-to-classify_images.py). 
&nbsp;    
&nbsp;   
     
