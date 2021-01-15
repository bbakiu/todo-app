FROM python:3.8.3-alpine

LABEL author="bbakiu"

ENV TERM=xterm-256color

# Install Python runitme
RUN apk update
RUN pip install --upgrade pip
RUN apk add python3-dev
RUN apk add gpgme-dev
RUN apk add libc-dev
RUN apk add gcc jpeg-dev zlib-dev libffi-dev freetype-dev musl-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev cairo-dev pango-dev gdk-pixbuf-dev
RUN apk add mariadb-dev 

RUN pip3 install virtualenv

# Create virtual envrionment
RUN virtualenv /appenv
RUN . /appenv/bin/activate && \
    pip3 install pip --upgrade
# Add entrypoint script
ADD scripts/entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh
ENTRYPOINT ["entrypoint.sh"]