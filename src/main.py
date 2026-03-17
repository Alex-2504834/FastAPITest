from workers import WorkerEntrypoint
from fastapi import FastAPI
import asgi

app = FastAPI()

@app.get("/")
async def root():
    return {"ok": True, "message": "hello from fastapi on cloudflare"}

class Default(WorkerEntrypoint):
    async def fetch(self, request):
        return await asgi.fetch(app, request, self.env)