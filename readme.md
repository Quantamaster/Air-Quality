# Delhi Air Quality Index Animator



## Table of Contents
- [About The Project](#about-the-project)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Data Source](#data-source)
- [Future Improvements](#future-improvements)
-
## About The Project

This project provides a Python-based solution to visualize urban air quality index (AQI) data over time as an animated GIF. Focusing specifically on Delhi, India, it fetches simulated (or real, if integrated) air quality data across various monitoring stations for a specified month and generates a time-lapse animation depicting the changing pollution levels geographically.

The primary goal is to offer an intuitive visual tool for understanding spatio-temporal trends in air quality, which can be beneficial for environmental studies, public awareness, and preliminary urban planning insights.

## Features

* **Daily AQI Data Simulation:** Simulates daily (hourly, in the backend logic) AQI data for a set of prominent monitoring stations in Delhi. (Note: This is currently a placeholder for actual CPCB data fetching).
* **Spatio-Temporal Visualization:** Generates individual map frames for each time step, showing AQI levels represented by color-coded markers at each station's geographical location.
* **Animated Output:** Compiles individual map frames into a single GIF animation for a dynamic visualization of air quality changes over a month.
* **AQI Color Categorization:** Utilizes standard AQI color codes (Good, Satisfactory, Moderate, Poor, Very Poor, Severe) for easy interpretation.

## 🌫️ Delhi AQI Visualization

![delhi_aqi_animation](https://github.com/Quantamaster/Air-Quality/blob/main/delhi_aqi_animation.gif)


## Getting Started

This section will guide you through setting up and running the project on your local machine.

### Prerequisites

Before you begin, ensure you have the following installed:

* **Python 3.x:** (e.g., Python 3.8+)
    * You can download it from [python.org](https://www.python.org/downloads/).
* **pip:** Python's package installer (usually comes with Python).

### Installation

1.  **Clone the repository (if applicable):**
    If this project is in a Git repository, clone it:
    ```bash
    git clone [https://github.com/your_username/Delhi-AQI-Animator.git](https://github.com/your_username/Delhi-AQI-Animator.git)
    cd Delhi-AQI-Animator
    ```
    If not, just navigate to your project directory:
    ```bash
    cd C:\Users\abc\PycharmProjects\Air_Quality _Index\
    ```

2.  **Create a Virtual Environment (Recommended):**
    It's good practice to create a virtual environment to manage project dependencies.
    ```bash
    python -m venv .venv1  # Or whatever you named your venv
    ```

3.  **Activate the Virtual Environment:**
    * **Windows:**
        ```bash
        .venv1\Scripts\activate
        ```
    * **macOS/Linux:**
        ```bash
        source .venv1/bin/activate
        ```

4.  **Install Dependencies:**
    Install the required Python packages using pip:
    ```bash
    pip install pandas matplotlib imageio requests # folium geopandas (if you expand mapping capabilities)
    ```
    *Note: `imageio` might require `ffmpeg` for certain video formats. For GIF, it often works without it.*

## Usage

Once installed, you can run the script to generate the AQI animation.

1.  **Ensure your virtual environment is active.** (See Installation Step 3)

2.  **Run the main script:**
    ```bash
    python p1.py
    ```

3.  **Output:**
    The script will print progress messages for data fetching. Upon successful completion, it will generate:
    * Individual PNG image frames in an `aqi_frames/` directory within your project root.
    * A compiled GIF animation named `delhi_aqi_animation.gif` in the project root directory.

    Navigate to your project root folder (`C:\Users\abc\PycharmProjects\Air_Quality _Index\`) to view the `delhi_aqi_animation.gif`.

## Project Structure

Air-Quality/
├── delhi_aqi_animation.gif   # Resulting animation
├── p1.py                     # Main script generating frames & GIF
├── aqi_frames/               # (Optional) generated image frames
└── README.md                 # This project description


## Future Improvements

Here are some ideas you might implement next:

✅ Integrate actual AQI data from public APIs
✅ Add support for other cities
✅ Plot additional pollutants (PM2.5, NO₂, O₃, etc.)
✅ Create web dashboard for interactive browsing


