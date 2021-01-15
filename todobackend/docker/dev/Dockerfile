FROM bujarbakiu/todo:latest

LABEL author=bujarbakiu

# Install dev/build dependencies
RUN apk upgrade --update && \
    apk add --no-cache python3 python3-dev

RUN apk add --no-cache mysql-client
# Activate virtual env and install wheel support
RUN pip --version
RUN python -m pip install --user --upgrade pip
RUN pip install wheel --upgrade

# PIP envrionment varibales 
ENV WHEELHOSE=/wheelhouse PIP_WHEEL_DIR=/wheelhouse PIP_FIND_LINKS=/wheelhouse XDG_CACHE_HOME=/cache

# OUTPUT: build artifacts (Wheels) output
VOLUME [ "/wheelhouse" ]

# OUTPUT: Test reports output
VOLUME [ "/reports" ]

# Add test entrypoint
COPY scripts/test.sh /usr/local/bin/test.sh
RUN chmod +x /usr/local/bin/test.sh

# Set dafaults for entrypoint and command string
ENTRYPOINT ["test.sh"]
CMD ["python3", "manage.py", "test", "--noinput"]

COPY src /application
WORKDIR /application