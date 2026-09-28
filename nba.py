#kütüphaneler
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score, roc_curve   
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier

from nba_api.stats.endpoints import leaguegamefinder


