from flask import render_template
from sklearn.neighbors import KNeighborsClassifier
from Comperator import app
from Comperator.models import TrainingData, DataCSV


@app.route('/data/train/<limit>')
def tain_data_pretty(limit):
    dt = TrainingData()
    cols, data = dt.get_pretty(limit)
    return render_template('data.html', cols=cols, data=data)

@app.route('/run/knn')
def run():
    dt = DataCSV()
    features, labels = dt.train_data()
    clf = KNeighborsClassifier(10)
    clf = clf.fit(features, labels)
    eval_data = dt.eval_data()
    result = clf.predict(eval_data)
    return render_template('diff.html', data=zip(result, dt.target_data()))