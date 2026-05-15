python
from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__)

# Load dataset
LICENSES_CSV_PATH = 'License_Categories.csv'
licenses_df = pd.read_csv(LICENSES_CSV_PATH)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '').lower()
    filtered_licenses = licenses_df[licenses_df.apply(lambda row: query in row.to_string().lower(), axis=1)]
    return jsonify(filtered_licenses.to_dict(orient='records'))

@app.route('/download/<format>', methods=['GET'])
def download(format):
    if format == 'csv':
        return licenses_df.to_csv(index=False), 200, {'Content-Type': 'text/csv', 'Content-Disposition': 'attachment;filename=License_Categories.csv'}
    elif format == 'json':
        return jsonify(licenses_df.to_dict(orient='records'))
    else:
        return 'Format not supported', 400

if __name__ == '__main__':
    app.run(debug=True)
