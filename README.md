# FastAPI Excel Processor Assignment

## Overview

This is a FastAPI application that reads data from an Excel sheet (`/Data/capbudg.xls`) and provides REST API endpoints to interact with the data.

The project demonstrates:
- API development using FastAPI
- Excel processing using Pandas
- Modular code design and error handling
- Clear and professional API documentation

## Setup Instructions

1. Clone the repository.
2. Place the provided `capbudg.xls` file inside the `Data/` folder.
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Run the API server:
    ```bash
    uvicorn app:app --host 0.0.0.0 --port 9090 --reload
    ```

## API Endpoints

Base URL: [http://localhost:9090](http://localhost:9090)

---

### 1️⃣ GET `/list_tables`

- **Description:** Lists all table names (sheet names) in the Excel file.

#### Example Request:
```http
GET http://localhost:9090/list_tables
Example Response:
json

{
  "tables": ["CapBudgWS"]
}

## 2️⃣ GET /get_table_details
Description: Returns the row names (first column values) of the specified table.

Query Parameter:

table_name (required) → Name of the table (sheet name).

Example Request:

GET http://localhost:9090/get_table_details?table_name=CapBudgWS
Example Response:
json

{
  "table_name": "CapBudgWS",
  "row_names": [
    "INITIAL INVESTMENT",
    "Initial Investment=",
    "Opportunity cost (if any)=",
    "Lifetime of the investment",
    "Salvage Value at end of project=",
    "Deprec. method(1:St.line;2:DDB)=",
    "Tax Credit (if any )=",
    "Other invest.(non-depreciable)=",
    ...
  ]
}
3️⃣ GET /row_sum
Description: Returns the sum of all numerical values in the specified row of the given table.

Query Parameters:

table_name (required)

row_name (required)

Example 1: Request

GET http://localhost:9090/row_sum?table_name=CapBudgWS&row_name=Tax%20Credit%20(if%20any%20)=
Example 1: Response
json

{
  "table_name": "CapBudgWS",
  "row_name": "Tax Credit (if any )=",
  "sum": 0.4
}
Example 2: Request

GET http://localhost:9090/row_sum?table_name=CapBudgWS&row_name=Initial%20Investment=
Example 2: Response
json

{
  "table_name": "CapBudgWS",
  "row_name": "Initial Investment=",
  "sum": 90002.0
}

##My Approach on Units
I return the pure numerical sum of all numeric columns for the specified row.
Any units (such as % or $) present in string columns are ignored during the sum calculation.

Potential Improvements
Add support for additional file formats (.csv, .xlsx, .ods).

Allow dynamic Excel upload via API instead of fixed file path.

Implement UI integration using React or Streamlit.

Return units where relevant in the API output (optional enhancement).

Add logging for better debugging.

Missed Edge Cases
Empty Excel sheets.

Tables with no numeric data.

Rows with mixed data types (example: "10%" as a string will not be summed).

Duplicated row names (currently the first matching row is used).

Testing
To facilitate quick testing, a ready Postman collection is provided:

👉 FastAPI_Excel_Processor.postman_collection.json

How to use:
Import the collection into Postman.

Run each request (/list_tables, /get_table_details, /row_sum) to verify functionality.

Author
Shaileja Patil
Batch: B.Tech from Mumbai University 
Course: AI & Data Science