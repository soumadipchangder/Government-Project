from flask import Flask, render_template, request, jsonify, redirect, url_for
import firebase_admin
from firebase_admin import credentials, firestore

app = Flask(__name__)

# Initialize Firebase Admin SDK
cred = credentials.Certificate("gdhgf-53e7b-firebase-adminsdk-fbsvc-ea98676b1e.json")  # Your Firebase JSON key
firebase_admin.initialize_app(cred)
db = firestore.client()

# Route for the form page
@app.route('/')
def index():
    return render_template('index.html')

# Route for submitting data
@app.route('/submit', methods=['POST'])
def submit():
    data = request.json  # Get JSON data from frontend

    if not all(k in data for k in ("name", "class", "section", "stream", "enrollment_no")):
        return jsonify({"error": "Missing fields"}), 400

    doc_ref = db.collection("students").document(data["enrollment_no"])
    doc_ref.set(data)

    return jsonify({"message": "Data stored successfully", "clearForm": True}), 200

# Route for admin panel (display stored data)
@app.route('/admin')
def admin():
    students_ref = db.collection("students")
    docs = students_ref.stream()
    students = [doc.to_dict() for doc in docs]

    return render_template('admin.html', students=students)

if __name__ == '__main__':
    app.run(debug=True)
