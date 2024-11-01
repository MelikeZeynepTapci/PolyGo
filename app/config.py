import os
from dotenv import load_dotenv
load_dotenv()

SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')

# SSL configuration if SSL is required
SSL_CERT_PATH = os.path.join(os.path.dirname(__file__), '..', 'ssl', 'ca-certificate.crt')
ssl_args = {}
if os.path.exists(SSL_CERT_PATH):
    ssl_args = {
        "ssl": {
            "ca": SSL_CERT_PATH
        }
    }

SQLALCHEMY_TRACK_MODIFICATIONS = False

