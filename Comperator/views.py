from flask import render_template
from Comperator import app
from Comperator.models import TrainingData


@app.route('/data/train')
def tain_data_pretty():
    dt = TrainingData()
    cols, data = dt.get_pretty()
    return render_template('data.html', cols=cols, data=data)