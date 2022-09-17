FROM python

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# Set work directory
WORKDIR /code
# Install dependencies
COPY ./requirements.txt /code/

ADD ./requirements.txt ./
RUN pip install -r requirements.txt

CMD [ "python", "manage.py", "makemigrations"]