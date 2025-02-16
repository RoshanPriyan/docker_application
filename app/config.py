from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

base_url = os.getenv("BASEURL")
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")
port = os.getenv("PORT")
database_name = os.getenv("DATABASENAME")
db_host = os.getenv('DBHOST')

DATABASE_URL = "mysql+pymysql://myuser:mypassword@mysql:3306/new_db"


# Create engine
engine = create_engine(DATABASE_URL, echo=False)

# Create session
SessionLocal = sessionmaker(bind=engine)

# Function to check DB connection
def check_db_connection():
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))  # ✅ Use text() for raw queries
        print("✅ Database connection successful!")
    except Exception as e:
        print(f"❌ Database connection failed: {e}")

# Run the check
check_db_connection()
