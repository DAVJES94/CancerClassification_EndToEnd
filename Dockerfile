FROM python:3.11-slim
WORKDIR /flask_streamlit_app

COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

# Expose necessary ports
EXPOSE 5000
EXPOSE 8501

# Start both Flask and Streamlit when the container runs
CMD ["bash", "-c", "python3 app.py & streamlit run streamlit_app.py --server.port=8501 --server.address=0.0.0.0"]



