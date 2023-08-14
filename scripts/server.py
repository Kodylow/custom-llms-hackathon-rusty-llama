from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/getfile', methods=['GET'])
def get_file():
    return send_from_directory('.', 'output.jsonl', as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
