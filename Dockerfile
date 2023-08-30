FROM python:3.8-slim-buster

EXPOSE 5000

#DONT PRODUCE .PYC FILES
ENV PYTHONDONTWRITEBYTECODE=1

#TURN OFF BUFFERING FOR LOGIN
ENV PYTHONUNBUFFERED=1

#INSTALL REQUIREMENTS
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /app
COPY . /app

#CREATE NON ROOT USER AND ADD PERMISSION TO ACCESS APP DIRECTORY
RUN useradd appuser && chown -R appuser /app
USER appuser

WORKDIR /app/
ENTRYPOINT [ "python3", "-m", "flask", "run", "-h", "0.0.0.0", "-p", "5000" ]
