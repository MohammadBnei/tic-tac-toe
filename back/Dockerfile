FROM python
ENV TZ=Europe/Paris
RUN apt-get update && apt-get install -y tzdata
RUN pip install Flask
RUN export PATH="/root/.local/bin:$PATH"
WORKDIR /usr/src/app