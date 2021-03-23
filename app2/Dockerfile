FROM python:latest

RUN apt-get update -y
RUN apt-get upgrade -y

COPY ./ /app2
WORKDIR /app2

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 9086

ENTRYPOINT [ "python" ]
CMD [ "application.py" ]
