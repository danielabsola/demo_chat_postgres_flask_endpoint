# demo_chat_postgres_flask_endpoint

# Chat History Project

This project is designed to store and manage chat history using a PostgreSQL database and a Flask API. The API provides endpoints for storing and retrieving chat history based on session IDs.

## Getting Started

These instructions will help you set up the project on your local machine for development and testing purposes.

### Prerequisites

- Python 3.6+
- PostgreSQL
- A PostgreSQL client (e.g., pgAdmin or DBeaver)
- Virtualenv (optional, but recommended)

### Installation

1. Clone the repository:

git clone https://github.com/danielabsola/demo_chat_postgres_flask_endpoint.git


2. (Optional) Create a virtual environment and activate it:

virtualenv venv
source venv/bin/activate


3. Install the required Python packages:


4. Set up the PostgreSQL database:

- Create a new PostgreSQL database and user.
- Update the `.env` file with your database credentials.
- Import the demo table from the `demo_table.sql` file.

5. Run the Flask application:


4. Set up the PostgreSQL database:

- Create a new PostgreSQL database and user.
- Update the `.env` file with your database credentials.
- Import the table from the `chat_history_companion.sql` file.

5. Run the Flask application:

app.py


The API should now be running at `http://127.0.0.1:5000/api`.

## API Endpoints

- `GET /api/companion/`: Retrieve all chat history records.
- `POST /api/companion/add`: Add a new chat history record.
- `GET /api/companion/<session_id>`: Retrieve chat history records for a specific session ID.


