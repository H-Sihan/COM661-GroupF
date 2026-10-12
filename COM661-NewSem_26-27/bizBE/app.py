from flask import Flask, make_response, jsonify, request
#pip install pymongo
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)

#Mongo connection
client = MongoClient("mongodb://localhost:27017")
db = client.bizDB
businesses = db.biz

@app.route("/", methods=["GET"])
def index():
    return make_response("<h1>Welcome to Flask</h1>", 200)


@app.route("/api/v1.0/businesses", methods=["GET"])
def show_all_businesses():
    
    page_num, page_size = 1, 3
    if request.args.get('pn'):
        page_num = int(request.args.get('pn'))
    if request.args.get('ps'):
        page_size = int(request.args.get('ps'))
    page_start = (page_size * (page_num - 1))

    data_to_return = []

    for business in businesses.find().skip(page_start).limit(page_size):
        business['_id'] = str(business['_id'])

        #for review in business['reviews']:
            #review['_id'] = str(review['_id'])

        data_to_return.append(business)

    return make_response(jsonify(data_to_return), 200)


# fetch by ID
@app.route("/api/v1.0/businesses/<int:biz_id>", methods=["GET"])
def show_one_businesses(biz_id):
    data_to_return = [business for business in businesses
                      if business["id"] == biz_id]

    return make_response(jsonify(data_to_return[0]), 200)


@app.route("/api/v1.0/businesses", methods=["POST"])
def add_business():
    next_id = businesses[-1]["id"] + 1

    new_business = {
        "id": next_id,
        "name": request.form["name"],
        "town": request.form["town"],
        "rating": request.form["rating"],
        "review": []
    }

    businesses.append(new_business)

    return make_response(jsonify(new_business), 201)


@app.route("/api/v1.0/businesses/<int:biz_id>", methods=["PUT"])
def edit_business(biz_id):
    for business in businesses:
        if business['id'] == biz_id:
            business['name'] = request.form['name']
            business['town'] = request.form['town']
            business['rating'] = request.form['rating']
            break

    return make_response(jsonify(business), 200)


@app.route("/api/v1.0/businesses/<int:biz_id>", methods=['DELETE'])
def delete_business(biz_id):
    for business in businesses:
        if business["id"] == biz_id:
            businesses.remove(business)
            break

    return make_response(jsonify({"Message": "Business deleted Successfully!!!"}), 200)


# ===================== REVIEWS ==============================

@app.route("/api/v1.0/businesses/<int:biz_id>/reviews", methods=['GET'])
def get_all_reviews(biz_id):
    for business in businesses:
        if business['id'] == biz_id:
            break

    return make_response(jsonify(business["reviews"]), 200)

@app.route("/api/v1.0/businesses/<int:biz_id>/reviews", methods=['POST'])
def add_new_review(biz_id):
    for business in businesses:
        if len(business['reviews']) == 0:
            new_review_id = 1
        else:
            new_review_id = business['reviews'][-1]["id"] + 1
            
        new_review = {
            "id": new_review_id,
            "username": request.form['username'],
            "comments": request.form['comments'],
            "stars": request.form['stars']
        }
        
        business["reviews"].append(new_review)
        break
    
    return make_response(jsonify(new_review), 201)


@app.route("/api/v1.0/businesses/<int:biz_id>/reviews/<int:rev_id>", methods=['GET'])
def fetch_one_review(biz_id, rev_id):
    for business in businesses:
        if business["id"] == biz_id:
            for review in business["reviews"]:
                if review["id"] == rev_id:
                    break
            break
    
    return make_response(jsonify(review), 200)

@app.route("/api/v1.0/businesses/<int:biz_id>/reviews/<int:rev_id>", methods=['PUT'])
def update_review(biz_id, rev_id):
    for business in businesses:
        if business["id"] == biz_id:
            for review in business["reviews"]:
                if review["id"] == rev_id:
                    review["username"] = request.form["username"]
                    review["comments"] = request.form["comments"]
                    review["stars"] = request.form["stars"]
                    break
            break
    
    return make_response(jsonify(review), 200)


@app.route("/api/v1.0/businesses/<int:biz_id>/reviews/<int:rev_id>", methods=['DELETE'])
def delete_review(biz_id, rev_id):
    for business in businesses:
        if business["id"] == biz_id:
            for review in business["reviews"]:
                if review["id"] == rev_id:
                    business["review"].remove(review)
                    break
            break
    
    return make_response(jsonify({"Message":"Review Deleted successfully!!!"}), 200)

if __name__ == "__main__":
    app.run(debug=True, port=5001)
