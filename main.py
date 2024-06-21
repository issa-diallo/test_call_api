import os
from dotenv import load_dotenv
from doctors import Doctors

# Load environment variables from .env file
load_dotenv()

# Define the URLs
base_url = "https://production.api-annuaire-sante.fr/professionnel_de_santes?libelleSavoirFaire[]=Médecine Générale"
login_url = "https://production.api-annuaire-sante.fr/login_check"

# Define the credentials
email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

if not email or not password:
    raise ValueError("EMAIL and PASSWORD environment variables must be set")

# Create an instance of the Doctors class
doctors = Doctors(base_url, login_url, email, password)

# Get the doctors
try:
    doctors_list = doctors.get_doctors()
    print(doctors_list)
except Exception as e:
    print(e)