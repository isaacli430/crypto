from sanic import Sanic
from sanic.response import html
from sanic.blueprints import Blueprint

from jinja2 import Environment, PackageLoader

env = Environment(loader=PackageLoader('app', 'templates'))

app = Sanic(__name__)
app.static('/static', './static')
mat_css_url = app.url_for('static', filename='css/materialize.min.css')
mat_js_url = app.url_for('static', filename='js/materialize.min.js')

@app.route('/')
async def test(request):
    global mat_css_url
    global mat_js_url
    template = env.get_template('index.html')
    html_content = template.render(js=mat_js_url, css=mat_css_url)
    return html(html_content)


app.run(host="0.0.0.0", port=8000)