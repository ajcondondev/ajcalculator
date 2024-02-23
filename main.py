from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

app = FastAPI()

templates = Jinja2Templates(directory="templates")

class Operation(BaseModel):
    num1: float
    num2: float

@app.get("/", response_class=HTMLResponse)
async def get_calculator(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/add")
async def add(operation: Operation):
    return {"result": operation.num1 + operation.num2}

@app.post("/subtract")
async def subtract(operation: Operation):
    return {"result": operation.num1 - operation.num2}

@app.post("/multiply")
async def multiply(operation: Operation):
    return {"result": operation.num1 * operation.num2}

@app.post("/divide")
async def divide(operation: Operation):
    return {"result": operation.num1 / operation.num2 if operation.num2 != 0 else "Error: Division by zero"}
