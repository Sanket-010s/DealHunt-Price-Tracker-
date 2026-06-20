from app.db.base import get_db
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import firebase_admin
from firebase_admin import auth, credentials
import os
import json

# Initialize Firebase Admin if not already initialized
try:
    if not firebase_admin._apps:
        firebase_json = os.getenv("FIREBASE_SERVICE_ACCOUNT_JSON")
        firebase_path = os.getenv("FIREBASE_CREDENTIALS_PATH")

        if firebase_json:
            # ✅ Render: load from environment variable (JSON string)
            cred_dict = json.loads(firebase_json)
            cred = credentials.Certificate(cred_dict)
        elif firebase_path:
            # ✅ Local: load from file path in .env
            cred = credentials.Certificate(firebase_path)
        else:
            # ✅ Local fallback: look for file in current directory
            cred = credentials.Certificate("firebase-adminsdk.json")

        firebase_admin.initialize_app(cred)
except Exception as e:
    print(f"Firebase admin init error: {e}")

security = HTTPBearer()

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)) -> str:
    """Verify Firebase token and return user ID (UID)"""
    try:
        token = credentials.credentials
        decoded_token = auth.verify_id_token(token)
        return decoded_token['uid']
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication token",
            headers={"WWW-Authenticate": "Bearer"},
        )

__all__ = ["get_db", "get_current_user"]