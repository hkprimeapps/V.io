from routes.instagram import router as instagram_router
import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Include the Instagram router
app.include_router(instagram_router)

# Mount the static files directory inside the 'app' directory
current_file_dir = os.path.dirname(os.path.abspath(__file__))
static_dir = os.path.join(current_file_dir, "static")
app.mount("/static", StaticFiles(directory=static_dir), name="static")

@app.get("/")
async def read_index():
    return {"message": "Welcome to the Instagram Integration App"}

@app.get('/dashboard')
async def dashboard():
    return {"message": "Welcome to your dashboard!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
