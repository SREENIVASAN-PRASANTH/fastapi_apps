from fastapi import FastAPI
from enum import Enum

class Fruits(str, Enum):
    apple = "Apple"
    pine_apple = "Pine Apple"
    orange = "Orange"

class Prizes(int, Enum):
    first_prize = 1
    second_prize = 2
    third_prize = 3

app = FastAPI()

@app.get("/")
async def main_page():
    return {"message": "Hello"}

@app.get("/{name}")
async def get_name_from_url(name: str):
    return {"name": name.upper()}

@app.get("/items/{item_id}")
async def get_name_from_url(item_id: int):
    return {"item_id": item_id}

@app.get("/fruits/{fruit_name}")
async def get_fruit(fruit_name: Fruits):
    if fruit_name == Fruits.orange:
        return {"fruit_name": Fruits.orange}
    
    if fruit_name.value == "Apple":
        return {"fruit_name": Fruits.apple}
    
    
    
    return {"fruit_name": Fruits.pine_apple}

@app.get("/prize_distribution/{winner_position}")
async def distribute_prize(winner_position: Prizes):
    if winner_position == Prizes.first_prize:
        return {"first_prize": "Congratulations you got gold medal."}

    if winner_position == Prizes.second_prize:
        return {"second_prize": "Congratulations you got silver medal."}
    
    if winner_position.value == 3:
        return {"third_prize": "Congratulations you got bronze medal."}



    
