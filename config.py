from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "database" / "price_tracker.db"
SCHEMA_PATH = BASE_DIR / "database" / "schema.sql"