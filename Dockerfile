FROM python:3.10
WORKDIR /app
COPY . .
RUN pip install pandas openpyxl matplotlib
CMD ["sh", "-c", "python subnet_analyzer.py && python visualize.py"]
