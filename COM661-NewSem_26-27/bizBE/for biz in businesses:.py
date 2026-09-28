    for biz in businesses:
        if biz == biz_id:
            return make_response(jsonify(biz), 200)
        else:
            return make_response(jsonify({"ERROR":"Business not found"}), 404)
        
        
        data_to_return = [ business for business in businesses
                    
                    if business["id"] == biz_id]
            
            return make_response(jsonify(data_to_return[0]),200)