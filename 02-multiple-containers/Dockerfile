FROM python:alpine3.6

EXPOSE 5000
ENV FLASK_ENV=development
ENV FLASK_APP=/api/api.py
CMD ["flask", "run", "--host=0.0.0.0"]

RUN apk update \
  && apk add --virtual build-deps gcc python3-dev musl-dev \
  && apk add postgresql-dev

COPY ./api /api
RUN pip3 install -r /api/requirements.txt
