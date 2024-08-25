# Flask CRUD Application with PostgreSQL using Docker Compose

This project is a basic CRUD (Create, Read, Update, Delete) application built with Flask and connected to a PostgreSQL database. The application is containerized using Docker and Docker Compose, and testing can be done using Postman.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

Before you begin, ensure you have the following installed:

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

## Project Structure

```
├── app/
│   ├── .dockerignore
│   ├── app.py
│   ├── Dockerfile 
│   └── requirements.txt
├── db/
│   ├── Dockerfile
|   └── init.sql  
├── .env
├── docker-compose.yml
└── README.md
```

- `app/`: Contains the Flask application code.
    - `.dockerignore`: Specifies files and directories to ignore when building the Docker image for the Flask app.
    - `app.py`: The main Flask application file.
    - `Dockerfile`: Defines the Docker image for the Flask application.
    - `requirements.txt`: Lists the Python dependencies for the Flask app.
- `db/`: Contains the PostgreSQL database setup.
    - `Dockerfile`: Defines the Docker image for the PostgreSQL database.
    - `init.sql`: SQL script to initialize the database schema.
- `.env`: Stores environment variables.
- `docker-compose.yml`: Docker Compose configuration file.
- `README.md`: Documentation for the project.

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/joharflo/flask-postgres-compose.git
cd flask-postgres-compose
```

### 2. Set Up Environment Variables

Create a `.env` file in the root directory of the project and add the following variables:

```env
# Database Configuration
POSTGRES_USER=your_user
POSTGRES_PASSWORD=your_password
POSTGRES_DB=data_base_name  

# Container Names
SERVER_NAME_DB=server_db_name
SERVER_NAME_APP=serve_app_name
```

### 3. Build and Run the Containers

Use Docker Compose to build and run the application:

```bash
docker-compose up --build
```

This command will start the Flask application and the PostgreSQL database in separate containers.


## Usage

Once the containers are running, you can interact with the API using tools like Postman or cURL. The application will be available at `http://localhost:5000`.

### API Endpoints

- **Create**: `POST /items`
    - Example Request Body:
     ```JSON
     {
       "description": "Enjoy vibrant colors and sharp details",
       "name": "SmartTV"
     }            
- **Read**: `GET /items`

- **Update**: `PUT /items/<id>`
            
- **Delete**: `DELETE /items/<id>`
## Testing

You can use Postman to test the API endpoints.
## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or features.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
