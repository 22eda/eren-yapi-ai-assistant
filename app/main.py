from fastapi import FastAPI

app = FastAPI(title="Eren Yapi AI Assistant")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
