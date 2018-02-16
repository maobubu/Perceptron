#!/usr/bin/python3
#This file contains the Class Perceptron and compare function
#modify weight function, test function
#please run main.py
class Perceptron:  # This is one node, there are total three nodes
    def __init__(self, w, desire, x_com):
        self._y = list()  # output y
        self._weight = w  # weight
        self._desire = desire  # desire out put
        self._x_com = x_com

    def compare(self, th, learning):
        ##TODO compare the true out put and desire output
        t, c = 0, 0
        for x_i in self._x_com:
            x_i.insert(0, 1)  # x0=1, add bias =1 to the beginning of list x_com
            net_x = sum(i * j for i, j in zip(self._weight, x_i))  # calculate the dot product
            # for f, j in zip(self._weight, x_i):
            ##print('w{}= {}, x{}= {}'.format(c, f, c, j))
            # c += 1
            ##print('Net_x is :{}-------'.format(net_x))  # w0*x0+w1*x1....
            y = 1 if net_x > th else 0  # bigger than threshold,fire
            self.modify_weight(self._desire[t], learning, y, x_i)  # modify the weight
            t += 1
            x_i.pop(0)  # delete the x0 from x_i
            self._y.append(y)

    def modify_weight(self, desire_op, learn, y, x):
        ##TODO modify the weight
        ##TODO upate the wights, w(t+1) = w(t) + learningRate * (d-y) * x
        if desire_op > y:  # if desire bigger than true
            u = 1
        elif desire_op < y:
            u = -1  # if desire smaller than true
        else:
            u = 0
        self._weight = [i + learn * u * j for i, j in zip(self._weight, x)]  # I'm wrong not wrong

    def test(self, th, list1):
        # TODO use the testing data to test the neural network
        for x_i in self._x_com:
            x_i.insert(0, 1)  # add bias to the data
            net_x = sum(i * j for i, j in zip(self._weight, x_i))  # calculate the dot product
            y = 1 if net_x > th else 0  # bigger than threshold,fire
            list1.append(y)
            x_i.pop(0)  # delete the x0 from x_i

    def get_y(self):  # return the output y
        return self._y

    def get_weight(self):  # return the output y
        return self._weight
