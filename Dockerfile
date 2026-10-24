FROM python:3.11-slim
RUN apt-get update && apt-get install -y ttyd
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8080
CMD ["ttyd", "-p", "8080", "-W", "python", "scrap_detective1.py"]