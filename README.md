#SSB Population Analytics on Databricks (Community Edition)

A lightweight project that explores Norwegian municipality‑level population data (2022 – 2025) entirely on the **free Databricks Community Edition**.

---

## 📂 Project structure

| Path / file                    | Description                                              |
|--------------------------------|----------------------------------------------------------|
| `population_analysis.ipynb`    | Notebook that loads, cleans, and analyses the Excel file |
| `befolkning.xlsx`              | Raw SSB dataset (“Population by region, sex, age…”)      |
| `README.md`                    | This file                                               |

---

## ✨ What the notebook does

1. **Load** &nbsp;`befolkning.xlsx` (official SSB Excel file)  
2. **Clean** &nbsp;out metadata rows, assign clear column names  
3. **Cast** &nbsp;year columns (`2022–2025`) to integers  
4. **Analyses**  

   | Analysis | Purpose |
   |----------|---------|
   | **Time‑series** | Auto‑plot the **3 largest municipalities** (based on 2025 pop.) |
   | **Growth rate** | Top‑10 municipalities by % growth 2022 → 2025 |
   | **Age pyramid** | Bar chart of age classes for a selected municipality |

5. **Visualise** results directly in the Databricks notebook  
6. *(Optional)* One‑click **Databricks dashboard** creation from any plot  

---

## 🛠 Tech stack

- **Databricks Community Edition** (Spark in the cloud, free)
- **PySpark** – fast aggregation
- **Pandas + Matplotlib** – plotting
- **openpyxl** – reading Excel

---

## 🚀 Run it yourself (5 minutes)

### 1. Create / log in to a free Databricks CE workspace  
<https://community.cloud.databricks.com/>

### 2. Upload the files  
1. Go to **Workspace ▶ Users ▶ \<your email>**  
2. **Import ▶ Upload File** → select `population_analysis.ipynb`  
3. Open the notebook  
4. Upload `befolkning.xlsx` via **Files** menu (or `https://community.cloud.databricks.com/files`) → it ends up in `/FileStore/tables/befolkning.xlsx`

### 3. Run the notebook cells  
The code automatically detects the Excel path and produces all plots.

### 4. (Optional) Build a dashboard  
Right‑click any plot ▶ **Create Dashboard** → pin additional visuals.

---

## 📊 Sample output

| Municipality | Population 2025 |
|--------------|----------------:|
| K‑0301 Oslo  | 712 000 |
| K‑4601 Bergen| 283 000 |
| K‑5001 Trondheim | 215 000 |

![timeseries](docs/img/timeseries.png)  
*Fig 1 – Population trend 2022 – 2025 for the three largest municipalities*

---

## 🔌 Local (offline) testing

```bash
python -m venv venv && source venv/bin/activate
pip install pandas openpyxl matplotlib pyspark
python scripts/run_local.py   # simple CLI demo without Databricks
