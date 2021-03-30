export $(grep -v '^#' .env | xargs)

pytest .
