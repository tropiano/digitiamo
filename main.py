from flask import Flask, request
from src import clean_data

app = Flask(__name__)


@app.route("/filter_null",  methods=['POST'])
def filter_null():
    
    csv_file = request.files.get('file')
    col = request.form.get('column')
    
    filtered_file = clean_data.filter_null(csv_file, column=col)
    return filtered_file

@app.route("/filter_ctg",  methods=['POST'])
def filter_ctg():
    
    csv_file = request.files.get('file')
    filtered_file = clean_data.filter_category(csv_file)
    return filtered_file

if __name__ == '__main__':
    app.run(debug=True)
    