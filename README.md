# Yandex Search Application

This Python application utilizes the Yandex Maps API to perform searches based on various parameters. 
The application provides three search endpoints:

1. **Search by Name:** `/search_by_name`
2. **Search by Services:** `/search_by_services`
3. **Search by Address:** `/search_by_address`

## Prerequisites

Make sure you have the following installed:

- Python (version 3.x)
- Requests library (`pip install requests`)

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/afafos/yandex_search_application.git
   ```
2. Change into the project directory:
   ```
   cd your-repo
   ```

## Configuration

Before running the application, you need to obtain a Yandex Maps API key. 
You can get one by following the instructions on the Yandex Maps API documentation
https://yandex.com/dev/maps/jsapi/doc/2.1/quick-start/index.html

Once you have the API key, create a file named `api.py` in the project directory and define your key like this:

```
# api.py
yandex_api = "your-yandex-maps-api-key"
```

## Usage

Run the application using the following command:

```
python your-app-name.py
```

The application will start serving on port 8000.

## Endpoints

### 1. Search by Name

   - **Endpoint:** `/search_by_name`

   - **Parameters:**
     - `name`: The name of the business or location you want to search for.

   - **Example:**
     ```
     curl http://localhost:8000/search_by_name?name=your-business-name
     ```

### 2. Search by Services

   - **Endpoint:** `/search_by_services`

   - **Parameters:**
     - `services`: The services offered by the business or location you want to search for.

   - **Example:**
     ```
     curl http://localhost:8000/search_by_services?services=your-service
     ```

### 3. Search by Address

   - **Endpoint:** `/search_by_address`

   - **Parameters:**
     - `organization`: The name of the organization.
     - `city`: The city where the organization is located.
     - `street`: The street where the organization is located.

   - **Example:**
     ```
     curl http://localhost:8000/search_by_address?organization=your-organization&city=your-city&street=your-street
     ```

## Result

The search results will be saved in a file named `result.json` in the project directory.

## Workspace

For more details about the application, check out the workspace
https://web.postman.co/workspace/yandex_search_app~5d85f047-a7be-48cd-86fe-6c1766f6716c/overview

















