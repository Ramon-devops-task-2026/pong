FROM python:3.12-slim

#מיקום  של התיקייה הראשית הראשונית שאתה נכנס לקונטיינר
WORKDIR /app

#מהתיקייה במחשב לתיקייה בקונטיינר 
COPY src/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./src/

#פקודה ראשונה שתעבוד שכשמפעילים את הקונטיינר
CMD ["python", "src/main.py"]
