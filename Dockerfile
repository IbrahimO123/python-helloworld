FROM python:3.9
LABEL maintainer = "Oliyide Ibrahim"

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt


#command to run on cotainer start
CMD [ "python", "app.py" ]




