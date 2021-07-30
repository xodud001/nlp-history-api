FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .

EXPOSE 9001

CMD ["python","app.py"]