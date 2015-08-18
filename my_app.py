from flask import Flask, request
from flask.ext.sentinel import ResourceOwnerPasswordCredentials, oauth
import flask

app = Flask(__name__)
ResourceOwnerPasswordCredentials(app)


@app.route('/endpoint')
@oauth.require_oauth()
def restricted_access():
    user = request.oauth.user
    return flask.jsonify(
        message="You made it through and accessed the protected resource!",
        username=user.username,
        user_id=str(user.id),
    )

if __name__ == '__main__':
    app.run(ssl_context='adhoc', debug=True)
