from flask import Flask, render_template, request, jsonify
from scraper import run_scraper

app = Flask(__name__, template_folder='../frontend')

@app.route('/')
def index():
    # Serve the frontend index.html
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    location = request.form.get('location')
    min_price = int(request.form.get('min_price'))
    max_price = int(request.form.get('max_price'))
    
    results = run_scraper(location, min_price, max_price)
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
