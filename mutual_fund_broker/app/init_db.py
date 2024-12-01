from database import Base, engine
from models import User, Portfolio  # Import all models here

print("Creating database tables...")
Base.metadata.create_all(bind=engine)
print("Tables created successfully.")
