from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


# SQLAlchemy models
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)

    # Establish a relationship with the Portfolio model
    portfolio = relationship("Portfolio", back_populates="user")


class Portfolio(Base):
    __tablename__ = "portfolios"

    id = Column(Integer, primary_key=True, index=True)
    user_email = Column(String, ForeignKey("users.email"), nullable=False)
    fund_name = Column(String, nullable=False)
    units = Column(Float, nullable=False)
    price_per_unit = Column(Float, nullable=False)
    total_value = Column(Float, nullable=False)

    # Establish a relationship with the User model
    user = relationship("User", back_populates="portfolio")


# Pydantic models for request/response validation
class UserCreate(BaseModel):
    email: str
    password: str


class UserLogin(BaseModel):
    email: str
    password: str


class UserResponse(BaseModel):
    email: str

    class Config:
        orm_mode = True


class PortfolioCreate(BaseModel):
    fund_name: str
    units: float
    price_per_unit: float

    class Config:
        orm_mode = True


class PortfolioResponse(BaseModel):
    fund_name: str


class BuyFundRequest(BaseModel):
    fund_name: str
    units: float
    price_per_unit: float

