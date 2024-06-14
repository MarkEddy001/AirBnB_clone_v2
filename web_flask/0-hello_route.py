#!/usr/bin/python3
"""Start a flask web app
"""

from flask import Flask
app = Flask(__name__)

# Make trailing slashes in the URL optional for all routes
app.url_map.strict_slashes = False

@app.route('/airbnb-onepage/')
def hello_flask():
    """Return string when route queried
    """
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
