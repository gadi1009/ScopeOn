#!/bin/bash

# Database credentials from docker-compose.yml
DB_NAME="coupon_db"
DB_USER="user"
DB_PASSWORD="password"
DB_HOST="localhost" # Use 'localhost' if running from host, 'db' if running inside another container
DB_PORT="5432"

# Backup directory
BACKUP_DIR="./db_backups"
mkdir -p $BACKUP_DIR

# Timestamp for backup file
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
BACKUP_FILE="$BACKUP_DIR/$DB_NAME-$TIMESTAMP.sql"

# Wait for PostgreSQL to be ready
MAX_RETRIES=10
RETRY_INTERVAL=5

echo "Waiting for PostgreSQL to be ready..."
for i in $(seq 1 $MAX_RETRIES);
do
  PGPASSWORD=$DB_PASSWORD pg_isready -h $DB_HOST -p $DB_PORT -U $DB_USER > /dev/null 2>&1
  if [ $? -eq 0 ]; then
    echo "PostgreSQL is ready!"
    break
  else
    echo "Attempt $i/$MAX_RETRIES: PostgreSQL not ready. Retrying in $RETRY_INTERVAL seconds..."
    sleep $RETRY_INTERVAL
  fi
done

PGPASSWORD=$DB_PASSWORD pg_isready -h $DB_HOST -p $DB_PORT -U $DB_USER > /dev/null 2>&1
if [ $? -ne 0 ]; then
  echo "Error: PostgreSQL did not become ready after multiple attempts. Aborting backup."
  exit 1
fi

# Perform the backup
PGPASSWORD=$DB_PASSWORD pg_dump -h $DB_HOST -p $DB_PORT -U $DB_USER -d $DB_NAME > $BACKUP_FILE

if [ $? -eq 0 ]; then
  echo "Database backup successful: $BACKUP_FILE"
else
  echo "Database backup failed!"
  rm -f $BACKUP_FILE # Remove incomplete backup file
  exit 1
fi