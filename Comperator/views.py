from Comperator import app
from Comperator.models import TrainingData

@app.route('/')
def home():
    a = TrainingData()
    asd = a.get_pretty()
    return ','.join(asd)