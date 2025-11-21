import requests, base64, datetime, os
from fastapi import APIRouter

router = APIRouter(prefix="/mpesa")

def get_access_token():
    url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
    key = os.getenv("MPESA_CONSUMER_KEY")
    secret = os.getenv("MPESA_CONSUMER_SECRET")
    resp = requests.get(url, auth=(key, secret))
    return resp.json()["access_token"]

@router.post("/pay")
def stk_push(phone: str, amount: int):
    token = get_access_token()

    timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    shortcode = os.getenv("MPESA_SHORTCODE")
    passkey = os.getenv("MPESA_PASSKEY")

    password = base64.b64encode((shortcode + passkey + timestamp).encode()).decode()

    payload = {
        "BusinessShortCode": shortcode,
        "Password": password,
        "Timestamp": timestamp,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": amount,
        "PartyA": phone,
        "PartyB": shortcode,
        "PhoneNumber": phone,
        "CallBackURL": os.getenv("CALLBACK_URL"),
        "AccountReference": "ComradeHousing",
        "TransactionDesc": "Hostel booking"
    }

    headers = {"Authorization": f"Bearer {token}"}
    url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    r = requests.post(url, json=payload, headers=headers)
    return r.json()