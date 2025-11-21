import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os


try:
    cred = credentials.Certificate(os.environ.get("GOOGLE_APPLICATION_CREDENTIALS", "serviceAccountKey.json"))
    firebase_admin.initialize_app(cred)
    db = firestore.client()
except Exception as e:

    print(f"Failed to initialize Firebase Admin SDK: {e}")
    db = None

def get_firestore_db():
    
    if db is None:
      
        raise ConnectionError("Database not initialized")
    return db