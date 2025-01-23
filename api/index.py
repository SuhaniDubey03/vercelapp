import csv
from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
import os

app = FastAPI()

# Read the CSV file and load data
def load_marks():
    marks_data = {}
    file_path = os.path.join(os.path.dirname(__file__), "../marks.csv")
    with open(file_path, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            marks_data[row["name"]] = int(row["marks"])
    return marks_data

marks = load_marks()

# Define API endpoint
@app.get("/")
async def get_marks(names: list[str] = Query(...)):
    response = {"marks": [marks.get(name, None) for name in names]}
    return JSONResponse(content=response)
