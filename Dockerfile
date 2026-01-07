FROM python:3.9-slim
WORKDIR /app
COPY src/ ./src
CMD ["python3", "-c", "from src.feature_engineering import hashed_feature; print(hashed_feature('test'))"]

