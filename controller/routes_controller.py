from uuid import UUID
from sanic import text

# Register routes

async def main_index(request):
    # call Alarm object to get all alarms and render them in template
    return text("Index page with template")

async def price_alarm_create(request):
    # extract objects and create with Alarm, do verification
    return text("Hello")

async def price_alarm_delete(request, id: UUID):
    # call delete in Alarm to delete the alarm!
    return text("Deleted!")