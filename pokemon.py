import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score, train_test_split
import argparse

"""
Gotcha Catch'em All!
This Program brings the cartoon version
of Pokedex to real life.

Here with the application of Machine
Learning we try to identify the Pokemon
based upon the parameters that we specify
"""

def get_args():
    parser = argparse.ArgumentParser(description='For the Pokemon Trainers.')
    parser.add_argument('-hp',type=int,help='Health Points of the Pokemon',required=True)
    parser.add_argument('-atk',type=int,help='Attack Points of the Pokemon',required=True)
    parser.add_argument('-dfs',type=int,help='Defense Points of the Pokemon',required=True)
    parser.add_argument('-satk',type=int,help='Special Attack Points',required=True)    
    parser.add_argument('-sdef',type=int,help='Special Attack Points',required=True)    
    parser.add_argument('-speed',type=int,help='Speed of the Pokemon',required=True)
    args = parser.parse_args()
    return [args.hp,args.atk,args.dfs,args.satk,args.sdef,args.speed]

"""
@params:
  hp : Health Points of the Pokemon
  atk : Attack Points of the Pokemon
  dfs : Defensive Points of the Pokemon
  satk : Special Attack Points of the Pokemon
  sdef : Special Defense Points of the Pokemon
  speed : Speed attribute of the Pokemon
@params over
"""

args = get_args()

"""
Reading the CSV file containing the data set.
The data set can be downloaded from :- (https://www.kaggle.com/abcsds/pokemon)
"""    
df = pd.read_csv("D:\Pokemon.csv", low_memory=False)
le = preprocessing.LabelEncoder()


x = df.drop(['#','Name','Type 1','Type 2','Total','Generation','Legendary'], axis=1)
y = df['Type 1']
z = df['Generation']
w = df['Legendary']

"""
'y' determines the Type of the Pokemon.
'z' determines the Generation of the Pokemon.
'w' determines the Legendary Characteristic of the Pokemon
"""

x_train, __, y_train, __ = train_test_split(x, y, test_size=0.2)
x_train, __, z_train, __ = train_test_split(x, z, test_size=0.2)
x_train, __, w_train, __ = train_test_split(x, w, test_size=0.2)


clfy = RandomForestClassifier(min_impurity_split=0.1, n_jobs = -1, max_depth=15)
clfz = RandomForestClassifier(min_impurity_split=0.1, n_jobs = -1, max_depth=15)
clfw = RandomForestClassifier(min_impurity_split=0.1, n_jobs = -1, max_depth=15)


scorey = cross_val_score(clfy, x, y, cv=5)
scorez = cross_val_score(clfz, x, z, cv=12)
scorez = cross_val_score(clfz, x, z, cv=15)


clfy = clfy.fit(x,y)
clfz = clfz.fit(x,z)
clfw = clfw.fit(x,w)

"""
creating the temp list and converting 
it to a numpy array so that th array 
can be reshaped.

Reshaping is done because the data 
contains a single sample.

For more reference : 
https://stackoverflow.com/questions/35082140/preprocessing-in-scikit-learn-single-sample-depreciation-warning
"""

temp = np.array(args)
temp = temp.reshape(1,-1)


pred_type = clfy.predict(temp)
pred_gen = clfz.predict(temp)
pred_leg = clfw.predict(temp)

"""
Printing the Prediction.
"""

print "<---------PREDICTION--------->"
print "Pokemon Type is : ", pred_type[0]
print "Generation: ",pred_gen[0]
print "Legendary: ",pred_leg[0]
print "<---------------------------->"
