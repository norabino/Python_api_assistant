from fastapi import FastAPI

app = FastAPI(title="Assistant prêt immobilier")

@app.get("/health")
def health():
    return {"status": "ok"}