# -*- coding: utf-8 -*-
"""
author: Yashaswi Aryan
reg. no.: 200968186
batch: 4
"""

# Importing libraries
import uvicorn
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from fastapi.responses import HTMLResponse, JSONResponse
import userRecommender
import itemRecommender
import pandas as pd


# Creating app object
app = FastAPI()

# Creating templates object
templates = Jinja2Templates(directory = "templates")

#Base Model
class data(BaseModel):
    user_id: int


class data2(BaseModel):
    movies: str
    
# Index, route

@app.get('/', response_class = HTMLResponse)
def home(request: Request, User_id = 0):
    
    #df = userRecommender.get_movie_recommendations_user_based(tf)
    results = [
        {'Title': 'No records', 'Values': 'found!'},
        ]
    #if isinstance(df, pd.DataFrame):
    #    results = df.to_dict('records')
    
    #    context = {'request': request, 'results': results}
    #else:
     #   context = {'request': request, 'results': results, 'User_id': User_id}
    #return JSONResponse(content = result)
    context = {'request': request}
    return templates.TemplateResponse("home.html", context)


@app.post('/moviePred_user_based/')
async def predict_movies_from_user(user: data):
    df = userRecommender.get_movie_recommendations_user_based(user.user_id)
    #result = df.to_dict('records')
    
    return df
    #return df

@app.post('/moviePred_item_based/')
async def predict_movies_from_movies(movie_name: data2):
    df = itemRecommender.get_movie_recommendation_item_based(movie_name.movies)
        
    return df        
    
# Run the api with uvicorn
#if __name__ == '__main__':
#    uvicorn.run(app, host = '127.0.0.1', port = 8000)
    
#uvicorn main:app --reload