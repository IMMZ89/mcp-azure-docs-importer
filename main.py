from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {
        "status": "running",
        "service": "mcp-azure-docs-importer"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
