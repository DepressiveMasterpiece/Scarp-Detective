FROM python:3.11-slim

RUN apt-get update && apt-get install -y wget curl ca-certificates && rm -rf /var/lib/apt/lists/*

RUN wget -O /usr/local/bin/ttyd https://github.com/tsl0922/ttyd/releases/download/1.7.7/ttyd.x86_64 && \
    chmod +x /usr/local/bin/ttyd

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

ENV TERM=xterm-256color
ENV COLORTERM=truecolor

EXPOSE 8080
CMD ["ttyd", "-p", "8080", "-W", "-t", "fontSize=20", "env", "TERM=xterm-256color", "python", "scrap_detective1.py"]
