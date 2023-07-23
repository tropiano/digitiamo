from flask import Flask, request
from src import clean_data

app = Flask(__name__)


@app.route("/filter_null",  methods=['POST'])
def filter_null():
    """
    Endpoint to filter null values  

    Args:

    Returns:
        str: the cleaned csv file as a str.
    """

    csv_file = request.files.get('file')
    col = request.form.get('column')
    
    filtered_file = clean_data.filter_null(csv_file, column=col)
    return filtered_file

@app.route("/filter_ctg",  methods=['POST'])
def filter_ctg():
    """
    Endpoint to filter categories  

    Args:

    Returns:
        str: the cleaned csv file as a str.
    """
    csv_file = request.files.get('file')
    filtered_file = clean_data.filter_category(csv_file)
    return filtered_file

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    