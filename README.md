# Birthday Party Confirmation API

A FastAPI application that handles birthday party confirmations, built with Python 3.x and leveraging the power of the uvicorn ASGI server. The project includes a single router for handling confirmation requests.

## Technologies Used

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Uvicorn](https://img.shields.io/badge/Uvicorn-ASGI%20Server-green.svg)](https://www.uvicorn.org/en/latest/)
[![FastAPI](https://img.shields.io/badge/FastAPI-Web%20Framework-blue.svg)](https://fastapi.tiangolo.com/)
[![Language](https://img.shields.io/badge/Language-JavaScript-brightgreen.svg)](https://www.javascript.com/)
[![Framework](https://img.shields.io/badge/Framework-React-blue.svg)](https://reactjs.org/)

## Features

| Feature | Description |
| --- | --- |
| **Confirmation Router** | Handles birthday party confirmation requests |
| **Real-time Updates** | Utilizes WebSockets for real-time data updates. |

## Endpoints

### Confirmation Router

- **POST /confirm**: Endpoint to submit a birthday party confirmation.
    - Request Body: JSON containing `name`, `email`, `phone` and `confirmation_status`.
    - Response: JSON with confirmation details.

- **GET /confirmations**: Endpoint to retrieve all confirmations.
    - Response: JSON array of all confirmation records.

## Real-time Updates

- **WebSocket /ws/updates**: WebSocket endpoint for real-time updates on confirmations.
    - Clients can connect to receive updates whenever a new confirmation is submitted.

## Contribution

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## Prerequisites

* Python 3.x installed on your system
* Uvicorn ASGI server installed (`pip install uvicorn`)
* FastAPI web framework installed (`pip install fastapi`)
* Node.js (version 14 or higher)
* npm (version 6 or higher)
* A code editor or IDE of your choice
* Basic understanding of JavaScript, React, and WebSockets

## Instructions

### Backend

1. Clone the repository to your local machine using `git clone`
2. Navigate to the backend directory: `cd backend`
3. Install dependencies by running `pip install -r requirements.txt`
4. Run the application using `uvicorn main:app --host 127.0.0.1 --port 8000`

### Frontend

1. Navigate to the frontend directory: `cd frontend`
2. Install dependencies by running `npm install`
3. Start the development server using `npm start`
4. Open your browser and navigate to `http://localhost:3000` to view the application

## Contribution

Contributions are welcome! Please fork the repository and submit a pull request with your changes.