from fastapi import FastAPI, HTTPException, Query
import pandas as pd
import os

# Initialize FastAPI app
app = FastAPI()

# Path to Excel file
EXCEL_PATH = "./Data/capbudg.xls"

# Read Excel into dictionary of DataFrames
def load_excel_data():
    try:
        xl = pd.ExcelFile(EXCEL_PATH)
        sheet_names = xl.sheet_names
        data_frames = {sheet: xl.parse(sheet) for sheet in sheet_names}
        return sheet_names, data_frames
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error reading Excel file: {e}")

# Load data once when the app starts
TABLE_NAMES, TABLE_DATA = load_excel_data()

@app.get("/")
def root():
    return {"message": "FastAPI Excel Processor is running!"}

@app.get("/list_tables")
def list_tables():
    return {"tables": TABLE_NAMES}

@app.get("/get_table_details")
def get_table_details(table_name: str = Query(..., description="Name of the table")):
    if table_name not in TABLE_DATA:
        raise HTTPException(status_code=404, detail=f"Table '{table_name}' not found.")
    
    df = TABLE_DATA[table_name]

    # Assuming first column holds row names
    first_col = df.columns[0]
    row_names = df[first_col].dropna().astype(str).tolist()

    return {
        "table_name": table_name,
        "row_names": row_names
    }

@app.get("/row_sum")
def row_sum(
    table_name: str = Query(..., description="Name of the table"),
    row_name: str = Query(..., description="Name of the row")
):
    if table_name not in TABLE_DATA:
        raise HTTPException(status_code=404, detail=f"Table '{table_name}' not found.")
    
    df = TABLE_DATA[table_name]
    first_col = df.columns[0]

    # Find the row matching the given row_name
    row_series = df[df[first_col].astype(str) == row_name]

    if row_series.empty:
        raise HTTPException(status_code=404, detail=f"Row '{row_name}' not found in table '{table_name}'.")

    # Improved and safe numeric sum:
    row_data = row_series.drop(columns=[first_col]).iloc[0]

    # Try to convert each value to float, ignore errors
    numeric_values = pd.to_numeric(row_data, errors='coerce')

    # Now sum only numeric values (non-NaN)
    total_sum = numeric_values.dropna().sum()

    return {
        "table_name": table_name,
        "row_name": row_name,
        "sum": float(total_sum)  # Convert to float for consistent API response
    }

