FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# create non-root user and group
RUN groupadd --gid 10001 app && \
    useradd --uid 10001 --gid app --no-create-home app

COPY src/ .

ARG APP_VERSION=dev
ENV APP_VERSION=${APP_VERSION}

USER 10001

EXPOSE 8080

CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app:app"]