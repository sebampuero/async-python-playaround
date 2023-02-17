from uuid import UUID
from sanic import Sanic
from sanic import text

app = Sanic.get_app()

# Register routes

@app.route("/")
async def main_index(request):
    return text("Index page with template")

@app.post("/price-alarm")
async def price_alarm_create(request):
    pass

@app.delete("/price-alarm/<id:uuid>")
async def price_alarm_create(request, id: UUID):
    pass