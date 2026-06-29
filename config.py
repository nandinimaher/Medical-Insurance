import os
FLASK_HOST = "0.0.0.0"
FLASK_PORT = 5005

MONGO_URL = "mongodb+srv://nandinimaherrajput_db_user:wZMdkTvydVgTe8f6@medicalinsurancecluster.f7og1cp.mongodb.net/?appName=MedicalInsuranceCluster"
db_name = 'medical_insurance_db'
user_collection_name = 'collection_user'
data_collection_name = "collection_data"

INPUT_DATA_PATH = os.path.join(os.getcwd(), "data","medical_insurance.csv")
ML_MODEL_PATH = os.path.join(os.getcwd(), "linear_reg_med_ins.pkl")

INPUT_COLUMN_DATA = os.path.join(os.getcwd(), "med_ins_column_data.json")