# 1️⃣ Use an official Python image as the base image
FROM python:3.9

# 2️⃣ Set the working directory inside the container
WORKDIR /app

# 3️⃣ Copy all files from the current directory to the container
COPY . .

# 4️⃣ Install dependencies (Flask)
RUN pip install -r requirements.txt

# 5️⃣ Expose the application’s port
EXPOSE 5000

# 6️⃣ Run the application
CMD ["python", "app.py"]
