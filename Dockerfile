FROM python:3.8-slim as base

COPY . .

RUN pip3 install -r requirements.txt

CMD ["python", "src/main.py"]