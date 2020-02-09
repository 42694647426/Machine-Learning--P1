# -*- coding: utf-8 -*-


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from math import exp
from sklearn.model_selection import train_test_split

class log_regression:
    
    def __init__(self, rate, gradient_iter):
        self.rate = rate
        self.gradient_iter = gradient_iter
        
    def bias(self, X):
        return np.insert(X, 0,1,axis=1)
    
    def log(self, z):
        return 1/(1+np.exp(-z))
    
    def loss (self, y_predict, y_real):
        return (-y_real*np.log(y_predict)-(1-y_real)* np.log(1 - y_predict)).mean()
        
    def predict_prob(self, X, features):
        X = self.bias(X)
        return np.array(self.log(np.dot(X,features)))
    
    def predict(self, X, feature, threshold =0.5):
        return self.predict_prob(X, feature) >=threshold
        
    def fit(self, X, Y):
        rate = self.rate
        iter = self.gradient_iter
        X = self.bias(X)
        feature=[0]*X.shape[1]
        
        for i in iter :
            y_predict = self.predict_prob(X, feature)
            grad = np.dot(X.T, (y_predict - Y))/Y.shape[0]
            feature = feature - rate*grad
        
        return feature

    def evaluate_acc(realY, predictY):
        return sum((realY-predictY)**2)
