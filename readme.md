

---


# 🌫️ Delhi Air Quality Index (AQI) Animator

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![Visualization](https://img.shields.io/badge/Data%20Visualization-Matplotlib%20%7C%20Geo--Mapping-orange)
![Environment](https://img.shields.io/badge/Domain-Environmental%20Analytics-green)
![Status](https://img.shields.io/badge/Project-Portfolio%20Ready-success)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

A Python-based visualization project that animates **spatio-temporal air quality trends** across Delhi using AQI data, producing an intuitive **time-lapse GIF**.

---

## 📑 Table of Contents
- [About the Project](#about-the-project)
- [Features](#features)
- [Visualization Preview](#visualization-preview)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Data Source](#data-source)
- [Future Improvements](#future-improvements)

---

## 📌 About the Project

This project visualizes **urban air quality dynamics** by generating an animated map of **Air Quality Index (AQI)** values over time.

Focusing on **Delhi, India**, it simulates (and can later integrate real) AQI measurements from multiple monitoring stations and converts them into a **geographically accurate animated GIF**.

### 🎯 Objectives
- Understand **spatio-temporal pollution patterns**
- Enable **visual storytelling** for environmental data
- Support **research, awareness, and urban analytics**

---

## ✨ Features

- **Daily AQI Simulation**  
  Simulates AQI values for major monitoring stations (placeholder for real CPCB/API data)

- **Geospatial Visualization**  
  Maps AQI values to real station coordinates with color-coded markers

- **Animated Time Series Output**  
  Compiles daily frames into a smooth animated GIF

- **Standard AQI Color Coding**  
  Uses CPCB-compliant AQI categories:
  - Good
  - Satisfactory
  - Moderate
  - Poor
  - Very Poor
  - Severe

---

## 🌍 Visualization Preview

![Delhi AQI Animation](https://github.com/Quantamaster/Air-Quality/blob/main/delhi_aqi_animation.gif)

---

## 🚀 Getting Started

### Prerequisites

Ensure the following are installed:

- **Python 3.8+**
- **pip** (comes with Python)

Optional (for extended geospatial features):
- `geopandas`
- `folium`

---

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/Quantamaster/Air-Quality.git
cd Air-Quality
````

2. **Create a virtual environment (recommended)**

```bash
python -m venv .venv
```

3. **Activate the virtual environment**

**Windows**

```bash
.venv\Scripts\activate
```

**Linux / macOS**

```bash
source .venv/bin/activate
```

4. **Install dependencies**

```bash
pip install pandas matplotlib imageio requests
```

> ℹ️ `imageio` works natively for GIF generation. `ffmpeg` is only needed for video formats.

---

## ▶️ Usage

1. Ensure the virtual environment is active
2. Run the main script:

```bash
python p1.py
```

### Output

* 📁 `aqi_frames/` → Individual map frames
* 🖼️ `delhi_aqi_animation.gif` → Final animated visualization

---

## 🗂️ Project Structure

```
Air-Quality/
│
├── delhi_aqi_animation.gif   # Final animated AQI output
├── p1.py                     # Main script
├── aqi_frames/               # Generated map frames
└── README.md                 # Documentation
```

---

## 📊 Data Source

* Currently uses **simulated AQI values**
* Designed for seamless integration with:

  * CPCB AQI API
  * OpenAQ
  * State pollution boards

---

## 🔮 Future Improvements

* ✅ Integrate **real-time AQI APIs**
* ✅ Extend to **multiple Indian cities**
* ✅ Visualize individual pollutants (PM2.5, NO₂, O₃)
* ✅ Add **interactive web dashboard (Streamlit/Folium)**
* ✅ Enable **monthly & yearly comparisons**

---

⭐ If you find this project useful, consider **starring the repository**!

```

---



Just tell me 👍
```

