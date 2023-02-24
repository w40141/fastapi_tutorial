FROM mysql:8.0

RUN apt update \
    && apt install --no-install-recommends -y tzdata \
    && apt clean \
    && rm -rf /var/lib/apt/lists/*

RUN touch /var/log/mysql/mysqld.log
