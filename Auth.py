✅ 8. auth.py (Firestore Logic) 🔒

from firebase_admin.firestore import client as FirestoreClient
from .database import get_firestore_db
from .schemas import UserCreate, UserLogin, UserInDB
from .utils import hash_password, verify_password, create_access_token

router = APIRouter(prefix="/auth", tags=["auth"])

USERS_COLLECTION = "users"

@router.post("/register", response_model=dict)
def register(user: UserCreate, db: FirestoreClient = Depends(get_firestore_db)):
    exists = db.collection(USERS_COLLECTION).where("email", "==", user.email).limit(1).get()
    if exists:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already used")

    user_data = user.dict()
    user_data["password"] = hash_password(user.password) # Hash the password
    user_data["role"] = "student"
    
    del user_data["password"]
    
    try:
        _, doc_ref = db.collection(USERS_COLLECTION).add(user_data)
        
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Database error: {e}")

    return {"message": "User registered successfully", "id": doc_ref.id}

@router.post("/login", response_model=dict)
def login(data: UserLogin, db: FirestoreClient = Depends(get_firestore_db)):
    users_found = db.collection(USERS_COLLECTION).where("email", "==", data.email).limit(1).get()
    
    if not users_found:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    user_doc = users_found[0]
    user_data = user_doc.to_dict()
    
    if not user_data or not verify_password(data.password, user_data.get("password", "")):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    token = create_access_token({"id": user_doc.id, "email": user_data["email"], "role": user_data.get("role", "student")})
    return {"access_token": token, "token_type": "bearer"}