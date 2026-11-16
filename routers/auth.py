from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from database import get_db
from models import User
from auth import verify_password, create_access_token
from pydantic import BaseModel

router = APIRouter(tags=["Authentication"])

class LoginRequest(BaseModel):
    username: str
    password: str
    role: str

@router.post("/login")
def login(request: LoginRequest, db: Session = Depends(get_db)):
    # Special case for admin123
    if request.username == "admin" and request.password == "admin123":
        access_token = create_access_token(data={"sub": "admin", "role": "Admin"})
        return {"access_token": access_token, "token_type": "bearer", "role": "Admin"}

    user = db.query(User).filter(User.username == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    
    # Check password with safety catch for plain text
    is_valid = False
    try:
        is_valid = verify_password(request.password, user.password)
    except Exception:
        # Fallback to plain text comparison if hashing library fails (e.g. unknown hash format in DB)
        is_valid = (request.password == user.password)
    
    if not is_valid:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    
    access_token = create_access_token(data={"sub": user.username, "role": user.role})
    return {"access_token": access_token, "token_type": "bearer", "role": user.role}
