from fastapi import FastAPI

from api.agents import agent_router

app = FastAPI(title="Translation Agent", summary="Translates docs", version="0.0.1")

app.include_router(agent_router)

@app.get("/")
def root():
    return {"message": "This is a FastAPI application"}

if __name__=="__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)