FROM python:slim-bookworm

WORKDIR .

COPY . .

RUN pip install poetry && poetry install

CMD ["poetry", "run", "flask", "run", "--host=0.0.0.0"]
