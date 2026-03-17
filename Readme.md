# 📊 Drop Sence Analytics Dashboard

A **professional Flask-based analytics dashboard** designed for NGOs to analyze education dropout trends and identify at-risk students across regions, demographics, and time periods.

*(Note: The main application lives inside the `DropSence` directory)*

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.0.0-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

---

## 🎯 Project Overview

Drop Sence helps educational NGOs and institutions:

- **Analyze dropout patterns** across multiple dimensions (region, age, gender, attendance)
- **Identify high-risk groups** requiring intervention
- **Track trends** over academic years
- **Generate actionable insights** automatically
- **Visualize data** through professional interactive charts and graphs

---

## ✨ Features

### 📁 **Dynamic CSV Upload**
- Upload your own education data files
- Real-time validation and error checking
- Automatic analysis and visualization
- No code changes required
- Support for datasets of any size (up to 16MB)

### 📈 Data Analytics
- Comprehensive dropout rate calculations
- Regional analysis with risk assessment
- Age group segmentation
- Gender-based analysis
- Attendance impact evaluation
- Yearly trend tracking

### 📊 Visualizations
1. **Bar Chart**: Dropout Rate by Region
2. **Bar Chart**: Dropout Rate by Age Group
3. **Line Chart**: Yearly Dropout Trend
4. **Pie Chart**: Dropout Distribution by Gender
5. **Scatter Plot**: Attendance vs Academic Performance

### 🎨 Professional UI
- Clean, modern NGO-style design
- Interactive Chart.js visualizations
- Card-based statistics display
- Custom theme toggle (Light / Dark mode)
- Mobile-friendly responsive design

---

## 🚀 Installation & Setup

### Step 1: Navigate to the Application Directory

```bash
cd DropSence
```

### Step 2: Create a Virtual Environment (Recommended)

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Run the Application

```bash
python app.py
```

### Step 5: Access the Dashboard

Open your web browser and navigate to `http://127.0.0.1:5000`. You'll see options to upload your own CSV file for custom analysis or use default datasets if available.

---

## 🔧 Technical Architecture

- **Backend (Flask):** Python-powered data processing API using Pandas and NumPy.
- **Frontend (HTML/CSS):** Vanilla HTML5 and CSS3 for rendering layout templates.
- **Visualizations:** Chart.js handling dynamic chart renders.

---

## ⚖️ License

MIT License - Free for educational and non-profit use.

**© 2026 Drop Sence Analytics Dashboard**
