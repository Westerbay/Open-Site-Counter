#!/usr/bin/env bash
set -euo pipefail

APP_NAME="app"

echo "[INFO] Building venv..."
python3 -m venv .venv
source .venv/bin/activate

echo "[INFO] Installing requirements..."
pip install --upgrade pip
pip install -r requirements.txt

echo "[INFO] Zipapp the application..."
TARGET="build/${APP_NAME}.pyz"
mkdir -p build
rm -rf build/*
cp -r src build/__app__
python -m compileall -b build/__app__
python -m zipapp build/__app__ -o "${TARGET}"

python ${TARGET}
