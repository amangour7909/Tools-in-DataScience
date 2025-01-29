from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Dict, Any
import csv

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load student data from CSV file
students = []

print("Loading students data from CSV file")
with open("students.csv", "r") as csvfile:
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:
        students.append({"studentId": int(row["studentId"]), "class": row["class"]})

@app.get("/api")
def get_students(class_: List[str] = Query(None, alias="class")):
    if class_:
        filtered_students = [student for student in students if student["class"] in class_]
        return {"students": filtered_students}
    return {"students": students}

# To run the server, use: uvicorn main:app --reload