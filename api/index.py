import json
from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
import os

app = FastAPI()

# Read the JSON file and load data
def load_marks():
    file_path = os.path.join(os.path.dirname(__file__), "../marks.json")
    with open(file_path, "r") as f:
        return json.load(f)

marks = load_marks()

# Define API endpoint
@app.get("/")
async def get_marks(names: list[str] = Query(...)):
    response = {"marks": [marks.get(name, None) for name in names]}
    return JSONResponse(content=response)
