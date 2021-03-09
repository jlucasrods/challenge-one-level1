# Challenge one

## Requirements
* Python 3.6+
* Postgres 13+

## Running
* Install dependencies running `pip install -r requirements.txt`
* Set up your environment variables following the `.env.example` as example
* Run `uvicorn app.main:app --host 0.0.0.0 --port 8000`

## Testing 
* Set up your environment variables with a database for testing
* Run `python -m unittest discover -v .`

## Docker
### Running as a container
* Set up your environment variables following the `.env.example` as example
* Run `docker-composer up`


### Testing with a container
* Run `docker-compose -f ./docker-compose.test.yml up --abort-on-container-exit`
