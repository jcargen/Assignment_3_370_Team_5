from flask import Flask, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB connection
client = MongoClient('mongodb://localhost:27017/')
db = client['microservices']
products = db['products']

@app.route('/products', methods=['GET'])
def get_products():
    # Query MongoDB for all products
    all_products = list(products.find({}, {"_id": 0}))
    return jsonify(all_products)

if __name__ == '__main__':
    # Initialize with sample data if collection is empty
    if products.count_documents({}) == 0:
        sample_products = [
            {"id": "1001", "name": "Laptop", "price": 1200},
            {"id": "1002", "name": "Smartphone", "price": 800},
            {"id": "1003", "name": "Tablet", "price": 600}
        ]
        products.insert_many(sample_products)
    app.run(port=5002)
