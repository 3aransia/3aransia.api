import json

from flask import Flask, jsonify, request
from aaransia import moroccan_to_arabic, moroccan_arabic_to_moroccan

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False

# Index
@app.route('/', methods=['GET'])
def hello_world():
    return jsonify({'message' : '3arania - The Moroccan Latin/Digit Language Framework'})

# Transliteration moroccan to moroccan arabic
@app.route('/translate_moroccan_arabic/<string:moroccan_entry>', methods=['GET'])
def translate_moroccan_arabic(moroccan_entry):
    return jsonify({'moroccan_transliteration': moroccan_to_arabic(' '.join(moroccan_entry.split('+')))})


# Transliteration moroccan arabic to moroccan
@app.route('/translate_arabic_moroccan/<string:moroccan_arabic_entry>', methods=['GET'])
def translate_arabic_moroccan(moroccan_arabic_entry):
    return jsonify({'moroccan_arabic_transliteration': moroccan_arabic_to_moroccan(' '.join(moroccan_arabic_entry.split('+')))})
if __name__ == "__main__":
    app.run(debug=True)