import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import pickle

# Reading Data
file_path = 'mushrooms.csv'
mushroom_data = pd.read_csv(file_path)

# Data Preparation
mushroom_data.columns = mushroom_data.columns.str.lower().str.replace(r'\W', '_', regex=True)
selected_columns = ['odor', 'ring_type', 'stalk_surface_above_ring', 'gill_color', 'stalk_surface_below_ring', 'class']
selected_data = mushroom_data[selected_columns]

# Split the data
train_data, test_data = train_test_split(selected_data, test_size=0.25, random_state=42)
X_train = train_data.drop(['class'], axis=1)
y_train = train_data['class']
X_test = test_data.drop(['class'], axis=1)
y_test = test_data['class']

# Encoding
categorical_features = X_train.columns
column_transformer = ColumnTransformer([("encoder", OneHotEncoder(), categorical_features)], remainder='passthrough')
X_train_encoded = column_transformer.fit_transform(X_train)
X_test_encoded = column_transformer.transform(X_test)

# Training the RandomForestClassifier
rf_model = RandomForestClassifier(random_state=42)
rf_model.fit(X_train_encoded, y_train)
rf_pred = rf_model.predict(X_test_encoded)
rf_accuracy = accuracy_score(y_test, rf_pred)

# Save the model
with open('mushroom_predict.pkl', 'wb') as f:
    pickle.dump({'model': rf_model, 'encoder': column_transformer}, f)