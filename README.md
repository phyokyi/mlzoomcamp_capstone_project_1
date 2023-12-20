# DataTalk MidTerm Project 2023 November


## Data Source
https://www.kaggle.com/datasets/uciml/mushroom-classification


## Project Description
There is one column call "class". In that datasets, p is poisonous and e is edible. I try to find out which mushrom is poisonous by using five most related columns.


## Note for Files

Dockerfile is for Docker Build  
Notebook.ipynb is cleaning and working notebook
Pipfile and Pipfile.lock is for environment
app.py is for flask and load model
mushroom_predict.pkl is model
mushrooms.csv is source file
train.py is to retrain the model

## To retrain the Dataset
python train.py

## note for pipenv setup

pipenv --python 3.10
pipenv install pandas
pipenv install flask  
pipenv install gunicorn  
pipenv install numpy  
pipenv install scikit-learn==1.3.1  

## Build Docker

sudo docker build -t capstone1-phyokyi .

## Run Docker

sudo docker run -it --rm -p 3000:3000 capstone1-phyokyi

## Sample curl request for result "poisonous"
curl -X POST https://orange-halibut-g4xxrvw49xpfvp6r-3000.app.github.dev/predict -H "Content-Type: application/json" -d '{"odor": "p", "ring_type": "p", "stalk_surface_above_ring": "s", "gill_color": "k", "stalk_surface_below_ring": "s"}'

## Sample curl request for result "edible"
curl -X POST https://orange-halibut-g4xxrvw49xpfvp6r-3000.app.github.dev/predict -H "Content-Type: application/json" -d '{"odor": "a", "ring_type": "p", "stalk_surface_above_ring": "s", "gill_color": "k", "stalk_surface_below_ring": "s"}'

## Working Screenshot
