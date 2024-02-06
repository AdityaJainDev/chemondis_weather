# Instructions

### Before starting
Note: Please edit the config.env file to add the required parameters described. Once added, please change file name to `.env`.

### Run via Docker
1. To run the app, please use `docker compose up` command.
2. To view all endpoints for the application, you can visit `localhost:8000/api/docs`.

### Homepage
1. The main homepage is at `localhost:8000`. Here you will see two fields, `Language` and `City Name`.
2. Please select the language in which you would like the API data and the City you want the weather for.
3. If entered correctly, a small card should show the details.
4. Queries are cached based on the time defined for `CACHE_TTL` in `.env` file. 

### Swagger
1. API spec should be available to see on `localhost:8000/api/docs`. 
2. Only a single endpoint `GET` is defined to fetch weather details, required two parameters, `City Name`  and a two letter `Language Code` (Eg: 'en' for English).