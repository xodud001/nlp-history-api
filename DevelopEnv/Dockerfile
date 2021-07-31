FROM python:3

WORKDIR /home/app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .

EXPOSE 9001

CMD ["python3","app.py"]