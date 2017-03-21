import pandas
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.cross_validation import KFold
from sklearn import cross_validation
from pylab import scatter, show, legend, xlabel, ylabel

from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification

heart = pandas.read_csv("pc.csv")
heart.loc[heart["heartpred"]==2,"heartpred"]=1
heart.loc[heart["heartpred"]==3,"heartpred"]=1
heart.loc[heart["heartpred"]==4,"heartpred"]=1
heart["slope"] = heart["slope"].fillna(heart["slope"].median())
heart["thal"] = heart["thal"].fillna(heart["thal"].median())
heart["ca"] = heart["ca"].fillna(heart["ca"].median())
print(heart.describe())
predictors=["age","sex","cp","trestbps","chol","fbs","restecg","thalach","exang","oldpeak","slope","ca","thal"]
#predictors=["age","chol"]
alg=LogisticRegression(random_state=1)
kf=KFold(heart.shape[0],n_folds=3, random_state=1)
predictions = []
for train, test in kf:
    # The predictors we're using the train the algorithm.  Note how we only take the rows in the train folds.
    train_predictors = (heart[predictors].iloc[train,:])
    #print(train_predictors)
    # The target we're using to train the algorithm.
    train_target = heart["heartpred"].iloc[train]
    #print(train_target)
    # Training the algorithm using the predictors and target.
    alg.fit(train_predictors, train_target)
    # We can now make predictions on the test fold
    test_predictions = alg.predict(heart[predictors].iloc[test,:])
    predictions.append(test_predictions)
# The predictions are in three separate numpy arrays.  Concatenate them into one.  
# We concatenate them on axis 0, as they only have one axis.
predictions = np.concatenate(predictions, axis=0)

# Map predictions to outcomes (only possible outcomes are 1 and 0)
predictions[predictions > .5] = 1
predictions[predictions <=.5] = 0


print("Logistic Regression Result:-")
print("Accuracy = ")
print(sum(heart["heartpred"]==predictions)/len(heart["heartpred"]))



r0=[]
s0=[]
r1=[]
s1=[]


for i in range(0,len(heart)):
    if predictions[i] == 0 and heart["heartpred"][i] == 0:
        r0.append(heart["age"][i])
        s0.append(heart["chol"][i])
    elif predictions[i] == 1 and heart["heartpred"][i] == 1:
        r1.append(heart["age"][i])
        s1.append(heart["chol"][i])


scatter(r0, s0, marker='o', c='b')
scatter(r1, s1, marker='x', c='r')
xlabel('fbs')
ylabel('Cholestrol')
legend(['Healthy', 'UnHealthy'])
show()
