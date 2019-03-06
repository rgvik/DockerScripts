FROM debian:latest

RUN apt-get update && apt-get install -y openssh-server shellinabox supervisor \
    && mkdir -p /var/log/supervisor \
    && sed -i 's/SHELLINABOX_ARGS="--no-beep"/SHELLINABOX_ARGS="--no-beep --disable-ssl"/' /etc/default/shellinabox \
    && mkdir /var/run/sshd \
    && useradd -ms /bin/bash user \
    && echo 'user:user' | chpasswd

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

EXPOSE 22

CMD ["/usr/bin/supervisord"]
