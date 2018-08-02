#!/usr/bin/python3
'''
Created on 25-Jan-2018
@author: Huicheng Liu
This is the main code, please run it to execute the code.
requirements: Python3, Python3.6.3 is prefered.(Doesn't work on Python2) My code doesn't include any library, all the import file
are wrote by myself which contains class and functions ,the only dependent import is "math" and "random" that includes
in python3 so there shouldn't be any problem running the code.
Run the code "main" code simply through the python IDLE,VSCODE,VISUAL STUDIO pycharm or even through the command line on Mac and Linux by typing
"python3 main.py". The input file is "train.txt" and "test.txt" which are from onQ, the output file "Final_ouput_result.txt"
contains all the information including epoch(iteration time), initial weight, final weight, classify result, precision, recall
You can change the learning rate and epoch or initial weight to get different results. A single input vector will be classified
as class one if the desire output is(1,0,0),class two if (0,1,0), class three if (0,0,1),if the desire output doesn't satisfy
any of the vector listed above, then it will be randomly classified as one of the three classes.
The best Result I got is about 80% accuracy!
The folder "Weka tool implement" contains the informations by using the tool Weka.
the folder"__pycache__" is the cache after running the code.
---------------------------------------------
'''
print("This is a perceptron algorithm\nauthor: Huicheng Liu\nDate:1/22/2018")
# BEGIN : variable declaration
import Data as dt
import Perceptron as Pn
import Final as fn

learning_rate = 0.05  # the learning rate
epoch = 500  # stop criteria iteration time or 1000
weights_1 = [1, 0, 0, 0, 0]  # a list of the initial weights, node 1, first element is the W0,threshold
weights_2 = [-4, 0, 0, 0, 0]  # a list of the initial weights, node 2
weights_3 = [1, 0, 0, 0, 0]  # a list of the initial weights, node 3
test_l1, test_l2, test_l3 = [], [], []
bias = 1
theta = 0  # the threshold theta
train_file = open('train.txt', 'r')
test_file = open('test.txt', 'r')

    


def main():
    try:
        output_file = open('Final_output_result.txt', 'w')
        print('start:\nlearning rate has been set to:{}\nstop criteria'
          ' has been set to:{}\nbias has been set to:{}'.format(learning_rate, epoch, bias))
        print('start:\nlearning rate has been set to:{}\nstop criteria'
          ' has been set to:{}\nbias has been set to:{}'.format(learning_rate, epoch, bias), file=output_file)
        d = dt.Data(train_file, test_file, output_file)
    ##TODO training phase
        d.arrange_train()
        d_final = d.split_desire(d.get_desire())  # a dictionary that contains all the desire output
        p1 = Pn.Perceptron(weights_1, d_final['first'], d.get_x())  # first:weights,second:desire output
        p2 = Pn.Perceptron(weights_2, d_final['second'], d.get_x())  # third: input
        p3 = Pn.Perceptron(weights_3, d_final['third'], d.get_x())
        print("\nthe first node:\nthe initial weight is:{}".format(weights_1))
        print("\nthe first node:\nthe initial weight is:{}".format(weights_1), file=output_file)
        weights_test1 = fn.run(p1, d_final['first'], weights_1, theta, learning_rate, output_file, epoch)
        print("\nthe second node:\nthe initial weight is:{}".format(weights_2))
        print("\nthe second node:\nthe initial weight is:{}".format(weights_2), file=output_file)
        weights_test2 = fn.run(p2, d_final['second'], weights_2, theta, learning_rate, output_file, epoch)
        print("\nthe third node:\nthe initial weight is:{}".format(weights_3))
        print("\nthe third node:\nthe initial weight is:{}".format(weights_3), file=output_file)
        weights_test3 = fn.run(p3, d_final['third'], weights_3, theta, learning_rate, output_file, epoch)
    ##TODO Testing phase
        d.arrange_test()
        d_test = d.split_desire(d.get_test_desire())  # a dictionary that contains all the desire output
        t1 = Pn.Perceptron(weights_test1, d_test['first'], d.get_test_new())
        t2 = Pn.Perceptron(weights_test2, d_test['second'], d.get_test_new())
        t3 = Pn.Perceptron(weights_test3, d_test['third'], d.get_test_new())
        t1.test(theta, test_l1)
        print('\n Node One, Node Two, Node Three true output')
        print('\n Node One, Node Two, Node Three true output', file=output_file)
        print("One:", test_l1)
        print("One:", test_l1, file=output_file)
        t2.test(theta, test_l2)
        print("Two:", test_l2)
        print("Two:", test_l2, file=output_file)
        t3.test(theta, test_l3)
        print("Three:", test_l3)
        print("Three:", test_l3, file=output_file)
        compare_list = zip(test_l1, test_l2, test_l3)
        c1, c2, c3, other, count, compare = [], [], [], [], 0, []
        fn.final(compare_list, c1, c2, c3, other, count, compare, d, output_file)
    except IOError:
        print('File error')
    finally:
        output_file.close()


if __name__ == "__main__": main()
