FROM python:slim

WORKDIR /tgbot
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./TGinsta_photobot.py" ]
