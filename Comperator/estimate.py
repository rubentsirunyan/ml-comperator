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
        self.params = {'binarize': 1.0, 'alpha': 0.23, 'fit_prior': True}
        self.weights = weights
        self.clf = BernoulliNB(**self.params)
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
            "prediction": self.prediction,
            "tgt": self.tgt,
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
           
class Parameters():
    def __init__(self,est, alg, grid, weights=None):
        self.est = est
        self.alg = alg
        self.grid = grid
        self.weights = weights


    def get_best_result(self):
        self.best_precision = {}
        self.best_precision_score = 0
        self.best_precision_ac = 0
        self.best_precision_tp = 0
        self.best_f1 = {}
        self.best_f1_score = 0
        self.best_f1_ac = 0
        self.best_f1_tp = 0
        for i in ParameterGrid(self.grid):
            exec("self.res = self.est.{}(self.weights, i)".format(self.alg))
            self.tgt = self.res['tgt']
            self.prediction = self.res['prediction']
            self.accuracy =  metrics.accuracy_score(self.tgt, self.prediction) * 100.0
            self.tp = sum(1 for i, j in zip(self.tgt, self.prediction) if i==1.0 and j == 1.0)
            self.ap = sum(1 for i in self.tgt if i ==1.0)
            if metrics.f1_score(self.tgt, self.prediction) > self.best_f1_score:
                self.best_f1_score = metrics.f1_score(self.tgt, self.prediction)
                self.best_f1 = i
                self.best_f1_tp = self.tp
                self.best_f1_ac = self.accuracy
            if metrics.precision_score(self.tgt, self.prediction) > self.best_precision_score:
                self.best_precision_score = metrics.precision_score(self.tgt, self.prediction)
                self.best_precision = i
                self.best_precision_ac = self.accuracy
                self.best_precision_tp = self.tp
        #     print "###############"
        #     print i
        #     print "Acuracy: ", self.accuracy
        #     print self.tp, "From", self.ap
        #     print metrics.precision_score(self.tgt, self.prediction)
        #     print metrics.f1_score(self.tgt, self.prediction)
        # print "$$$$$$$$$$$$$"
        self.dct = {
            "Best F1 Score": self.best_f1,
            "With score": self.best_f1_score,
            "Best F1 TP" : self.best_f1_tp, 
            "Best F1 Accuracy": self.best_f1_ac,
            "Best precision Score": self.best_precision,
            "With score": self.best_precision_score,
            "Best precision Accuracy": self.best_precision_ac,
            "Best precision TP": self.best_precision_tp
        }
        # print "Best F1 Score: ", self.best_f1 
        # print "With score: ", self.best_f1_score
        # print "Best precision Score: ", self.best_precision
        # print "With score: ", self.best_precision_score
        return self.dct
