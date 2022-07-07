from flask import Flask

app = Flask(__name__)


@app.route('/api/v1/peoples', methods=['GET'])
def get_peoples():
    return 'get peoples'

# @app.route('/api/v1/peoples/', methods=['GET'])
# def get_people():
#     return 'get one people'

@app.route('/api/v1/peoples', methods=['POST'])
def create_peoples():
    return 'create peoples'