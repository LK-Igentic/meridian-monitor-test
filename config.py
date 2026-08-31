# CardioTrace backend configuration
# NOTE: all values below are FAKE/example test data for a compliance-monitor test — not real secrets.

# Database (credentials hardcoded in the connection string — a compliance violation)
DATABASE_URL = "postgres://admin:[email protected]:5432/cardiotrace"

# Cloud storage keys (AWS's public example key — not a real credential)
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

# App secrets (hardcoded)
JWT_SIGNING_SECRET = "supersecret_jwt_key_123"
TWILIO_AUTH_TOKEN = "0123456789abcdef0123456789abcdef"

DEBUG = True
ALLOW_INSECURE_TLS = True   # disables certificate verification
