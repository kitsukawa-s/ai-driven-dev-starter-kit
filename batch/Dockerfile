FROM python:3.12-slim
WORKDIR /app
COPY main.py .
ENV BATCH_NAME=nightly-etl
ENTRYPOINT ["python", "main.py"]