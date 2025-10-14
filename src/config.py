import os
import logging
import sys
from dotenv import load_dotenv
from typing import Dict, Any

class Config:
    """Manages environment variables and application settings."""
    
    # Load environment variables from .env file
    # A .env file is REQUIRED for this PoC to run with real credentials.
    load_dotenv()

    # --- Database Configuration (REQUIRED for PoC) ---
    MONGO_URI: str = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
    MONGO_DB_NAME: str = os.getenv("MONGO_DB_NAME", "ugvp")
    # Collection names for vector index and metadata storage
    MONGO_RAG_COLLECTION: str = "data"
    MONGO_SSR_COLLECTION: str = "ugvp_registry"
    
    # --- Protocol Constants ---
    SHI_ALGORITHM: str = "sha256"
    SHI_PREFIX_LENGTH: int = 10 # Length of SHI prefix to use in user-facing markers
    EMBEDDING_DIMENSION: int = 384 # Google's embedding dimension for 'text-embedding-004'
    EMBEDDING_MODEL: str = os.getenv("EMBEDDING_MODEL", "gemini-embedding-001") # Default to a common Google embedding model
    GOOGLE_API_KEY: str = os.getenv("GOOGLE_API_KEY", "") # Google API Key
    
    # ACG Delimiters
    ACG_DELIMITERS: Dict[str, str] = {
        "CLAIM_START": "[",
        "CLAIM_END": "]",
        "CLAIM_SEP": ":",
        "RELATION_START": "(",
        "RELATION_END": ")",
        "RELATION_SEP": ":",
        "RELATION_TYPE_SEP": ":"
    }

    # --- Logging Configuration ---
    LOG_LEVEL: int = logging.DEBUG
    LOG_FORMAT: str = '%(asctime)s - %(levelname)s - %(name)s - %(message)s'

    @classmethod
    def get_db_config(cls) -> Dict[str, str]:
        """Returns the database configuration as a dictionary."""
        return {
            "uri": cls.MONGO_URI,
            "db_name": cls.MONGO_DB_NAME
        }

# Configure logging immediately upon import
LOG_FILE_PATH = os.getenv("LOG_FILE_PATH", "agent.log") # Default log file name

logging.basicConfig(
    format=Config.LOG_FORMAT,
    handlers=[
        logging.FileHandler(LOG_FILE_PATH),
        logging.StreamHandler(sys.stdout) # Keep console output for interactive elements
    ]
)
logging.getLogger("pymongo").setLevel(logging.WARNING)
log = logging.getLogger('UGVP_POC')
log.setLevel(Config.LOG_LEVEL)

# Example .env content:
# MONGO_URI="mongodb+srv://<user>:<password>@<cluster-url>/?"
# GOOGLE_API_KEY="YOUR_GOOGLE_API_KEY"
# EMBEDDING_MODEL="text-embedding-004"
