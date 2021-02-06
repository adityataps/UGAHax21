FROM python:3.9.0

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN mkdir /code
RUN mkdir /code/staticfiles
WORKDIR /code

RUN pip install --upgrade pip
COPY ./requirements.txt /code/
RUN pip install -r requirements.txt

run apt-get update && apt-get install -y netcat


COPY ./ /code/
ENTRYPOINT ["/bin/bash", "/code/entrypoint.sh"]

