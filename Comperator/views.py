from flask import render_template
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cluster import KMeans

from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB, MultinomialNB, BernoulliNB
from sklearn.mixture import GaussianMixture
from Comperator import app
from Comperator.models import TrainingData, DataCSV


@app.route('/data/train/<limit>')
def tain_data_pretty(limit):
    dt = TrainingData()
    cols, data = dt.get_pretty(limit)
    return render_template('data.html', cols=cols, data=data)

@app.route('/run/<algorithm>')
def run(algorithm):
    dt = DataCSV()
    features, labels = dt.train_data()
    if algorithm == "knn":
        clf = KNeighborsClassifier(10)
    elif algorithm == "km":
        clf = KMeans(2)
    elif algorithm == "nn":
        clf = MLPClassifier(solver='lbfgs', alpha=1e-5,
                            hidden_layer_sizes=(5, 2), random_state=1)
    elif algorithm == "svc":
        clf = SVC()
    elif algorithm == "gnb":
        clf = GaussianNB()
    elif algorithm == "mnb":
        clf = MultinomialNB()
    elif algorithm == "bnb":
        clf = BernoulliNB()
    elif algorithm == "gm":
        clf = GaussianMixture()
    clf = clf.fit(features, labels)
    eval_data = dt.eval_data()
    result = clf.predict(eval_data)
    zip_lists = zip(result, dt.target_data())
    diff = sum(1 for i, j in zip_lists if i != j)
    error = float(diff) / float(len(zip_lists)) * 100.0
    return render_template('diff.html', 
                            diff=diff,
                            length=len(zip_lists),
                            data=zip_lists, 
                            error=error)