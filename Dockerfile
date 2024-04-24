FROM python:3.9

WORKDIR /api/
RUN apt-get update
RUN apt-get install -y wget 

RUN python3 -m venv /opt/venv

COPY . /api/

RUN /opt/venv/bin/pip install -r requirements.txt --progress-bar off

CMD ["/opt/venv/bin/python", "main.py"]
