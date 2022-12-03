from fastapi import FastAPI
from pydantic import BaseModel

import pandas as pd 
import json 
import csv 
import os 
MEDIA_ROOT = os.path.expanduser("~/snap/snappyatom/FastAPI/iris.csv")

app = FastAPI()
@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI!!"}

@app.get("/iris/")

async def root():

    X_df = pd.read_csv(MEDIA_ROOT)
    data = X_df.to_json(orient="index")
    data = json.loads(data)
    return data

     

class Iris(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float
    species: str


@app.post("/insertData/")
async def insertData(item: Iris):

    with open(MEDIA_ROOT, 'a', newline='') as csvfile:
        fieldnames = ['sepal_length', 'sepal_width', 'petal_length',
                      'petal_width', 'species']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({'sepal_length': item.sepal_length,
                        'sepal_width': item.sepal_width,
                        'petal_length': item.petal_length,
                        'petal_width': item.petal_width,
                        'species': item.species})
    return item


@app.put("/updateData/{item_id}")
async def updateData(item_id: int, item: Iris):
    df = pd.read_csv(MEDIA_ROOT)

    df.loc[df.index[-1], 'sepal_length'] = item.sepal_length
    df.loc[df.index[-1], 'sepal_width'] = item.sepal_width,
    df.loc[df.index[-1], 'petal_length'] = item.petal_length,
    df.loc[df.index[-1], 'petal_width'] = item.petal_width,
    df.loc[df.index[-1], 'species'] = item.species
    df.to_csv(MEDIA_ROOT, index=False)

    return {"item_id": item_id, **item.dict()}


@app.delete("/deleteData/")
async def deleteData():
    df = pd.read_csv(MEDIA_ROOT)
    df.drop(df.index[-1], inplace=True)
    df.to_csv(MEDIA_ROOT, index=False)
    return 'Eliminado'