# Mutual Fund Broker API

This project is a FastAPI-based backend application that facilitates managing mutual fund portfolios and interacting with open-ended mutual fund schemes. The API allows users to view available schemes, make purchases, and track their portfolios.

## Features

- **User Registration & Login**: Allows users to register and log in to the system.
- **Fetch Open-Ended Schemes**: Get a list of open-ended mutual fund schemes.
- **Purchase Mutual Fund**: Allows users to purchase mutual funds and add them to their portfolio.
- **View Portfolio**: View the user's portfolio containing mutual fund details.
- **Get Unique Mutual Fund Families**: Retrieve all unique mutual fund families.
- **Get Schemes by Mutual Fund Family**: Get open-ended schemes based on a specific mutual fund family.

## Requirements

- Python 3.7 or higher
- FastAPI
- SQLAlchemy
- Pydantic
- Uvicorn

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/adityasharma-786/BHIVE.git
   cd mutual_fund_broker
   ```

2. Create a virtual environment:

   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   
   - On Windows:

     ```
     venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```
     source venv/bin/activate
     ```

4. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

5. Set up your database and configure the necessary settings in `app/config.py`.

6. Run the application:

   ```
   uvicorn app.main:app --reload
   ```

   This will start the FastAPI development server at `http://127.0.0.1:8000`.

## API Endpoints

### 1. **User Registration**

- **POST** `/auth/register`
  
  Register a new user with email and password.

  **Request Body**:
  ```json
  {
    "email": "user@example.com",
    "password": "password123"
  }
  ```

  **Response**:
  ```json
  {
    "message": "User registered successfully"
  }
  ```

### 2. **User Login**

- **POST** `/auth/login`
  
  Log in to the application and receive a JWT token.

  **Request Body**:
  ```json
  {
    "email": "user@example.com",
    "password": "password123"
  }
  ```

  **Response**:
  ```json
  {
    "access_token": "your_jwt_token",
    "token_type": "bearer"
  }
  ```

### 3. **Fetch Open-Ended Mutual Fund Schemes**

- **GET** `/mutual-funds/open`
  
  Get a list of all open-ended mutual fund schemes.

  **Response**:
  ```json
  [
    {
      "Scheme_Code": 119551,
      "ISIN_Div_Payout_ISIN_Growth": "INF209KA12Z1",
      "Scheme_Name": "Aditya Birla Sun Life Banking & PSU Debt Fund - DIRECT - IDCW",
      "Net_Asset_Value": 108.3481,
      "Scheme_Type": "Open Ended Schemes",
      "Scheme_Category": "Debt Scheme - Banking and PSU Fund",
      "Mutual_Fund_Family": "Aditya Birla Sun Life Mutual Fund"
    }
  ]
  ```

### 4. **Purchase Mutual Fund**

- **POST** `/mutual-funds/buy`
  
  Buy a mutual fund and add it to the user's portfolio.

  **Request Body**:
  ```json
  {
    "fund_name": "Aditya Birla Sun Life Banking & PSU Debt Fund",
    "units": 10,
    "price_per_unit": 108.3481
  }
  ```

  **Response**:
  ```json
  {
    "message": "Purchase successful",
    "total_value": 1083.481
  }
  ```

### 5. **View Portfolio**

- **GET** `/portfolio`
  
  View the user's mutual fund portfolio.

  **Response**:
  ```json
  [
    {
      "fund_name": "Aditya Birla Sun Life Banking & PSU Debt Fund",
      "units": 10,
      "price_per_unit": 108.3481,
      "total_value": 1083.481
    }
  ]
  ```

### 6. **Get Unique Mutual Fund Families**

- **GET** `/mutual-funds/families`
  
  Get a list of all unique mutual fund families.

  **Response**:
  ```json
  [
    "Aditya Birla Sun Life Mutual Fund",
    "HDFC Mutual Fund"
  ]
  ```

### 7. **Get Schemes by Mutual Fund Family**

- **GET** `/mutual-funds/family/{family_name}`
  
  Get open-ended schemes for a specific mutual fund family.

  **Response**:
  ```json
  [
    {
      "Scheme_Code": 119551,
      "Scheme_Name": "Aditya Birla Sun Life Banking & PSU Debt Fund - DIRECT - IDCW",
      "Net_Asset_Value": 108.3481,
      "Scheme_Category": "Debt Scheme - Banking and PSU Fund"
    }
  ]
  ```

## Testing

You can test the API endpoints using `curl` commands or by using tools like Postman.
postman collection - https://api.postman.com/collections/25968910-fd6d3011-c425-4079-8ffd-a17236ea4e98?access_key=PMAT-01JE0XDN8C7N7TCWPAB77MD5PG
