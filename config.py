import os

# Flask Configuration
FLASK_HOST = os.getenv("FLASK_HOST", "0.0.0.0")
FLASK_PORT = int(os.getenv("FLASK_PORT", 8000))

# Security Keys
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "secret")
SECRET_KEY = os.getenv("SECRET_KEY", "flask-session-secret")

# MongoDB Atlas Connection
MONGO_URL = os.getenv(
    "MONGO_URL",
    "mongodb+srv://nandinimaherrajput_db_user:wZMdkTvydVgTe8f6@medicalinsurancecluster.f7og1cp.mongodb.net/?appName=MedicalInsuranceCluster"
)

# Database Details
db_name = "medical_insurance_db"
user_collection_name = "collection_user"
data_collection_name = "collection_data"

# Base Directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# File Paths
INPUT_DATA_PATH = os.path.join(BASE_DIR, "data", "medical_insurance.csv")
ML_MODEL_PATH = os.path.join(BASE_DIR, "linear_reg_med_ins.pkl")
INPUT_COLUMN_DATA = os.path.join(BASE_DIR, "med_ins_column_data.json")