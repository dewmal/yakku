FROM python:3.8-buster
WORKDIR /usr/src/app
#COPY requirements.txt ./
#RUN pip install --no-cache-dir -r requirements.txt

#FROM ceylonapp/fx-engine-base
#WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
#RUN mv .prod.env .local.env

CMD [ "python", "./app.py" ]