
from fastapi import FastAPI, HTTPException, Depends, Query
from pydantic import BaseModel
import time

app = FastAPI(title="M1-02 Demo")


class Item(BaseModel):
    name: str
    price: float
    in_stock: bool = True


class ItemResponse(Item):
    id: int


_items: dict[int, Item] = {}
_next_id = 1


def fake_request_timer():
    start = time.time()
    yield start
    print(f"Request took {time.time() - start:.4f}s")


@app.get("/items/{item_id}", response_model=ItemResponse)
def get_item(item_id: int, verbose: bool = Query(default=False)):
    if item_id not in _items:
        raise HTTPException(status_code=404, detail="Item not found")
    item = _items[item_id]
    if verbose:
        print(f"Fetched item {item_id}: {item}")
    return ItemResponse(id=item_id, **item.model_dump())


@app.post("/items", response_model=ItemResponse, status_code=201)
def create_item(item: Item, timer=Depends(fake_request_timer)):
    global _next_id
    item_id = _next_id
    _items[item_id] = item
    _next_id += 1
    return ItemResponse(id=item_id, **item.model_dump())


@app.get("/health")
async def health():
    return {"status": "ok"}