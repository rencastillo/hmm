from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Path for file uploads
upload_path = 'uploads/'

# Ensure upload directory exists
os.makedirs(upload_path, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if file:
        filename = os.path.join(upload_path, file.filename)
        file.save(filename)
        return jsonify({"status": f"File {file.filename} uploaded successfully."}), 200

if __name__ == "__main__":
    app.run(debug=True)
