# Best Buy Staff Service

A cloud-native microservice for managing Best Buy staff information. This service provides REST APIs for handling CRUD (Create, Read, Update, Delete) operations for staff information, built with FastAPI and containerized for deployment on Azure Kubernetes Service (AKS).

## Features

- RESTful API endpoints for staff management
- In-memory data storage
- Docker containerization
- Kubernetes deployment support
- Built following 12-factor app principles

## Technical Stack

- Python 3.9
- FastAPI framework
- Docker
- Azure Kubernetes Service (AKS)

## Staff Information Schema

```json
{
    "id": "string (auto-generated)",
    "name": "string",
    "position": "string",
    "department": "string",
    "email": "string",
    "phone": "string"
}
```

## API Endpoints

### Create Staff Member
- **POST** `/api/staff`
- Request Body:
```json
{
    "name": "John Doe",
    "position": "Sales Associate",
    "department": "Electronics",
    "email": "john.doe@bestbuy.com",
    "phone": "555-0100"
}
```

### Get Staff Member
- **GET** `/api/staff/{staff_id}`
- Returns staff member details by ID

### Get All Staff Members
- **GET** `/api/staff`
- Returns list of all staff members

### Update Staff Member
- **PUT** `/api/staff/{staff_id}`
- Request Body: Same as Create Staff Member

### Delete Staff Member
- **DELETE** `/api/staff/{staff_id}`
- Removes staff member by ID

## Local Development Setup

1. Clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/bestbuy-staff-service.git
cd bestbuy-staff-service
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the service:
```bash
uvicorn app.main:app --reload --port 8080
```

## Docker Container

Build and run the Docker container:

```bash
# Build container
docker build -t your-dockerhub-username/staff-service:latest .

# Run container
docker run -p 8080:8080 your-dockerhub-username/staff-service:latest
```

## Deployment to AKS

1. Create AKS cluster:
```bash
az aks create --resource-group bestbuy-staff-rg --name bestbuy-staff-aks --node-count 1
```

2. Get credentials:
```bash
az aks get-credentials --resource-group bestbuy-staff-rg --name bestbuy-staff-aks
```

3. Deploy the application:
```bash
kubectl apply -f kubernetes-deployment.yaml
```

## Completed Tasks

1. **Microservice Development**
   - Created FastAPI-based staff service
   - Implemented CRUD operations
   - Set up in-memory data storage
   - Added input validation using Pydantic models

2. **Containerization**
   - Created Dockerfile
   - Built and pushed Docker image
   - Tested container functionality

3. **AKS Deployment**
   - Created deployment YAML
   - Set up AKS cluster
   - Deployed service to Kubernetes

## API Testing

Using curl:

```bash
# Create staff member
curl -X POST http://localhost:8080/api/staff \
  -H "Content-Type: application/json" \
  -d '{"name": "John Doe", "position": "Sales Associate", "department": "Electronics", "email": "john.doe@bestbuy.com", "phone": "555-0100"}'

# Get all staff members
curl http://localhost:8080/api/staff

# Get specific staff member
curl http://localhost:8080/api/staff/{staff_id}

# Update staff member
curl -X PUT http://localhost:8080/api/staff/{staff_id} \
  -H "Content-Type: application/json" \
  -d '{"name": "John Doe", "position": "Senior Sales Associate", "department": "Electronics", "email": "john.doe@bestbuy.com", "phone": "555-0100"}'

# Delete staff member
curl -X DELETE http://localhost:8080/api/staff/{staff_id}
```

#Docker Image link 
[link (https://hub.docker.com/repository/docker/pascalkc9999/staff-service/general)]
