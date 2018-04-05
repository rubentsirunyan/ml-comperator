from flask import render_template
import numpy as np

from estimate import Estimate
from Comperator import app
from Comperator.models import TrainingData, DataCSV
from sklearn.model_selection import ParameterGrid

def mn(x,y):
    return (float(x) + float(y)) / 2.0

def perc(x, y):
    return float(x) / float(y) + 100.0

@app.route('/data/train/<limit>')
def tain_data_pretty(limit):
    dt = TrainingData()
    cols, data = dt.get_pretty(limit)
    return render_template('data.html', cols=cols, data=data)


@app.route('/test/<algorithm>')
def run(algorithm):
    dt = DataCSV()
    X, y = dt.train_data()
    weights = []
    for i in y:
        if i == 1.0:
            weights.append(5)
        else:
            weights.append(1)
    eval_data = dt.eval_data()
    tgt = dt.target_data()
    est = Estimate(X, y, eval_data, tgt)
    exec("stats = est.{}(weights)".format(algorithm))

    # gm = list(np.arange(0.1, 1.5, 0.1))
    # gm.append("auto")
    # grid = [{'C': np.arange(0.1, 4, 0.1), 'kernel': ['rbf'],'gamma':gm}]
        
    # elif algorithm == 'gnb':
    #     clf = GaussianNB()
    #     clf.fit(X, y, weights)        
    # elif algorithm == 'bnb':
    #     clf = BernoulliNB()
    #     clf.fit(X, y, weights)        
    # elif algorithm == 'mnb':
    #     clf = MultinomialNB()
    #     clf.fit(X, y, weights)        
    
    
    return render_template('diff.html', **stats)
    
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

