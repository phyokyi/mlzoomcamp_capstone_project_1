FROM python:3.10.12-slim
RUN pip install pipenv
WORKDIR /app
COPY ["Pipfile","Pipfile.lock","./"]
RUN pipenv install --deploy --system
COPY ["app.py","mushroom_predict.pkl", "./"]
EXPOSE 3000
ENTRYPOINT  ["gunicorn","--bind","0.0.0.0:3000","app:app"]