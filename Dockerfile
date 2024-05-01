FROM python

# set working directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# add requirements (to leverage Docker cache)
ADD ./requirements.txt /usr/src/app/requirements.txt

# install requirements
RUN pip install -r requirements.txt

# add app
ADD . /usr/src/app

# add environment variables
ENV APP_CONFIG=config.DevelopmentConfig
ENV FLASK_APP=playground/__init__.py

# run server
ENTRYPOINT ["python3", "-m", "flask", "run", "--host=0.0.0.0", "--port=80"]
