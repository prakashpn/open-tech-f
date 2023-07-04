from flask import Flask, jsonify, make_response, render_template

from controller.user_controller import user_app

application = Flask(__name__)
application.config['SECRET_KEY'] = 'OpenTech'


@application.route("/")
def hello_from_root():
    return jsonify(message='Hello, Hope you are doing well!')


@application.route("/open-tech-image")
def hello():
    return render_template('index.html')


@application.errorhandler(404)
def resource_not_found(e):
    return make_response(jsonify(error='Not found!'), 404)


application.register_blueprint(user_app, url_prefix='/rest/user')

if __name__ == '__main__':
    application.run(host="localhost", port=8080, debug=True)
