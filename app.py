from sanic import Sanic
from sanic.response import html
from sanic.blueprints import Blueprint

from jinja2 import Environment, PackageLoader

env = Environment(loader=PackageLoader('app', 'templates'))

app = Sanic(__name__)
app.static('/static', './static')

class GlobalVars:
    def __init__(self):
        self.favicon = app.url_for('static', filename='favicon.png')
        self.logo_large = app.url_for('static', filename='logo-large.png')
        self.main_css = app.url_for('static', filename='main.css')
        self.placeholder1 = app.url_for('static', filename='placeholder1.jpg')
        self.placeholder2 = app.url_for('static', filename='placeholder2.jpg')

gvars = GlobalVars()

@app.route('/')
async def test(request):
    template = env.get_template('index.html')
    html_content = template.render(favicon=gvars.favicon, logo_large=gvars.logo_large, css=gvars.main_css, p1=gvars.placeholder1, p2=gvars.placeholder2)
    return html(html_content)

@app.route('/about-us')
async def test(request):
    template = env.get_template('aboutus.html')
    html_content = template.render(favicon=gvars.favicon, logo_large=gvars.logo_large, css=gvars.main_css)
    return html(html_content)

@app.route('/features')
async def test(request):
    global favicon
    template = env.get_template('features.html')
    html_content = template.render(favicon=gvars.favicon, logo_large=gvars.logo_large, css=gvars.main_css)
    return html(html_content)

@app.route('/getting-started')
async def test(request):
    global favicon
    template = env.get_template('gettingstarted.html')
    html_content = template.render(favicon=gvars.favicon, logo_large=gvars.logo_large, css=gvars.main_css)
    return html(html_content)

@app.route('/signin')
async def test(request):
    global favicon
    template = env.get_template('signin.html')
    html_content = template.render(favicon=gvars.favicon, logo_large=gvars.logo_large, css=gvars.main_css)
    return html(html_content)

@app.route('/signup')
async def test(request):
    global favicon
    template = env.get_template('signup.html')
    html_content = template.render(favicon=gvars.favicon, logo_large=gvars.logo_large, css=gvars.main_css)
    return html(html_content)

app.run(host="0.0.0.0", port=8000)