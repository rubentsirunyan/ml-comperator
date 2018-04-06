from flask import render_template, jsonify, request
import numpy as np

from Comperator.estimate import Estimate, Parameters
from Comperator import app
from Comperator.models import TrainingData, DataCSV


@app.route('/data/train/')
def tain_data_pretty():
    dt = DataCSV()
    cols, data = dt.get_train_pretty()
    return render_template('data.html', 
                           desc="train",
                           cols=cols,
                           data=data)

@app.route('/data/test/')
def test_data_pretty():
    dt = DataCSV()
    cols, data = dt.get_test_pretty()
    return render_template('data.html',
                           desc="test", 
                           cols=cols, 
                           data=data)


@app.route('/')
@app.route('/home')
def home():
    method_list = [func for func in dir(Estimate) if callable(getattr(Estimate, func)) and not func.startswith("__")]
    return render_template('home.html', methods=method_list)

@app.route('/test/<algorithm>',methods=['GET', 'POST'])
def run(algorithm):
    dt = DataCSV()
    X, y = dt.train_data()
    w = request.args.get("paramselect")
    print(w)
    weights = []
    for i in y:
        if i == 1.0:
            weights.append(int(w))
        else:
            weights.append(1)
    eval_data = dt.eval_data()
    tgt = dt.target_data()
    cols, pretty_data = dt.get_test_pretty()
    est = Estimate(X, y, eval_data, tgt)
    if algorithm == 'knn':
        stats = eval("est.{}(w)".format(algorithm))
    else:
        stats = eval("est.{}(weights)".format(algorithm))
    stats['cols'] = cols
    stats['data'] = zip(pretty_data,stats['data'])
    return render_template('diff.html',alg=algorithm, **stats)

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