from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.testing import db
from app.services.mutual_fund import get_open_ended_schemes
from app.routers.auth import router as auth_router, get_current_user
from app.models import Portfolio, BuyFundRequest

from fastapi import Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal, Base, engine

# Create database tables
Base.metadata.create_all(bind=engine)


# Dependency for database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = FastAPI()

# Include the auth router
app.include_router(auth_router)


@app.get("/mutual-funds/open")
async def fetch_open_ended_schemes(current_user: str = Depends(get_current_user)):
    return await get_open_ended_schemes(current_user)


@app.post("/mutual-funds/buy")
async def buy_mutual_fund(
    request: BuyFundRequest,
    current_user: str = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    total_value = request.units * request.price_per_unit
    new_entry = Portfolio(
        user_email=current_user,
        fund_name=request.fund_name,
        units=request.units,
        price_per_unit=request.price_per_unit,
        total_value=total_value,
    )
    db.add(new_entry)
    db.commit()
    return {"message": "Purchase successful", "total_value": total_value}


@app.get("/portfolio")
async def view_portfolio(
    current_user: str = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    portfolio = db.query(Portfolio).filter_by(user_email=current_user).all()
    return portfolio


@app.get("/mutual-funds/families")
async def get_mutual_fund_families(current_user: str = Depends(get_current_user)):
    # Fetch the open-ended mutual fund schemes
    schemes = await get_open_ended_schemes(current_user)

    # Extract the unique Mutual_Fund_Family names using a set
    families = {scheme["Mutual_Fund_Family"] for scheme in schemes}

    # Return the unique families as a list
    return {"unique_families": list(families)}


@app.get("/mutual-funds/family")
async def fetch_schemes_by_family(fund_family: str, current_user: str = Depends(get_current_user)):
    schemes = await get_open_ended_schemes(current_user)
    filtered_schemes = [
        scheme for scheme in schemes if scheme["Mutual_Fund_Family"] == fund_family
    ]
    if not filtered_schemes:
        raise HTTPException(status_code=404, detail="No schemes found for the given fund family")
    return {"schemes": filtered_schemes}
