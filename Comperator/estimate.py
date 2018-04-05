from sklearn import metrics
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC
from sklearn.naive_bayes import  GaussianNB, BernoulliNB, MultinomialNB
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import RandomForestClassifier
from Comperator import app
from Comperator.models import TrainingData, DataCSV
from sklearn.model_selection import ParameterGrid


class Estimate():

    def __init__(self, X, y, evl, tgt):
        self.X = X
        self.y = y
        self.evl = evl
        self.tgt = tgt


    def svc(self, weights):
        self.weights = weights
        self.clf = SVC()
        self.clf.fit(self.X, self.y, self.weights)
        self.prediction = self.clf.predict(self.evl)
        self.stats = AnalyseResult(self.prediction, self.tgt).stats()
        return self.stats

    def bnb(self, weights):
        self.weights = weights
        self.clf = BernoulliNB()
        self.clf.fit(self.X, self.y, self.weights)
        self.prediction = self.clf.predict(self.evl)
        self.stats = AnalyseResult(self.prediction, self.tgt).stats()
        return self.stats    

class AnalyseResult():

    def __init__(self, prediction, tgt):
        self.prediction = prediction
        self.tgt = tgt

    def stats(self):
        self.zip_lists = zip(self.tgt, self.prediction)
        self.accuracy =  metrics.accuracy_score(self.tgt, self.prediction) * 100.0
        self.diff = sum(1 for i, j in self.zip_lists if i != j)
        self.all_positives = sum(1 for i in self.tgt if i == 1.0)
        self.true_positive = sum(1 for i, j in self.zip_lists if i == 1.0 and j == 1.0)
        self.false_positive = sum(1 for i, j in self.zip_lists if i == 0.0 and j == 1.0)
        self.false_negative = self.all_positives - self.true_positive
        self.true_negative = len(self.tgt) - self.all_positives - self.false_positive
        self.error_perc = float(self.diff) / float(len(self.zip_lists)) * 100.0
        return {
            "data": self.zip_lists,
            "accuracy": self.accuracy,
            "diff": self.diff,
            "error_perc": self.error_perc,
            "all_positives": self.all_positives,
            "true_positive": self.true_positive,
            "false_positive": self.false_positive,
            "true_negative": self.true_negative,
            "false_negative": self.false_negative,            
        }
           