# python3.9のイメージをダウンロード
FROM python:3.9-buster
ENV PYTHONUNBUFFERED=1 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_CREATE=false \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 
    
ENV PATH="$POETRY_HOME/bin:$PATH"

RUN apt-get update \
    && apt-get install -y --no-install-recommends default-mysql-client \
    && apt-get install -y --no-install-recommends tzdata \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /src

SHELL ["/bin/bash", "-o", "pipefail", "-c"]
RUN curl -sSL https://install.python-poetry.org | python3 -

COPY pyproject.toml* poetry.lock* ./

RUN if [ -f pyproject.toml ]; then poetry install; fi
