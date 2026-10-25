SKILL NEXIS WEEK 2 — SOLUTIONS USING YOUR ORIGINAL DATASET

This package uses the uploaded file SQL_Sales_Dataset_200_Rows.xlsx.xlsx (200 rows, 10 columns),
not the earlier sample dataset.

FILES
- sql_assignment_solution.sql: SQL queries using the dataset's actual column names.
- python_assignment_solution.py: answers all five Python/Pandas practice questions.
- SQL_Sales_Dataset_200_Rows.xlsx: the original dataset copy required by the Python script.
- week2_python_results.xlsx: actual result tables and analysis.
- actual_dataset_results.txt: summary of results from the uploaded dataset.

PYTHON
Keep the .py and .xlsx files in the same folder. Install dependencies with:
    pip install pandas openpyxl
Then run:
    python python_assignment_solution.py

SQL
Import SQL_Sales_Dataset_200_Rows.xlsx into your SQL tool as a table named `sales`.
Use the column names shown in the SQL file, then run the queries. SQL dialects differ; LIMIT is supported by SQLite/MySQL/PostgreSQL.

NOTE
The SQL PDF's instruction is to find top customers and average order values. The Python practice PDF lists five tasks.
The dataset itself is a spreadsheet, so SQL needs it imported into a database table first.
