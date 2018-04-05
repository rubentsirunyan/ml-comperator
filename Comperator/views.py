from flask import render_template, jsonify
import numpy as np

from estimate import Estimate, Parameters
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

@app.route('/home')


@app.route('/test/<algorithm>')
def run(algorithm):
    dt = DataCSV()
    X, y = dt.train_data()
    weights = []
    for i in y:
        if i == 1.0:
            weights.append(1)
        else:
            weights.append(1)
    eval_data = dt.eval_data()
    tgt = dt.target_data()
    est = Estimate(X, y, eval_data, tgt)
    exec("stats = est.{}(weights)".format(algorithm))  
    return render_template('diff.html', **stats)

@app.route('/tune/<algorithm>')
def tune(algorithm):
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

    gm = list(np.arange(0.01, 3.0, 0.01))
    gm.append(None)
    gm.append(0.0)
    grid = [{'alpha': np.arange(0.01, 3, 0.01), 'fit_prior': [True,False], 'binarize': gm}]
    params_test = Parameters(est=est, alg='bnb', grid=grid, weights=weights)
    return jsonify(params_test.get_best_result())