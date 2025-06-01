
FROM python:3.7


WORKDIR /app

COPY . /app/

EXPOSE 8501

RUN pip install -r requirements.txt


CMD ["streamlit", "run", "app.py"]