import os
import argparse

import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.ensemble import ExtraTreesClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import HistGradientBoostingClassifier

# for shell scripts
parser = argparse.ArgumentParser()
home_dir = os.getcwd()
parser.add_argument('--training_mode', default='classification', type=str,
                    help='Choose train type classification / Regression ')
parser.add_argument('--dataset', default='load_iris', type=str,
                    help='Choose dataset')
args, unknown = parser.parse_known_args()
# saving arguments
training_mode = args.training_mode
dataset_name = args.dataset

# Data Loading from shell input
exec(f'from sklearn.datasets import {dataset_name}')
exec(f'data = {dataset_name}()')

# Load data from sklearn.datasets
X = data.data
y = data.target

# Data split
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.2, random_state = 42)

# Classification training
if training_mode == 'classification':
  # model list
  model_lst = ['ExtraTreesClassifier','GradientBoostingClassifier','RandomForestClassifier','HistGradientBoostingClassifier']
  # save model's accuracy in this list
  model_acc = []

  # training data by models in list
  for model in model_lst:
    score = 0
    exec(f'score = {model}().fit(X_train,y_train).score(X_test, y_test)')
    model_acc.append(score)

  # print each model's score
  print("Classification Model Acc")
  print("=" * 45)
  for idx, model in enumerate(model_lst):
    print(f'{model} : {model_acc[idx] * 100:.2f}'.rjust(40,' '), '%')