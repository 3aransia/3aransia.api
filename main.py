import json

from flask import Flask, jsonify, request
from aaransia import transliterate_moroccan, transliterate_moroccan_arabic

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False

# Index
@app.route('/', methods=['GET'])
def hello_world():
    return jsonify({'message' : '3arania - The Moroccan Latin/Digit Language Framework API'})

# Transliteration moroccan to moroccan arabic
@app.route('/transliterate_moroccan_route/<string:moroccan_entry>', methods=['GET'])
def transliterate_moroccan_route(moroccan_entry):
    return jsonify({'moroccan_arabic_transliteration': transliterate_moroccan(' '.join(moroccan_entry.split('+')))})


# Transliteration moroccan arabic to moroccan
@app.route('/transliterate_moroccan_arabic_route/<string:moroccan_arabic_entry>', methods=['GET'])
def transliterate_moroccan_arabic_route(moroccan_arabic_entry):
    return jsonify({'moroccan_transliteration': transliterate_moroccan_arabic(' '.join(moroccan_arabic_entry.split('+')))})
if __name__ == "__main__":
    app.run(debug=True)
