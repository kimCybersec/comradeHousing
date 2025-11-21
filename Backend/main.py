from fastapi import FastAPI
from .auth import router as auth_router
from .hostels import router as hostel_router
from .bookings import router as bookings_router
from .mpesa import router as mpesa_router

app = FastAPI(title="ComradeHousing Firestore API")

app.include_router(auth_router)
app.include_router(hostel_router)
app.include_router(bookings_router)
app.include_router(mpesa_router)

@app.get("/")
def home():
    return {"message": "ComradeHousing API running (Firestore Edition)"}