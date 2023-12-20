# DataTalk MLZoomcamp Capstone 1 Project 2023


## Data Source
https://www.kaggle.com/datasets/uciml/mushroom-classification

## Note for Files

Dockerfile is for Docker Build  
Notebook.ipynb is cleaning and working notebook  
Pipfile and Pipfile.lock is for environment  
app.py is for flask and load model  
mushroom_predict.pkl is model  
mushrooms.csv is source file  
train.py is to retrain the model  

## Project Description
There is one column call "class". In that datasets, p is poisonous and e is edible. I try to find out which mushrom is poisonous by using five most related columns.

### Dataset Overview
Dataset has total 23 columns. I use "class" column to predict.

### Learning about data

I try to visualize the data as follow to learn about datasets:
![image](https://github.com/phyokyi/mlzoomcamp_capstone_project_1/assets/12389166/1e4c6ab4-9535-4f5f-a62e-d325b79bdf4e)

Among them only five columns, I choose to train the model. Those are odor, ring_type, stalk_surface_below_ring, stalk_surface_above_ring, gill_color  
![image](https://github.com/phyokyi/mlzoomcamp_capstone_project_1/assets/12389166/5647231b-5e26-49cf-9513-fd4ae68e9441)


### Model Testing and accuracy

I try to test with three different model:  
RandomForestClassifier got 0.9945839487936977  
LogisticRegression got 0.9940915805022157  
SVC got 0.9945839487936977  

So I choose RandomForestClassifier for this project.

## To Re-Build the Project

### note for pipenv setup

pipenv --python 3.10  
pipenv install pandas  
pipenv install flask  
pipenv install gunicorn  
pipenv install numpy  
pipenv install scikit-learn==1.3.1  

### To retrain the Dataset
pipenv shell  
python train.py  

### Build Docker

sudo docker build -t capstone1-phyokyi .

### Run Docker

sudo docker run -it --rm -p 3000:3000 capstone1-phyokyi

## Testing

### Sample curl request for result "poisonous"
curl -X POST http://mlzoomcamp-capstone-11.phyokyi.com:3000/predict -H "Content-Type: application/json" -d '{"odor": "p", "ring_type": "p", "stalk_surface_above_ring": "s", "gill_color": "k", "stalk_surface_below_ring": "s"}'

### Sample curl request for result "edible"
curl -X POST http://mlzoomcamp-capstone-11.phyokyi.com:3000/predict -H "Content-Type: application/json" -d '{"odor": "a", "ring_type": "p", "stalk_surface_above_ring": "s", "gill_color": "k", "stalk_surface_below_ring": "s"}'

## Working Screenshot
![image](https://github.com/phyokyi/mlzoomcamp_capstone_project_1/assets/12389166/1405cafe-54d8-4458-b00c-7b08e63cbe08)

## Hostting
App is hosted on google cloud. You can access the app via http://mlzoomcamp-capstone-11.phyokyi.com:3000/predict
