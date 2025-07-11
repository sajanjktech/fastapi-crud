
from dotenv import load_dotenv
import os

load_dotenv()

store = {}

fake_users_db = {
    os.getenv("USER1_USERNAME"): {
        "username": os.getenv("USER1_USERNAME"),
        "role": os.getenv("USER1_ROLE"),
        "hashed_password": os.getenv("USER1_HASHED_PASSWORD"),
    },
    os.getenv("USER2_USERNAME"): {
        "username": os.getenv("USER2_USERNAME"),
        "role": os.getenv("USER2_ROLE"),
        "hashed_password": os.getenv("USER2_HASHED_PASSWORD"),
    }
}
