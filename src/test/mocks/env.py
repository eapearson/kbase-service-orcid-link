import os

MOCK_KBASE_SERVICES_PORT = 9999
MOCK_ORCID_API_PORT = 9997
MOCK_ORCID_OAUTH_PORT = 9998

TEST_ENV = {
    "KBASE_ENDPOINT": f"http://127.0.0.1:{MOCK_KBASE_SERVICES_PORT}/services/",
    "SERVICE_DIRECTORY": os.environ.get("SERVICE_DIRECTORY"),
    "MONGO_HOST": "mongo",
    "MONGO_PORT": "27017",
    "MONGO_DATABASE": "orcidlink",
    "MONGO_USERNAME": "dev",
    "MONGO_PASSWORD": "d3v",
    "ORCID_API_BASE_URL": f"http://127.0.0.1:{MOCK_ORCID_API_PORT}",
    "ORCID_OAUTH_BASE_URL": f"http://127.0.0.1:{MOCK_ORCID_OAUTH_PORT}",
    "ORCID_SITE_BASE_URL": "https://sandbox.orcid.org",
    "ORCID_CLIENT_ID": "REDACTED-CLIENT-ID",
    "ORCID_CLIENT_SECRET": "REDACTED-CLIENT-SECRET",
    "LINKING_SESSION_RETURN_URL": "https://ci.kbase.us/orcidlink/linkcontinue",
}
