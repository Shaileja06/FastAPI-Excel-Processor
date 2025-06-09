# FastAPI Excel Processor Assignment

## Overview:
This FastAPI application reads data from an Excel file (/Data/capbudg.xls) and exposes REST API endpoints to access and process the data. It demonstrates:

* API development using FastAPI
* Excel processing with pandas
* Modular design and error handling
* Auto-generated documentation via FastAPI

## Setup Instructions:

1. Clone the repository.
2. Place the provided capbudg.xls file inside the Data/ folder.
3. Install dependencies:
   pip install -r requirements.txt
4. Run the API server:
   uvicorn app\:app --host 0.0.0.0 --port 9090 --reload

## API Endpoints:
### Base URL: [http://localhost:9090](http://localhost:9090)

#### 1️⃣ GET /list\_tables

Description: Returns all sheet names (tables) available in the Excel file.

Example Request:
GET [http://localhost:9090/list\_tables](http://localhost:9090/list_tables)

Example Response:
{
"tables": \["CapBudgWS"]
}

#### 2️⃣ GET /get\_table\_details

Description: Returns all row names (first column values) of a given sheet/table.

Query Parameters:

* table\_name (required): Name of the sheet to inspect

Example Request:
GET [http://localhost:9090/get\_table\_details?table\_name=CapBudgWS](http://localhost:9090/get_table_details?table_name=CapBudgWS)

Example Response:
```
{
"table\_name": "CapBudgWS",
"row\_names": \[
"INITIAL INVESTMENT",
"Initial Investment=",
"Opportunity cost (if any)=",
"Lifetime of the investment",
"Salvage Value at end of project=",
"Deprec. method(1\:St.line;2\:DDB)=",
"Tax Credit (if any )=",
"Other invest.(non-depreciable)=",
...
]
}
```

#### 3️⃣ GET /row\_sum

Description: Returns the sum of all numeric values in a given row from the specified table.

Query Parameters:

* table\_name (required)
* row\_name (required)

Example Request 1:
GET [http://localhost:9090/row\_sum?table\_name=CapBudgWS\&row\_name=Tax%20Credit%20(if%20any%20)=](http://localhost:9090/row_sum?table_name=CapBudgWS&row_name=Tax%20Credit%20%28if%20any%20%29=)

Example Response 1:
```
{
"table\_name": "CapBudgWS",
"row\_name": "Tax Credit (if any )=",
"sum": 0.4
}
```
Example Request 2:
GET [http://localhost:9090/row\_sum?table\_name=CapBudgWS\&row\_name=Initial%20Investment=](http://localhost:9090/row_sum?table_name=CapBudgWS&row_name=Initial%20Investment=)

Example Response 2:
```
{
"table\_name": "CapBudgWS",
"row\_name": "Initial Investment=",
"sum": 90002.0
}
```

#### Approach on Units:
The sum includes only numeric values. Textual content like "%" or "\$" is ignored. Only clean numeric columns are summed.

Potential Improvements:

* Support other formats like .csv, .xlsx, .ods
* Enable dynamic Excel file upload via API
* Add frontend (React/Streamlit)
* Return units where available
* Add logging for debugging

Known Limitations:

* Empty Excel sheets not handled
* Sheets with no numeric data
* Mixed-type rows (e.g. strings like "10%") ignored
* Duplicate row names (first match used)

Testing:
A Postman collection is included: FastAPI\_Excel\_Processor.postman\_collection.json

Usage:

* Import collection in Postman
* Run /list\_tables, /get\_table\_details, and /row\_sum endpoints to test

Author:
Shaileja Patil |
B.Tech - Mumbai University |
Course: AI & Data Science

---
