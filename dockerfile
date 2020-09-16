FROM python:3.8.5-slim
ADD Pipfile Pipfile.lock ./
RUN pip install pipenv
RUN pipenv sync
COPY src ./src
CMD pipenv run prod
