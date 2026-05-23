FROM python:3.11

WORKDIR /net

RUN pip install flask

COPY sample.py .

EXPOSE 5000

CMD ["python", "sample.py"]
