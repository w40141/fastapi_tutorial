#!/bin/bash

# 自動マイグレーションを追加
cd /src && poetry run python -m api.db.migrate_db
echo "Done migration"

cd /src && poetry run uvicorn api.main:app --reload --port=8000 --host=0.0.0.0
echo "Start"
