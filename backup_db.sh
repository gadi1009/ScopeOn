
#!/bin/bash

# Database credentials from docker-compose.yml
DB_NAME="coupon_db"
DB_USER="user"
DB_PASSWORD="password"
DB_HOST="localhost"
DB_PORT="5432"

# Backup directory
BACKUP_DIR="./db_backups"
mkdir -p $BACKUP_DIR

# Timestamp for backup file
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
BACKUP_FILE="$BACKUP_DIR/$DB_NAME-$TIMESTAMP.sql"

# Perform the backup
PGPASSWORD=$DB_PASSWORD pg_dump -h $DB_HOST -p $DB_PORT -U $DB_USER -d $DB_NAME > $BACKUP_FILE

if [ $? -eq 0 ]; then
  echo "Database backup successful: $BACKUP_FILE"
else
  echo "Database backup failed!"
  rm -f $BACKUP_FILE # Remove incomplete backup file
fi
