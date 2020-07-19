FROM python:3.8

ENV PYTHONPATH=/usr/src/app

WORKDIR /usr/src/app

COPY Pipfile.lock Pipfile ./
RUN pip install -U pip pipenv && pipenv install --system --deploy --ignore-pipfile --dev

COPY . .

RUN chmod +x ./entrypoint.sh

EXPOSE 8081

ENTRYPOINT ./entrypoint.sh
