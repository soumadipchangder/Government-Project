import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase Admin SDK
cred = credentials.Certificate("gdhgf-53e7b-firebase-adminsdk-fbsvc-ea98676b1e.json")  # Path to your service account JSON file
firebase_admin.initialize_app(cred)

# Get Firestore database instance
db = firestore.client()

# Function to store academic details
def store_academic_details():
    academic_details = {
        "name": "Parthib Karak",
        "class": "3rd Year",
        "section": "B",
        "stream": "CSE",
        "enrollment_no": "12022002002165"
    }

    # Store data in Firestore with enrollment_no as document ID
    doc_ref = db.collection("students").document(academic_details["enrollment_no"])
    doc_ref.set(academic_details)

    print("✅ Data stored successfully in Firestore!\n")

# Function to retrieve and display stored academic details
def retrieve_academic_details():
    students_ref = db.collection("students")
    docs = students_ref.stream()

    print("📜 Academic Details (Schema):\n")
    for doc in docs:
        print(f"🆔 Document ID: {doc.id}")  # Enrollment number as document ID
        data = doc.to_dict()
        for key, value in data.items():
            print(f"{key}: {value}")
        print("-" * 40)  # Separator for better readability

# Execute both functions
store_academic_details()
retrieve_academic_details()
