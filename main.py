import json

from flask import Flask
from flask import jsonify
from flask import request

from api.transliterator import *
from api.constants import *

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False

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

# Transliteration moroccan to moroccan arabic
@app.route('/translate_moroccan_arabic/<string:moroccan_entry>', methods=['GET'])
def translate_moroccan_arabic(moroccan_entry):
    moroccan_entry = ' '.join(moroccan_entry.split('+'))
    with open(BASE_DIR + DATA_DIR + USER_INPUT, 'a') as ui:
        ui.write(f'{moroccan_entry},{moroccan_to_arabic(moroccan_entry)}\n')
    return jsonify({'moroccan_transliteration': moroccan_to_arabic(moroccan_entry)})


# Transliteration moroccan arabic to moroccan
@app.route('/translate_arabic_moroccan/<string:moroccan_arabic_entry>', methods=['GET'])
def translate_arabic_moroccan(moroccan_arabic_entry):
    moroccan_arabic_entry = ' '.join(moroccan_arabic_entry.split('+'))
    with open(BASE_DIR + DATA_DIR + USER_INPUT, 'a') as ui:
        ui.write(f'{moroccan_arabic_entry},{arabic_to_moroccan(moroccan_arabic_entry)}\n')
    return jsonify({'moroccan_arabic_transliteration': arabic_to_moroccan(moroccan_arabic_entry)})
if __name__ == "__main__":
    app.run(debug=True)