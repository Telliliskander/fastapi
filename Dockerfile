FROM python:3.9-alpine AS base

ENV PYROOT /pyroot
ENV PYTHONUSERBASE ${PYROOT}
ENV PATH=${PATH}:${PYROOT}/bin


RUN PIP_USER=1 pip install pipenv 
COPY Pipfile* ./
RUN PIP_USER=1 pipenv install --system --deploy --ignore-pipfile



FROM python:3.9-alpine

ENV PYROOT /pyroot
ENV PYTHONUSERBASE ${PYROOT}
ENV PATH=${PATH}:${PYROOT}/bin

RUN addgroup -S myapp && adduser -S -G myapp user -u 1234
COPY --chown=myapp:user --from=base ${PYROOT}/ ${PYROOT}/

RUN mkdir -p /usr/src/app
WORKDIR /usr/src

COPY --chown=myapp:user app ./app
COPY --chown=myapp:user main.py ./
USER user


CMD ["uvicorn", "main:app","--host", "0.0.0.0", "--port", "8080"]