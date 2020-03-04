"""This script manages the 3aransia API routes for its multiple features"""

from flask import Flask, jsonify, request
from aaransia import transliterate, get_alphabets_codes, get_alphabets

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False

# Index route
@app.route('/', methods=['GET'])
def hello_world():
    """This is the base route function of 3aransia"""
    return jsonify({'message' : '3arania - Transliteration of languages and dialects - 3aransia.com'})

# Get alphabets codes route
@app.route('/get_alphabets_codes_route/', methods=['GET'])
def get_alphabets_codes_route():
    """This route returns the alphabets codes available in 3aransia"""
    return jsonify({'alphabets_codes' : get_alphabets_codes()})

# Get alphabets route
@app.route('/get_alphabets_route/', methods=['GET'])
def get_alphabets_route():
    """This route returns the alphabets available in 3aransia"""
    return jsonify({'alphabets' : get_alphabets()})

# Transliteration moroccan to moroccan arabic
@app.route('/transliteration_route/', methods=['GET'])
def transliteration_route():
    """This route returns the transliteration of the text entry using the source
    and target language parameters
    text: first value, string
    source-language: second value, language code, string
    target-language: third value, language code, string
    """
    try:
        return jsonify({'transliteration':
                        transliterate(' '.join(request.args.get('text').split('+')),
                                      request.args.get('source-language'),
                                      request.args.get('target-language'),
                                      universal=True)})
    except SourceLanguageException as sle:
        return jsonify({'sourceLanguageException': sle})

if __name__ == "__main__":
    app.run(debug=True)
