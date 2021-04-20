FROM docker.io/python:3.7-slim

EXPOSE 8080

WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . ./

ENV API_KEY=41e1dc1e-ccda-4cfa-9fbc-c10b9fd8c0ba
ENV IS_LOCAL true

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]