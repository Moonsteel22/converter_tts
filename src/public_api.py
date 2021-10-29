from src.main import app


@app.get("/converter")
def converter():
    return {"converter": "hello"}
