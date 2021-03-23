FROM python:latest

RUN apt-get update -y
RUN apt-get upgrade -y

COPY ./ /app1
WORKDIR /app1

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 9087

ENTRYPOINT [ "python" ]
CMD [ "application.py" ]
