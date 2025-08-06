FROM ubuntu:22.04
LABEL org.opencontainers.image.authors="Antonio Russi"

RUN apt-get update && \
    apt install -y python3 && \
    apt install -y python3-pip && \
    apt install -y curl && \
    apt install -y unzip && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y tzdata && \
    apt-get clean

ADD https://downloads.rclone.org/rclone-current-linux-amd64.zip .

RUN unzip rclone-current-linux-amd64.zip && \
    cd rclone-*-linux-amd64 && \
    cp rclone /usr/bin/ && \
    chown root:root /usr/bin/rclone && \
    chmod 755 /usr/bin/rclone

COPY . .

RUN pip install -r requirements.txt &&  \
    pip install gunicorn

ENV PYTHONUNBUFFERED=1

CMD ["gunicorn", "--bind", "0.0.0.0:8080", "--workers=4", "--threads=8", "--timeout=600", "app:app"]