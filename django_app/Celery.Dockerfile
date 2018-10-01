FROM python:3.6.4

ENV CELERY_BROKER_URL redis://redis:6379/0
ENV CELERY_RESULT_BACKEND redis://redis:6379/0
ENV C_FORCE_ROOT true

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt && \
    python -m textblob.download_corpora

ENTRYPOINT celery -A django_app worker --loglevel=info