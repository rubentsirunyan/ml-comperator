from flask import render_template
import numpy as np

from sklearn import metrics
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC
from sklearn.naive_bayes import GaussianNB, BernoulliNB
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import RandomForestClassifier
from Comperator import app
from Comperator.models import TrainingData, DataCSV
from sklearn.model_selection import ParameterGrid

def mn(x,y):
    return (float(x) + float(y)) / 2.0

def perc(x, y):
    return float(x) / float(y) + 100.0



@app.route('/test/')
def run():
    dt = DataCSV()
    X, y = dt.train_data()
    weights = []
    for i in y:
        if i == 1.0:
            weights.append(10)
        else:
            weights.append(1)
    eval_data = dt.eval_data()
    tgt = dt.target_data()
    # gm = list(np.arange(0.1, 1.5, 0.1))
    # gm.append("auto")
    # grid = [{'C': np.arange(0.1, 4, 0.1), 'kernel': ['rbf'],'gamma':gm}]
    clf = SVC()
    clf.fit(X, y, weights)
    prediction = clf.predict(eval_data)
    zip_lists = zip(tgt, prediction)
    accuracy =  metrics.accuracy_score(tgt, prediction) * 100.0
    diff = sum(1 for i, j in zip_lists if i != j)
    all_positives = sum(1 for i in tgt if i == 1.0)
    true_positive = sum(1 for i, j in zip_lists if i == 1.0 and j == 1.0)
    false_positive = sum(1 for i, j in zip_lists if i == 0.0 and j == 1.0)
    false_negative = all_positives - true_positive
    true_negative = len(tgt) - all_positives - false_positive
    error = float(diff) / float(len(zip_lists)) * 100.0
    return render_template('diff.html', 
                            diff=diff,
                            length=len(zip_lists),
                            data=zip_lists, 
                            error=error,
                            accuracy=accuracy,
                            all_positives=all_positives,
                            true_positive=true_positive,
                            false_positive=false_positive,
                            false_negative=false_negative,
                            true_negative=true_negative)

    
    # best = {}
    # best_score = 0
    # for i in ParameterGrid(grid):
    #     clf = SVC(**i)
    #     clf.fit(X, y, weights)
    #     prediction = clf.predict(eval_data)
    #     ac =  metrics.accuracy_score(tgt, prediction) * 100.0
    #     cor = sum(1 for i, j in zip(tgt, prediction) if i==1.0 and j == 1.0)
    #     al = sum(1 for i in tgt if i ==1.0)
    #     if metrics.f1_score(tgt, prediction) > best_score:
    #         best_score = metrics.f1_score(tgt, prediction)
    #         best = i
    #     print "###############"
    #     print i
    #     print cor, "From", al
    #     print "Acuracy: ", ac
    #     print metrics.accuracy_score(tgt, prediction)
    #     print metrics.precision_score(tgt, prediction)
    #     print metrics.f1_score(tgt, prediction)
    # print "$$$$$$$$$$$$$"
    # print best , best_score

