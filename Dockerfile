FROM python:3.8

COPY ./ ./

RUN pip install -r requirements.txt

ENTRYPOINT ["uvicorn", "app.main:app"]

CMD ["--host", "0.0.0.0", "--port", "8000"]
