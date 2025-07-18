from fastapi import FastAPI

app = FastAPI(title="Backend API")

@app.get("/")
def read_root():
    """Returns a welcome message."""
    return {"message": "Hello from the FastAPI backend! 👋"}

# New function
@app.get("/greet")
def greet_by_name(name: str):
    """Returns a personalized greeting for the given name."""
    return {"greeting": f"Hello, {name}!"}