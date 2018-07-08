from sanic import Sanic
from sanic.response import html
from sanic.blueprints import Blueprint

from jinja2 import Environment, PackageLoader

env = Environment(loader=PackageLoader('app', 'templates'))

app = Sanic(__name__)
app.static('/static', './static')

@app.route('/')
async def test(request):
    template = env.get_template('index.html')
    html_content = template.render()
    return html(html_content)


app.run(host="0.0.0.0", port=8000)