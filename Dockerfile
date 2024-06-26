FROM python:3.9-alpine

RUN pip install pipenv 
RUN mkdir -p /usr/src/app/app
WORKDIR /usr/src/app
COPY Pipfile Pipfile.lock main.py ./
COPY app ./app

RUN pipenv install --system  
RUN addgroup -S myapp && adduser -S -G myapp user -u 1234
USER user

CMD ["uvicorn", "main:app","--host", "0.0.0.0", "--port", "8080"]