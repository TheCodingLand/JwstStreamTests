FROM python:3.10-rc-buster

RUN apt-get update && apt-get install --no-install-recommends --no-install-suggests -y curl
RUN apt-get -y install build-essential
COPY requirements.txt . 
RUN pip install -r requirements.txt

COPY main.py main.py

CMD ["python" ,"main.py"]
