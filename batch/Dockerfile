FROM python:3.14-slim
WORKDIR /app
COPY main.py .
ARG GIT_SHA=unknown
ENV GIT_SHA=$GIT_SHA
ENV BATCH_NAME=nightly-etl
ENTRYPOINT ["python", "main.py"]