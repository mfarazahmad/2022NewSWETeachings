
"""
import json     # Converts json to a python dictionary

# Open a file in python
file = open('product.json')
products = json.load(file)

print(products)
"""

products = [
  {
    "product_id": 1,
    "product_category": "Conditioner",
    "product_brand": "Butter London",
    "product_name": "Handbag Holiday Cutile Oil",
    "img": "img_egg_product6538.webp",
    "rating": 3,
    "description": "With added vitamins A and E, this heavenly-smelling oil revives and restores dry, split cuticles.",
    "price": 74.53,
    "quantity": 67
  },
  {
    "product_id": 2,
    "product_category": "Face Care",
    "product_brand": "Butter London",
    "product_name": "LIPPY",
    "img": "img_bee_product4907.webp",
    "rating": 3,
    "description": "Lippy: British slang for someone who makes impertinent or cheeky remarks. Introducing a range of long-wearing, lacquer-like lip glosses in shades to match the famous butter LONDON nail lacquers. From the punchy fuchsia pink of Primrose Hill to the true nude of Yummy Mummy, a hue to complement any look. All butter LONDON products are free of formaldehyde, bismuth, toluene, sulphates, DBP, parabens, synthetic fragrances.",
    "price": 58.13,
    "quantity": 68
  },
  {
    "product_id": 3,
    "product_category": "Conditioner",
    "product_brand": "Butter London",
    "product_name": "Hardwear P.D. Quick Top Coat",
    "img": "img_nut_product9611.webp",
    "rating": 4,
    "description": "Lock your lacquer. butter LONDON's quick-dry, ultra-glossy topcoat protects your lacquer, extending the life of your manicure.",
    "price": 72.94,
    "quantity": 98
  }
]


# REST API that delivers information about these products

# Product Info | All the products

# Product Info | One Product
# What's Left of Stock
# Top 10 Rated Products
# Product Categories
# Top 10 Most Expensive Products
# Average Price of Shampoo


# 1. Import Modules - Flask, jsonify, request
from flask import Flask, jsonify, request

# 2. Create an instance of Flask
app = Flask(__name__)

# 3. Create a route - EVERY FLASK ROUTE HAS TO RETURN JSON OR HTML
@app.route('/test', methods=['GET'])
def test():
    return jsonify({'data':'faraz'})


@app.route('/products', methods=['GET'])
def getProducts():
    return jsonify({'data': products})


@app.route('/products/ratings', methods=['GET'])
def topRatings():
    topProduct = ''
    topRating = 0
    for i in range(0, len(products)):
        currentRating = products[i]['rating']
        if currentRating > topRating:
            topRating = currentRating
            topProduct = products[i]['product_name']

    return jsonify({'data': topProduct})

@app.route('/products/categories', methods=['GET'])
def getCategories():
    categories = []
    for i in range(0, len(products)):
        category = products[i]['product_category']
        categories.append(category)

    return jsonify({'data': categories})

@app.route('/products/search', methods=['GET'])
def searchProducts():
    searchTerm = request.args.get('q').lower()
    for i in range(0, len(products)):
        currentProduct = products[i]['product_name'].lower()

        if searchTerm in currentProduct:
            return jsonify({'data':products[i]})

# 4. Initialize Flask Server
app.run(debug=True)