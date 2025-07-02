FROM python:3.10.3-alpine

WORKDIR /rustdesk-api-server
ADD . /rustdesk-api-server

# include linux-headers so psutil can build
RUN apk add --no-cache \
      gcc \
      musl-dev \
      linux-headers \
      mariadb-connector-c-dev \
      pkgconfig

RUN set -ex \
  && pip install --no-cache-dir --disable-pip-version-check -r requirements.txt \
  && rm -rf /var/cache/apk/* \
  && cp -r ./db ./db_bak

…
