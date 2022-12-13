from flask import Flask, jsonify, request

khuzaima = Flask(__name__)

# GET Request - CAN send data but its insecure and the point is the get content
# DONT DO THIS -> GET /saveContact  -> 127.0.0.1:3000/saveContact?name=joe&age=12&phone=4043331222 | request.args.get('name')

# POST Request keeps your data private by not putting your data in the URL
# POST Request packages the data together in JSON
# POST requires data because the point is to save it
@khuzaima.route('/saveContact', methods=['POST'])           
def saveContact():    
    try:   
        # Getting data from the REQUEST body                                            
        data = request.data
        print(data)
        
        # Connect to DB | db = MongoDB('127.0.0.1:27017')   
        # Save to DB    | db.insertOne(data)
    except Exception as e:
        print(str(e))
        return jsonify({'msg':'failed', 'data':'', 'err':str(e)})

    return jsonify({'msg':'success', 'data':'', 'err':''})



khuzaima.run(debug=True, port=3000)

"""
Package : {'name': 'joe', 'age': 12, 'phone':'4043331222'}
# REQUEST -> WHO? faraz | WHAT? saving a package | CONTAINS package aka payload | content-type: application/json | status code - 200
      package 
kamran -------> faraz

# RESPONSE -> Flask let me see what package he gave me | Let me save it | Let me give him a message that I saved it
faraz ------> kamran

"""

def sum(x, y):
    try:
        total = x + y
        return total
    except Exception as e:
        print(str(e))
        return 'Failed'

print(sum(5,"5"))
print(sum(5,2))