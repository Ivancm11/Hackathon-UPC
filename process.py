import numpy as np
from joblib import load


def process(calories, carbohydrates, protein, fat, saturatedFats, salt, co2):
    model = load('model.joblib')
    return model.predict([calories, carbohydrates, protein, fat, saturatedFats, salt, co2])