# Challenge one

## Docker
### Running as a container
* Set up your environment variables following the `.env.example` as example
* Run `docker-composer up`
```
   Browser
      ▲
      │
      │
      │
      ▼
┌───────────┐       ┌───────────┐
│ (Backend) │       │(Database) │
│           │       │           │
│  Uvicorn  │◄─────►│ Postgres  │
│           │       │           │
│   80      │       │   5432    │
└───────────┘       └───────────┘
```