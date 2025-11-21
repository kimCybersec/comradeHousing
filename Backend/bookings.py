from fastapi import HTTPException,APIRouter, Depends, status
from firebase_admin.firestore import client as FirestoreClient
from .database import get_firestore_db
from .schemas import BookingCreate

router = APIRouter(prefix="/bookings", tags=["bookings"])

BOOKINGS_COLLECTION = "bookings"

@router.post("/", response_model=dict)
def create_booking(data: BookingCreate, db: FirestoreClient = Depends(get_firestore_db)):
    # The incoming data from the frontend should match the BookingCreate schema
    booking_data = data.dict()
    
    try:
        _, doc_ref = db.collection(BOOKINGS_COLLECTION).add(booking_data)
        return {"message": "Booking created successfully", "booking_id": doc_ref.id}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Database error: {e}")