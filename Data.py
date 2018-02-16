#!/usr/bin/python3
'''
This file contains the class Data and function arrange_train
arrange_Test, label ,split desire etc
please run main.py
'''
class Data:
    def __init__(self, train, test, output):
        self._train_in = train
        self._test_in = test
        self._out = output
        self._x_new = []
        self._desire_new = []
        self._test_new = []
        self._test_desire = []
        self._final = []

    def arrange_train(self):
        ##TODO transfer each line of the txt file into a list including x and label
        for line in self._train_in:
            train_out = line.rstrip().split(',')
            self._desire_new.append(self.label(train_out))  # add the desire output to a list
            train_out.pop()  # delete the labels # and appended into a list
            train_out = list(map(float, train_out))
            self._x_new.append(train_out)  # append each list to a new list.

    def arrange_test(self):
        for line in self._test_in:
            test_out = line.rstrip().split(',')
            self._final.append(line)
            self._test_desire.append(self.label(test_out))  # add the desire output to a list
            test_out.pop()  # delete the labels # and appended into a list
            test_out = list(map(float, test_out))
            self._test_new.append(test_out)  # append each list to a new list.

    def label(self, label_list):
        ##TODO transform the strings to vectors.
        if label_list[4] == 'Iris-setosa':
            label_list[4] = [1, 0, 0]

        elif label_list[4] == 'Iris-versicolor':
            label_list[4] = [0, 1, 0]

        elif label_list[4] == 'Iris-virginica':
            label_list[4] = [0, 0, 1]
        return label_list[4]


    def split_desire(self, desire):
        # TODO split the desire output
        d1 = [int(l[0]) for l in desire]
        d2 = [int(l[1]) for l in desire]
        d3 = [int(l[2]) for l in desire]
        dic = dict(first=d1, second=d2, third=d3)  # add to the dictionary
        return dic

    def get_x(self):
        return self._x_new

    def get_desire(self):
        return self._desire_new

    def get_test_desire(self):
        return self._test_desire

    def get_test_new(self):
        return self._test_new

    def get_final_class(self):
        return self._final
