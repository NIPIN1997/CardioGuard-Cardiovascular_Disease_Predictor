FROM python:3.14
LABEL authors="Nipin"
WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt
COPY /ui /app/ui
COPY /model /app/model
EXPOSE 8501
ENTRYPOINT ["streamlit","run","ui/app.py","--server.port=8501","--server.address=0.0.0.0"]