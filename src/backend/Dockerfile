FROM python:3.14-slim 

WORKDIR /app/backend
#кэширование скачивания зависимостей
COPY requirements.txt .

RUN pip install -r requirements.txt
RUN pip install 'pydantic[email]'

COPY . .

WORKDIR /app

RUN python -m backend.main

CMD [ "python", "-m", "uvicorn", "backend.main:app", "--reload", "--host", "0.0.0.0" ]

