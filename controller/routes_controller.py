from sanic import HTTPResponse, redirect, Sanic
from sanic.response import html
from jinja2 import Template
from core.Alarm import Alarm
from persistance.AlarmEntity import AlarmEntity
import logging

logger = logging.getLogger(__name__)
# Register routes

async def main_index(request):
    # call Alarm object to get all alarms and render them in template
    alarm =  Alarm()
    with open("/home/pi/price_alarm/jinja_templates/index.html", "r") as f:
        template = Template(f.read())
    app =  Sanic.get_app()
    template_obj = {
        'alarms': await alarm.get_alarms(),
        'subdirectory': app.ctx.subdirectory
    }
    content = template.render(template_obj)
    return html(content)

async def price_alarm_create(request):
    body = request.form
    email = body.get('email')
    url = body.get('link')
    price_from = int(body.get('price_from'))
    price_to = int(body.get('price_to'))
    new_alarm = AlarmEntity(url, email, price_from, price_to)
    await Alarm().create_alarm(new_alarm)
    return HTTPResponse(status=201)

async def price_alarm_delete(request, id: str):
    await Alarm().delete_alarm(id)
    app =  Sanic.get_app()
    url = app.url_for("main_index")
    return redirect(url)