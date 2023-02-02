from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/login', methods=['GET', 'POST'] )
def login(data):
    return data