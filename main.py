import json

from flask import Flask
from flask import jsonify
from flask import request

from api.algorithms import *
from api.constants import *

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False

moroccan_words = pd.read_csv(BASE_DIR + DATA_DIR + DICTIONARY_SAMPLE)
moroccan_words = moroccan_to_arabic(' '.join(moroccan_words["LDM"]))

# Index
@app.route('/', methods=['GET'])
def hello_world():
    return jsonify({'message' : '3arania - The Moroccan Latin/Digit Language Framework'})

# Get all the moroccan words
@app.route('/moroccan_words', methods=['GET'])
def returnAll():
    return jsonify({'moroccan_words' : moroccan_words})

# Look for a word in the dictionary
@app.route('/moroccan_words/<string:moroccan_word>', methods=['GET'])
def returnOne(moroccan_word):
    the_one = dict(WORD_NOT_FOUND_ERROR)
    for i, w in enumerate(moroccan_words):
        if w['moroccan_word'] == moroccan_word:
            the_one = moroccan_words[i]
    return jsonify({'moroccan_word' : the_one})

# Add a word to the dictionary
@app.route('/moroccan_words', methods=['POST'])
def addOne():
    new_moroccan_word = request.get_json()
    moroccan_words.append(new_moroccan_word)
    return jsonify({'moroccan_words' : moroccan_words})

# Edit a word on the dictionary
@app.route('/moroccan_words/<string:moroccan_word>', methods=['PUT'])
def editOne(moroccan_word):
    new_moroccan_word = request.get_json()
    for i,w in enumerate(moroccan_words):
      if w['moroccan_word'] == moroccan_word:
        moroccan_words[i] = new_moroccan_word    
    ws = request.get_json()
    return jsonify({'moroccan_words' : moroccan_words})

# Delete a word from the dictionary
@app.route('/moroccan_words/<string:moroccan_word>', methods=['DELETE'])
def deleteOne(moroccan_word):
    for i,w in enumerate(moroccan_words):
      if w['moroccan_word'] == moroccan_word:
        del moroccan_words[i]  
    return jsonify({'moroccan_words' : moroccan_words})

# Translation moroccan to arabic
@app.route('/translate_moroccan_arabic/<string:moroccan_entry>', methods=['GET'])
def translate_moroccan_arabic(moroccan_entry):
    moroccan_translation_arabic = moroccan_to_arabic(' '.join(moroccan_entry.split('+')))
    return jsonify({'moroccan_translation_arabic' : moroccan_translation_arabic})

if __name__ == "__main__":
    app.run(debug=True)