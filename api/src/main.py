"""Main API file
"""
# Set PYTHONPATH of the project
import os 
import sys
import pathlib

file_path =  os.path.realpath(__file__)
root_dir = pathlib.Path(file_path).parents[1] # 2 for 2 levels etc
sys.path.insert(1, str(root_dir))

# Third-party imports
import uvicorn 

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Internal imports
from src.app.auto.router import router as auto_router
from src.app.manual.router import router as manual_router

app = FastAPI(
    title="RoboticLLMApi",
    routes=[
        auto_router, 
        manual_router
    ]
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health_check():
    return {"OK"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)