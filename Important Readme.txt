Created on 25-Jan-2018
@author: Huicheng Liu
This is the main code, please run it to execute the code.
requirements: Python3, Python3.6.3 is prefered(Doesn't work on Python2). My code doesn't include any library, all the import file are wrote by myself which contains class and functions, the only dependent import is "math" and "random" that includes in python3 so there shouldn't be any problem running the code. 
Run the code "main" code simply through the python IDLE,VSCODE,VISUAL STUDIO, pycharm or even through the command line on Mac and Linux by typing "python3 main.py". The input file is "train.txt" and "test.txt" which are from onQ, the output file "Final_output_result.txt" contains all the information including epoch(iteration time), initial weight, final weight, classify result, precision, recall, classfication error, the results using Weka tool etc.
You can change the learning rate and epoch or initial weight to get different results. A single input vector will be classified as class one if the desire output is(1,0,0),class two if (0,1,0), class three if (0,0,1),if the desire output doesn't satisfy any of the vector listed above, then it will be randomly classified as one of the three classes.
The best Result I got is about 80% accuracy!
The folder "Weka tool implement" contains the informations by using the tool Weka.
the folder"__pycache__" is the cache after running the code.
Please contact me if there are any problems email:  17hl7@queensu.ca
