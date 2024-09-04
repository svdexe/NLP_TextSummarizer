from fastapi import FastAPI, Request, Form
import uvicorn
import sys
import os
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from starlette.responses import RedirectResponse
from fastapi.responses import HTMLResponse
from textSummarizer.pipeline.prediction import PredictionPipeline

app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates
templates = Jinja2Templates(directory="templates")

@app.get("/", tags=["authentication"])
async def index():
    return RedirectResponse(url="/predict")

@app.get("/docs", tags=["documentation"])
async def docs():
    return RedirectResponse(url="/docs")

@app.get("/train")
async def training():
    try:
        os.system("python main.py")
        return {"message": "Training successful!!"}
    except Exception as e:
        return {"error": f"Error Occurred! {str(e)}"}

@app.get("/predict", response_class=HTMLResponse)
async def predict_page(request: Request):
    return templates.TemplateResponse("predict.html", {"request": request})

@app.post("/predict", response_class=HTMLResponse)
async def predict_route(request: Request, text: str = Form(...)):
    try:
        obj = PredictionPipeline()
        summary = obj.predict(text)
        return templates.TemplateResponse("predict.html", {"request": request, "summary": summary, "original_text": text})
    except Exception as e:
        return templates.TemplateResponse("predict.html", {"request": request, "error": str(e)})

if __name__=="__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)