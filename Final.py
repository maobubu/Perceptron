#!/usr/bin/python3
'''
This file contains the run function and final function
please run main.py
'''
import random
import math


def run(p, desire_output, weights, theta, learn, output_file, criteria):
    epoch = 1
    terminate = False
    while not terminate:
        p.compare(theta, learn)
        if epoch >= criteria or p.get_y() == desire_output:  # stop criteria
            weights = p.get_weight()
            terminate = True  # stop training
            print('epoch: {}'.format(epoch))
            print('epoch: {}'.format(epoch), file=output_file)
            print("final weight is ", weights)
            print("final weight is ", weights, file=output_file)
        else:
            p.get_y().clear()
        epoch += 1
    return weights


def chunkify(lst, n):  # devide a list to three parts
    return [lst[i::n] for i in range(n)]


def final(compare_list, c1, c2, c3, other, count, compare, d, output_file):
    for i in compare_list:
        compare.append(i)
        if compare[count] == tuple(d.get_test_desire()[count]) and tuple(d.get_test_desire()[count]) == (1, 0, 0):
            c1.append(count)
        elif compare[count] == tuple(d.get_test_desire()[count]) and tuple(d.get_test_desire()[count]) == (0, 1, 0):
            c2.append(count)
        elif compare[count] == tuple(d.get_test_desire()[count]) and tuple(d.get_test_desire()[count]) == (0, 0, 1):
            c3.append(count)
        else:
            other.append(count)
        count += 1
    print(" final testing output:\n(1,0,0) represent Iris-setosa\n(0,1,0)represent Iris-versicolor\n"
          "(0,0,1) represents Iris-virginica\nOther combination represents other\nFinal ouput:\n", compare)
    print(" final testing output:\n(1,0,0) represent Iris-setosa\n(0,1,0)represent Iris-versicolor\n"
          "(0,0,1) represents Iris-virginica\nOther combination represents other\nFinal output:\n", compare,
          file=output_file)
    print('Vectors that are not as the combination mentioned above will be randomly classified as one of the 3 classes')
    print('Vectors that are not as the combination mentioned above will be randomly classified as one of the 3 classes',file=output_file)
    # TODO randomly select from other
    random.shuffle(other)  # shuffle the list:other
    chunk = chunkify(other, 3)  # split into evenly parts and add to c1,c2,c3
    c1.extend(chunk[0])
    c2.extend(chunk[1])
    c3.extend(chunk[2])
    mol_1 = list(filter(lambda x: x < len(d.get_final_class()) / 3, c1))  # find certain class 1
    mol_2 = list(filter(lambda x: len(d.get_final_class()) / 3 <= x < 2 * len(d.get_final_class()) / 3, c2))
    mol_3 = list(filter(lambda x: 2 * len(d.get_final_class()) / 3 <= x < len(d.get_final_class()), c3))

    ##TODO for Iris-setosa
    print("\nClassified as Iris-setosa:")
    print("\nClassified as Iris-setosa:", file=output_file)
    if not c1:  # execute when c1 is empty
        print('None of them have been classified to Iris-setosa\n')
        print('None of them have been classified to Iris-setosa\n', file=output_file)
    for i in c1:
        print(d.get_final_class()[i])
        output_file.write(d.get_final_class()[i])
        ##TODO for Iris-versicolor
    print("\nClassified as Iris-versicolor:")
    print("\nClassified as Iris-versicolor:", file=output_file)
    if not c2:
        print('None of them have been classified to Iris-versicolor\n')
        print('None of them have been classified to Iris-versicolor\n', file=output_file)
    for i in c2:
        print(d.get_final_class()[i])
        output_file.write(d.get_final_class()[i])
        ##TODO for Iris-virginica
    print("\nClassified as Iris-virginica:")
    print("\nClassified as Iris-virginica:", file=output_file)
    if not c3:
        print('None of them have been classified to Iris-virginica\n')
        print('None of them have been classified to Iris-virginica\n', file=output_file)
    for i in c3:
        print(d.get_final_class()[i])
        output_file.write(d.get_final_class()[i])
        ##TODO add precision and recall,error,sum square error
    print('The precision and recall\n')
    print('The precision and recall\n', file=output_file)
    pre1, pre2, pre3 = len(mol_1) / len(c1), len(mol_2) / len(c2), len(mol_3) / len(
        c3)  # the Precision is definitely one because it only classify as a certain class when the output vector
    # exactly matches, +1 is to avoid the division being 0
    re1, re2, re3 = len(mol_1) / (len(d.get_final_class()) / 3), len(mol_2) / (len(d.get_final_class()) / 3), len(
        mol_3) / (len(
        d.get_final_class()) / 3)
    re1 = math.floor(re1) if re1 > 1 else re1  # floor to make sure smaller than 1
    re2 = math.floor(re2) if re2 > 1 else re2
    re3 = math.floor(re3) if re3 > 1 else re3
    sum_error = len(c1) - len(mol_1) + len(c2) - len(mol_2) + len(c3) - len(mol_3)  # sum squared error
    accuracy = (sum_error / len(d.get_final_class())) * 100  # classfication error in percent
    if not c1:  # execute when c1 is empty
        print('None of them have been classified to Iris-setosa\n')
        print('None of them have been classified to Iris-setosa\n', file=output_file)
    else:
        print('Class one Iris-setosa:\nPrecision:{}\nRecall:{}\n'.format(pre1, re1))
        print('Class one Iris-setosa:\nPrecision:{}\nRecall:{}\n'.format(pre1, re1), file=output_file)
    if not c2:
        print('None of them have been classified to Iris-versicolor\n')
        print('None of them have been classified to Iris-versicolor\n', file=output_file)
    else:
        print('Class two Iris-versicolor:\nPrecision:{}\nRecall:{}\n'.format(pre2, re2))
        print('Class two Iris-versicolor:\nPrecision:{}\nRecall:{}\n'.format(pre2, re2), file=output_file)
    if not c3:
        print('None of them have been classified to Iris-virginica\n')
        print('None of them have been classified to Iris-virginica\n', file=output_file)
    else:
        print('Class three Iris-virginica:\nPrecision:{}\nRecall:{}\n'.format(pre3, re3))
        print('Class three Iris-virginica:\nPrecision:{}\nRecall:{}\n'.format(pre3, re3), file=output_file)
    print('Sum squared error is {}\n'.format(sum_error))
    print('Sum squared error is {}\n'.format(sum_error), file=output_file)
    print('The Classification Error is {}%\n'.format(accuracy))
    print('The Classification Error is {}%\n'.format(accuracy), file=output_file)
    print('''The Precision and Recall by using Weka Tool:
    Class Iris-setosa:          Precision: 1.000  Recall: 1.000
    Class Iris-versicolor:      Precision :0.769 Recall: 1.000
    Class Iris-verginica:       Precision: 1.000 Recall: 0.700
    Classification Error is:                 90%
    Mean absolute error                      0.132 
    Root mean squared error                  0.256 
    Relative absolute error                 29.7109 %
    Root relative squared error             54.3162 %
    Total Number of Instances               30
    ''')
    print('''The Precision and Recall by using Weka Tool:
    Class Iris-setosa:          Precision: 1.000  Recall: 1.000
    Class Iris-versicolor:      Precision :0.769 Recall: 1.000
    Class Iris-verginica:       Precision: 1.000 Recall: 0.700
    Classification Error is:                 90%
    Mean absolute error                      0.132 
    Root mean squared error                  0.256 
    Relative absolute error                 29.7109 %
    Root relative squared error             54.3162 %
    Total Number of Instances               30
    ''', file=output_file)
