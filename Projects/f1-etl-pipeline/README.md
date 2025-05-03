# 🏎️ F1 ETL Pipeline: API → PostgreSQL → Google Sheets → Looker Studio

This project builds a full end-to-end ETL pipeline using public Formula 1 racing data. It extracts data from the Open F1 API, processes it using Python and pandas, loads it into a PostgreSQL database (hosted locally or on Amazon RDS), and visualises the final results through Looker Studio.

---

## 🚀 What pipeline does

1. Extracts race, driver, and weather data from a public API
2. Cleans and transforms the data using Python (`pandas`)
3. Loads the data into a PostgreSQL database
4. Optionally pushes the dataset to Google Sheets
5. Visualises the results using Looker Studio

---

## 🛠️ Tech Stack

- **Python 3.11+**
- **pandas** – for data processing
- **psycopg2** – to connect to PostgreSQL
- **gspread & oauth2client** – for Google Sheets integration
- **python-dotenv** – for managing secrets
- **PostgreSQL (AWS RDS)**
- **Looker Studio** – for data visualisation

---

## 📁 Project Structure
```
f1-etl-project/
│
├── scripts/
│ ├── extract_api_data.py
│ ├── load_to_postgres.py
│ ├── transform_data.py
│ └── load_to_gsheet.py
│
├── config/
│ └── xxx.json (🔐 Google credentials – not in repo)
│
├── .env ← Contains database and API paths (not tracked)
├── .env.example ← Template for your environment variables
├── requirements.txt
└── README.md
```


---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/n-chistyakov/git-repo/tree/main/Projects/f1-etl-pipeline
cd f1-etl-pipeline
```

### 2. Create and activate virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate  # or `.venv\Scripts\activate` on Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

```bash
cp .env.example .env
```

Then update `.env` with your database details and the path to your Google API key (if using Google Sheets).

---

## ▶️ Running the Pipeline

You can run each script manually:

```bash
python scripts/extract_api_data.py
python scripts/load_to_postgres.py
python scripts/transform_data.py
python scripts/load_to_gsheet.py
```

---

## 📊 Visual Output

* Data visualised in **Looker Studio** via Google Sheets connection
* Sample dashboard: [Looker](https://lookerstudio.google.com/s/qUlGVQlW5ao)

---

## 🔒 Security Notes

* `.env` and Google credentials are **excluded** from the repo via `.gitignore`
* Always create your own Google service account key if you wish to run the Google Sheets upload

---

## 🙇‍♂️ Contact

Built by **\[Nikita Chistyakov]**
[LinkedIn](https://www.linkedin.com/in/nikitachistyakov) | [GitHub](https://github.com/n-chistyakov/git-repo)




