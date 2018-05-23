FROM python:alpine3.6

EXPOSE 5000
ENV FLASK_ENV=development
ENV FLASK_APP=/api/api.py
CMD ["flask", "run", "--host=0.0.0.0"]

COPY ./api /api
RUN pip3 install -r /api/requirements.txt
