FROM python:3.9-alpine

WORKDIR /my_file

COPY . /my_file/

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5050

CMD ["python", "main.py" ]
