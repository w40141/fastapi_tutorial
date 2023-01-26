# python3.9のイメージをダウンロード
FROM python:3.9-buster
ENV PYTHONUNBUFFERED=1

RUN apt update \
    && apt install -y default-mysql-client \
    && apt install --no-install-recommends -y tzdata \
    && apt clean

WORKDIR /src

RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python3 - && \
	cd /usr/local/bin && \
	ln -s /opt/poetry/bin/poetry && \
	poetry config virtualenvs.create false && \
	poetry config virtualenvs.in-project true

COPY pyproject.toml* poetry.lock* ./

RUN if [ -f pyproject.toml ]; then poetry install; fi
