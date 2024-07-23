import pandas as pd
import firebase_admin
from firebase_admin import credentials, firestore
from keys import firebase_credentials
# Initialize Firebase Admin SDK
cred = credentials.Certificate(firebase_credentials)
firebase_admin.initialize_app(cred)

# Initialize Firestore database
db = firestore.client()

# Function to store Pandas DataFrame into Firestore
def store_dataframe_to_firestore(dataframe, collection_name):
    for _, row in dataframe.iterrows():
        doc_ref = db.collection(collection_name).document()
        doc_ref.set(row.to_dict())

# Function to retrieve Pandas DataFrame from Firestore
def get_dataframe_from_firestore(collection_name):
    docs = db.collection(collection_name).stream()
    data = [doc.to_dict() for doc in docs]
    return pd.DataFrame(data)

