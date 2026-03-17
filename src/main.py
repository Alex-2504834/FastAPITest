from fastapi import FastAPI
from workers import WorkerEntrypoint, Response
from workers.asgi import ASGIApp

app = FastAPI()

@app.get("/")
async def root():
    return {"ok": True, "message": "hello from fastapi on cloudflare"}

asgi = ASGIApp(app)

class Default(WorkerEntrypoint):
    async def fetch(self, request):
        return await asgi.fetch(request)