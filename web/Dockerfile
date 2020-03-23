FROM  python:3.8
ENV PYTHONUNBUFFERED 1

COPY ./sources/requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt

WORKDIR /app

EXPOSE 5050

CMD python ui_server.py