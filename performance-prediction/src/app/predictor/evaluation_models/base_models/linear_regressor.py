import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.impute import SimpleImputer
import matplotlib.pyplot as plt
from src.app.predictor.contracts.model import Model

class LinearRegressor(Model):
    def __init__(self, filepath):
        super().__init__(filepath)

    def create_model(self):
        return LinearRegression()

    
        