# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "fastapi",
#     "uvicorn",
# ]
# ///
from fastapi import FastAPI, HTTPException
from typing import Dict, List

app = FastAPI()

# Create a list of items that will act like a database
items: List[Dict[str, float | int | str]] = []

# Create a GET endpoint that returns all items
@app.get("/items")
async def get_items() -> List[Dict[str, float | int | str]]:
    return items

# Create a GET endpoint that returns a specific item by ID
@app.get("/items/{item_id}")
async def get_item(item_id: int) -> Dict[str, float | int | str]:
    if item := next((i for i in items if i["id"] == item_id), None):
        return item
    raise HTTPException(status_code=404, detail="Item not found")

# Create a POST endpoint that creates a new item
@app.post("/items")
async def create_item(item: Dict[str, float | str]) -> Dict[str, float | int | str]:
    new_item = {"id": len(items) + 1, "name": item["name"], "price": float(item["price"])}
    items.append(new_item)
    return new_item

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)