FROM python:3-alpine

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
  && rm -rf /var/cache/apk/* 

ENV HOST="0.0.0.0"
ENV PYTHONUNBUFFERED=1

EXPOSE 21114/tcp
EXPOSE 21114/udp

HEALTHCHECK --interval=30s --timeout=5s --retries=3 CMD wget --spider 0.0.0.0:21114

ENTRYPOINT ["sh", "run.sh"]
