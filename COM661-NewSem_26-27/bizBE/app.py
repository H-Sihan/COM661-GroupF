from flask import Flask, make_response, jsonify

app = Flask(__name__)

businesses = [
    {
        "id":1,
        "name":"Costa",
        "town":"London",
        "rating":4,
        "reviews":[]
    },
    {
        "id":2,
        "name":"Nero",
        "town":"London",
        "rating":4,
        "reviews":[]
    },
    {
        "id":3,
        "name":"Starbucks",
        "town":"London",
        "rating":4,
        "reviews":[]
    },
]

@app.route("/", methods=["GET"])
def index():
    return make_response("<h1>Welcome to Flask</h1>", 200)


@app.route("/api/v1.0/businesses", methods=["GET"])
def show_all_businesses():
    return make_response(jsonify(businesses), 200)


#fetch by ID
@app.route("/api/v1.0/businesses/<int:biz_id>", methods=["GET"])
def show_one_businesses(biz_id):
    for biz in businesses:
        if biz == biz_id:
            return make_response(jsonify(biz), 200)
        else:
            return make_response(jsonify({"ERROR":"Business not found"}), 404)

if __name__ == "__main__":
    app.run(debug=True)
