# WeatherWebsite
# 🌦️ Weather App - Real-time Forecasting Platform

## 📌 Overview
This is a **responsive weather forecasting application** built with **Django**.  
It integrates with the **OpenWeatherMap API** to fetch real-time weather data based on user input (city or location).  

The application provides users with accurate weather updates, including temperature, humidity, wind speed, and condition icons with a dynamic UI.

---

## 🚀 Features
- 🌍 Fetch real-time weather data from **OpenWeatherMap API**.  
- 🌡 Display **temperature, humidity, and wind speed**.  
- 🌤 Dynamic UI with **weather condition icons**.  
- 🔍 User input for searching by **city name or location**.  
- 📱 Responsive design for desktop and mobile.  

---

## 🛠️ Tech Stack
- **Backend:** Django (Python)  
- **API:** OpenWeatherMap API  
- **Database:** SQLite (default)  
- **Frontend:** Django Templates, HTML, CSS, Bootstrap  

---

## ⚙️ Installation & Setup

### 🔹 Prerequisites
- Python (>= 3.8)  
- Django installed  
- OpenWeatherMap API key (free from [https://openweathermap.org/api](https://openweathermap.org/api))  

### 🔹 Steps to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/Yogesh-p-079/WeatherApp.git
   cd WeatherApp
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```bash
   python manage.py migrate
   ```

5. Add your **OpenWeatherMap API key** in the Django settings (or `.env` file).

6. Run the server:
   ```bash
   python manage.py runserver
   ```

7. Open the app in your browser:  
   👉 http://127.0.0.1:8000

---

## 📂 Project Structure
```
WeatherApp/
│-- WeatherProject/     # Main Django project
│-- db.sqlite3          # Default SQLite database
│-- manage.py           # Django management script
│-- README.md           # Project documentation
```
---

## 📑 Screenshots (Optional)
_Add screenshots of your UI here_

---

## 🐛 Troubleshooting
- **ModuleNotFoundError: No module named 'django'**  
  → Install Django with `pip install django`  

- **API not working**  
  → Ensure your OpenWeatherMap API key is correct and active.  

---

## 📜 License
This project is open-source under the **MIT License**.

---

## 🔗 Author
👨‍💻 [Yogesh Prajapati](https://github.com/Yogesh-p-079)  
