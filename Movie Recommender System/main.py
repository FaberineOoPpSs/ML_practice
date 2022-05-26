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
import userRecommender
import itemRecommender

df = list()

# Creating app object
app = FastAPI()

# Creating templates object
templates = Jinja2Templates(directory = "templates")


# Index, route

@app.get('/')
def home(request: Request, User_id = None):
    global df
    df = userRecommender.get_movie_recommendations_user_based(User_id)
    return templates.TemplateResponse("home.html", {
        "request": request,
        "User_id": User_id
        })

class RequestBody(BaseModel):
    Title: str
    Values: float

@app.post("/userRecommendations")
async def create_stock(stock_request: RequestBody):
    global df
    

    return {
        df
        }

@app.get('/moviePred_user_based')
def predict_movies_from_user(user_id: int):
    df = userRecommender.get_movie_recommendations_user_based(user_id)
        
    return df

@app.get('/moviePred_item_based')
def predict_movies_from_movies(movie_name: str):
    df = itemRecommender.get_movie_recommendation_item_based(movie_name)
        
    return df        
    
# Run the api with uvicorn
if __name__ == '__main__':
    uvicorn.run(app, host = '127.0.0.1', port = 8000)
    
#uvicorn main:app --reload