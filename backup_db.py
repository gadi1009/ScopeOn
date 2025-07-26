
import os
import subprocess
import datetime

# Database credentials from environment variables or defaults
DB_NAME = os.getenv("POSTGRES_DB", "coupon_db")
DB_USER = os.getenv("POSTGRES_USER", "user")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD", "password")
DB_HOST = os.getenv("DB_HOST", "localhost") # Use 'db' for Docker internal network
DB_PORT = os.getenv("DB_PORT", "5432")

# Backup directory
BACKUP_DIR = "./db_backups"
os.makedirs(BACKUP_DIR, exist_ok=True)

# Timestamp for backup file
TIMESTAMP = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
BACKUP_FILE = os.path.join(BACKUP_DIR, f"{DB_NAME}-{TIMESTAMP}.sql")

# Command to execute pg_dump
# We set PGPASSWORD in the environment for the subprocess call
command = [
    "pg_dump",
    "-h", DB_HOST,
    "-p", DB_PORT,
    "-U", DB_USER,
    "-d", DB_NAME,
    "-Fc", # Custom format archive file
    "-f", BACKUP_FILE
]

env = os.environ.copy()
env["PGPASSWORD"] = DB_PASSWORD

try:
    # Run the pg_dump command
    subprocess.run(command, check=True, env=env)
    print(f"Database backup successful: {BACKUP_FILE}")
except subprocess.CalledProcessError as e:
    print(f"Database backup failed! Error: {e}")
    if os.path.exists(BACKUP_FILE):
        os.remove(BACKUP_FILE) # Remove incomplete backup file
except FileNotFoundError:
    print("Error: pg_dump command not found. Make sure PostgreSQL client tools are installed and in your PATH.")
