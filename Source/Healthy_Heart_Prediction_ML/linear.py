import pandas
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.cross_validation import KFold
heart = pandas.read_csv("pc.csv")
heart.loc[heart["heartpred"]==2,"heartpred"]=1
heart.loc[heart["heartpred"]==3,"heartpred"]=1
heart.loc[heart["heartpred"]==4,"heartpred"]=1
heart["slope"] = heart["slope"].fillna(heart["slope"].median())
heart["thal"] = heart["thal"].fillna(heart["thal"].median())
heart["ca"] = heart["ca"].fillna(heart["ca"].median())
print(heart.describe())
predictors=["age","sex","cp","trestbps","chol","fbs","restecg","thalach","exang","oldpeak","slope","ca","thal"]
alg=LinearRegression()
kf=KFold(heart.shape[0],n_folds=3, random_state=1)
predictions = []
for train, test in kf:
    train_predictors = (heart[predictors].iloc[train,:])
    train_target = heart["heartpred"].iloc[train]
    alg.fit(train_predictors, train_target)
    test_predictions = alg.predict(heart[predictors].iloc[test,:])
    predictions.append(test_predictions)
predictions = np.concatenate(predictions, axis=0)


predictions[predictions > .5] = 1
predictions[predictions <=.5] = 0
i=0
count=0
for each in heart["heartpred"]:
    if each==predictions[i]:
        count+=1
    i+=1
accuracy=count/i
print("Linear Regression Result:-")
print("Accuracy = ")
print(accuracy*100)