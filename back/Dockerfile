FROM python

ENV TZ=Europe/Paris
ENV PATH="/root/.local/bin:${PATH}"

RUN apt-get update && apt-get install -y tzdata
RUN pip install Flask
RUN pip install flask-bcrypt
RUN pip install flask-restful
RUN pip install flask-jwt-extended
RUN pip install flask-mail
RUN pip install flask-mongoengine
WORKDIR /usr/src/app