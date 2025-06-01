

#Base Image
FROM python:3.9

#Working Directory
WORKDIR /app 

#COPY 
COPY . /app/

#RUN 
RUN pip install -r requirements.txt

#EXPOSE
EXPOSE 8000

#CMD
CMD ["uvicorn", "main:app" , "--host" , "0.0.0.0" , "--port" , "8000" ]

