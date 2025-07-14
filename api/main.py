from fastapi import FastAPI

app = FastAPI(title="Notes API", version="0.0.1", description="API for managing notes")

# Root endpoint to check if the API is running
@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to the Notes API!"}

# Health check endpoint
@app.get("/health", tags=["Health"])
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

