import json

from flask import Flask, jsonify, request
from aaransia import transliterate

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False

# Index
@app.route('/', methods=['GET'])
def hello_world():
    return jsonify({'message' : '3arania - Languages and Dialects transliteration'})

# Transliteration moroccan to moroccan arabic
@app.route('/transliteration_route/', methods=['GET'])
def transliteration_route():
    return jsonify({'transliteration': transliterate(' '.join(request.args.get('text').split('+')), 
                                                    request.args.get('source-language'),
                                                    request.args.get('target-language'))})

if __name__ == "__main__":
    app.run(debug=True)