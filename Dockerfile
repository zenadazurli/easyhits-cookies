FROM python:3.12-slim

# Installa uv (include uvx)
RUN pip install uv

# Installa browser-use con uv (usa --system per evitare ambiente virtuale)
RUN uv pip install --system browser-use

# Installa il browser
RUN uvx browser-use install

WORKDIR /app
COPY cookies.py .

CMD ["python", "cookies.py"]
