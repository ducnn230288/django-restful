FROM python:3.11.6-alpine
LABEL maintainer="langphongmtb"

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

ENV APP_ROOT=/app

COPY . ${APP_ROOT}
WORKDIR ${APP_ROOT}
EXPOSE 8000

ARG DEV=false
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apk add --upgrade --no-cache postgresql-client && \
    apk add --upgrade --no-cache --virtual .tmp-build-deps \
        build-base postgresql-dev musl-dev && \
    /py/bin/pip install -r requirements.txt && \
    if [ $DEV = "true" ]; \
      then /py/bin/pip install -r requirements.dev.txt ; \
    fi && \
    rm -rf requirements.txt && \
    rm -rf requirements.dev.txt && \
    apk del .tmp-build-deps && \
    adduser \
        --disabled-password \
        --no-create-home \
        django-user

ENV PATH="/py/bin:$PATH"

USER django-user