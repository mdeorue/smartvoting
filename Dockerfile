from python:3.7-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip --no-cache-dir install -r requirements.txt

COPY . /app

ENV FLASK_APP=entrypoint:app
ENV FLASK_ENV=production
ENV APP_SETTINGS_MODULE=config.default

CMD ["python", "entrypoint.py"]