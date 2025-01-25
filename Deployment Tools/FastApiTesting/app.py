from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import csv

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load the CSV data
students_data = []

with open('q-fastapi.csv', newline='') as csvfile:
    print("running csv file")
    reader = csv.DictReader(csvfile)
    for row in reader:
        students_data.append({
            "studentId": int(row['studentId']),
            "class": row['class']
        })

@app.get("/api")
async def get_students(class_: list[str] = Query(None, alias="class")):
    if class_:
        # Filter students by the specified classes
        filtered_students = [student for student in students_data if student['class'] in class_]
        return JSONResponse(content={"students": filtered_students})
    else:
        # Return all students
        return JSONResponse(content={"students": students_data})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)