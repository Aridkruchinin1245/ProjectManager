FROM python:alpine 

WORKDIR /app

COPY . .

WORKDIR /app

RUN pip install -r backend/requirements.txt
RUN pip install 'pydantic[email]'

CMD [ "python", "-m", "uvicorn", "backend.main:app", "--reload", "--host", "0.0.0.0" ]

