# Web-based ETL Tool (Django + PySpark)

A simple web-based ETL application where users can provide an API URL (with optional headers/auth), fetch data (JSON/XML), and process it using PySpark.  
The backend is built with Django, and Spark is used locally for schema inference and table creation.

This project is intentionally **minimal** — no orchestration, no cloud, no scaling — just core ETL logic end-to-end.

---

## 🚀 Features

- Simple web UI to submit:
  - API URL
  - Headers (optional)
  - Authentication (optional)
- Fetch API response (JSON / XML)
- Infer schema automatically using PySpark
- Convert API response into Spark DataFrame
- Display inferred schema and sample output
- Local Spark execution (no cluster required)

---

## 🧱 Tech Stack

- **Backend**: Django
- **ETL Engine**: PySpark
- **Frontend**: Django Templates (HTML)
- **Language**: Python 3.11
- **Java**: OpenJDK 11 / 17
- **OS**: Windows (tested)

---

## 📁 Project Structure

```text
webETL/
│
├── etl/
│   ├── spark_etl.py        # PySpark ETL logic
│   ├── views.py            # Django views
│   ├── urls.py
│   └── __init__.py
│
├── webETL/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── templates/
│   └── index.html          # Simple UI form
│
├── manage.py
├── requirements.txt
└── README.md
