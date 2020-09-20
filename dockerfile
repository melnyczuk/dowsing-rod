FROM python:3.8.5-slim
RUN pip install pipenv
ADD Pipfile Pipfile.lock ./
RUN pipenv install --system --deploy
COPY src ./src
EXPOSE 6666:6666
CMD waitress-serve --port=6666 src.server:server
