# 🎭 Playwright Learning -- Udemy (Python)

This repository contains my **hands-on learning and practice work** for
**Playwright Automation using Python**, based on Udemy training and
real-world QA automation scenarios.

It covers **UI Automation, API Testing, and E2E testing concepts** using
**Playwright + Pytest**.

------------------------------------------------------------------------

## 📌 Tech Stack

-   **Language:** Python\
-   **Automation Tool:** Playwright\
-   **Test Framework:** Pytest\
-   **Reporting:** Pytest HTML (optional)\
-   **Version Control:** Git & GitHub

------------------------------------------------------------------------

## 📂 Project Structure

    playwright-learning-udemy/
    │
    ├── tests/
    │   ├── test_login.py
    │   ├── test_ui_basic.py
    │   ├── test_api_get.py
    │   ├── test_api_post.py
    │   └── test_e2e_web_api.py
    │
    ├── utils/
    │   ├── apiBase.py
    │   └── config.py
    │
    ├── playwright.config.py
    ├── pytest.ini
    ├── requirements.txt
    ├── .gitignore
    └── README.md

------------------------------------------------------------------------

## 🚀 Features Covered

### ✅ UI Automation

-   Login page automation
-   Form handling
-   Dropdowns, checkboxes, alerts
-   Window & tab handling
-   Assertions using `expect`

### ✅ API Testing

-   GET requests
-   POST requests
-   API request context
-   Token-based authentication
-   JSON response validation

### ✅ E2E Testing

-   Create order via API
-   Capture Order ID
-   Validate order in UI
-   API + UI integration flow

------------------------------------------------------------------------

## ⚙️ Setup & Installation

### 1️⃣ Clone the Repository

``` bash
git clone https://github.com/<your-username>/playwright-learning-udemy.git
cd playwright-learning-udemy
```

### 2️⃣ Create Virtual Environment

``` bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
```

### 3️⃣ Install Dependencies

``` bash
pip install -r requirements.txt
```

### 4️⃣ Install Playwright Browsers

``` bash
playwright install
```

------------------------------------------------------------------------

## ▶️ Running Tests

### Run All Tests

``` bash
pytest
```

### Run Specific Test File

``` bash
pytest tests/test_login.py
```

### Run in Headed Mode

``` bash
pytest --headed
```

------------------------------------------------------------------------

## 📖 Learning Objective

-   Build a **strong foundation** in Playwright with Python
-   Gain **real interview-level confidence**
-   Understand **real-world automation framework design**
-   Practice **API + UI combined E2E testing**

------------------------------------------------------------------------

## 👤 Author

**Shankar G**\
QA Engineer \| Manual & Automation Testing\
Playwright (Python) \| API \| E2E Testing

------------------------------------------------------------------------

⭐ This repository is created for **learning and interview preparation
purposes**.
