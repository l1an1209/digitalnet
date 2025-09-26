#!/usr/bin/env bash
# Exit on error
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Create media directory if it doesn't exist
mkdir -p media/noticias

# Set permissions
chmod 755 media
chmod 755 media/noticias

# Create a test image if media directory is empty
if [ ! "$(ls -A media/noticias)" ]; then
    echo "Creating placeholder for media directory..."
    touch media/noticias/.gitkeep
fi
