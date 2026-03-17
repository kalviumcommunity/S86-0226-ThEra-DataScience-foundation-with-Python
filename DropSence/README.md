# 📊 Drop Sence Analytics Dashboard

A **professional Flask-based analytics dashboard** designed for NGOs to analyze education dropout trends and identify at-risk students across regions, demographics, and time periods.

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

### 💡 Automated Insights
- Identifies highest-risk regions
- Highlights vulnerable age groups
- Detects attendance thresholds linked to dropout
- Analyzes gender disparities
- Tracks year-over-year trends

### 🎨 Professional UI
- Clean, modern NGO-style design
- Interactive Chart.js visualizations
- Card-based statistics display
- Responsive grid layouts
- Custom theme toggle (Light / Dark mode)
- Mobile-friendly responsive design

---

## 🏗️ Project Structure

```
DropSence/
│
├── app.py                      # Main Flask application
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
│
├── data/                       # Contains dataset files
│
├── static/
│   └── style.css               # Dashboard styling
│
└── templates/
    ├── index.html              # Upload page template
    ├── dashboard.html          # Main dashboard template
    ├── visual_analytics.html   # Charts and graphs template
    ├── documentation.html      # Technical docs template
    ├── about.html              # About page template
    └── error.html              # Error handling template
```

---

## 🚀 Installation & Setup

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Step 1: Navigate to the Project

```bash
cd path/to/DropSence
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

Open your web browser and navigate to:
```
http://127.0.0.1:5000
```

You'll see options to upload your own CSV file for custom analysis or use default datasets if available.

---

## 📤 Uploading Your Data

### Quick Upload

1. Visit `http://127.0.0.1:5000`
2. Click "Choose CSV File"
3. Select your education dataset requirements
4. Click "Process & Analyze"
5. View your custom dashboard!

### CSV Requirements

Your CSV file can be flexible, but should generally include data pertaining to:
- Age (or Years, StudentAge)
- Gender (or Sex, M/F)
- Attendance (or AttendanceRate, Present%)
- Score (or Marks, Grade, TestScore)
- Dropout (or Status, Left, Discontinued)

If ID, School, Region, or Year are missing, the system will automatically generate them for you.

---

## 🔧 Technical Architecture

### Backend (Flask)

- Data loading and intelligent column mapping
- Data cleaning and preprocessing
- Statistical calculations using Pandas and NumPy
- Advanced API routing

### Frontend 

- HTML5, modern vanilla CSS3
- Chart.js for all interactive animations and dynamic graphing
- Lucide icons for rich SVG iconography

---

## 🛡️ Error Handling

The system handles:
- Missing dataset file
- Invalid CSV format
- Empty datasets
- Missing required columns
- Data type mismatches

Provides user-friendly error messages with troubleshooting steps on a dedicated error page.

---

## 🔌 API Endpoint

### GET `/api/stats`

Returns JSON with statistics and insights:

```json
{
  "statistics": {
    "total_students": 150,
    "total_dropouts": 45,
    "dropout_rate": 30.0,
    "avg_attendance": 72.5,
    "avg_score": 68.3
  },
  "insights": [
    "Region South has the highest dropout rate...",
    "Age group 16-20 shows the highest dropout risk..."
  ],
  "status": "success"
}
```

---

## 🚀 Deployment Considerations

### Production Deployment

For production use:

1. Set `debug=False` in `app.py`
2. Use a production WSGI server (Gunicorn, uWSGI)
3. Configure proper security settings
4. Implement user authentication if needed

---

## ⚖️ License

MIT License - Free for educational and non-profit use.

---

**© 2026 Drop Sence Analytics Dashboard**  
*Empowering NGOs with data-driven insights for better education outcomes*ern CSS3 and HTML5
- Data science best practices

---

**© 2026 Education Dropout Analytics Dashboard**  
*Empowering NGOs with data-driven insights for better education outcomes*
