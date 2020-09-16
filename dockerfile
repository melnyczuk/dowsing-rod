FROM python:3.8.5-slim
ADD app.py Pipfile Pipfile.lock ./
COPY src ./src
RUN pip install pipenv
RUN pipenv sync
EXPOSE 8080:8080
CMD pipenv run prod
