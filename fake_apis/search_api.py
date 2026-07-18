from fastapi import FastAPI


app = FastAPI(title="Fake Bank Search API")


search_index = [
    {"type": "customer", "id": "C1001", "text": "Avery Morgan active customer checking account"},
    {"type": "customer", "id": "C1002", "text": "Jordan Lee review customer frozen card"},
    {"type": "case", "id": "CASE3001", "text": "ATM cash dispute open operations"},
    {"type": "document", "id": "D6002", "text": "card dispute form pending review"},
]


@app.get("/health")
def health():
    return {"status": "ok", "service": "search-api"}


@app.get("/search")
def search(q: str, result_type: str | None = None):
    query = q.lower()
    results = [item for item in search_index if query in item["text"].lower()]
    if result_type:
        results = [item for item in results if item["type"] == result_type]
    return {"query": q, "count": len(results), "results": results}

