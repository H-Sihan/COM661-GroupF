from flask import Flask

from blueprint.businesses.businesses import businesses_bp
from blueprint.reviews.reviews import review_bp
from blueprint.auth.auth import auth_bp

app = Flask(__name__)

app.register_blueprint(businesses_bp)
app.register_blueprint(review_bp)
app.register_blueprint(auth_bp)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
