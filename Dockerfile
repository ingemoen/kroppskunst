FROM python:latest


RUN apt-get upgrade -y
RUN apt-get update

# This prevents Python from writing out pyc files
ENV PYTHONDONTWRITEBYTECODE 1

# This keeps Python from buffering stdin/stdout
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

COPY . .

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

EXPOSE 8080
ENV FLASK_DEBUG 1
ENV FLASK_ENV development

ENTRYPOINT [ "/bin/bash",  "./server.sh" ]
# ENTRYPOINT [ "/bin/bash" ]
# ENTRYPOINT [ "python", "src/app.py" ]