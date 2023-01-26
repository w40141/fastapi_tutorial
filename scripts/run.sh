#!/bin/bash

echo "Waiting for mysql to start..."
until mysql $MYSQL_DATABASE -h$MYSQL_HOST -u$MYSQL_USER -p$MYSQL_PASSWORD &>/dev/null; do
	echo mysql "$MYSQL_DATABASE" -h$MYSQL_HOST -u$MYSQL_USER -p$MYSQL_PASSWORD
	sleep 1
done

# 自動マイグレーションを追加
cd /src && poetry run python -m api.db.migrate_db
echo "Done migration"

cd /src && poetry run uvicorn api.main:app --reload --port=8000 --host=0.0.0.0
echo "Start"
