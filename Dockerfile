FROM python:3.12-slim

# Installa uv (include uvx)
RUN pip install uv

# Installa browser-use
RUN uv pip install --system browser-use

# Installa il browser (Chromium)
RUN uvx browser-use install

WORKDIR /app
COPY cookies.py .

CMD ["python", "cookies.py"]
