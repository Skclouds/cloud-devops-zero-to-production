#!/bin/bash
set -e

SOURCE="/tmp/permission-lab/source/config.yaml"
DEST="/tmp/permission-lab/target"

echo "Starting deployment..."
cp "$SOURCE" "$DEST/config.yaml"

echo "Deployment successful"
