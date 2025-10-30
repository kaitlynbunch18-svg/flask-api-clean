# Flask API - Supplier Intelligence

Production Flask API for Bunch of Equipment Online supplier intelligence automation.

## Endpoints

- `GET /` - Service info
- `GET /health` - Health check
- `GET /dbcheck` - Database connection check
- `POST /api/v1/products/upsert` - Upsert product (requires auth)
- `POST /api/v1/workflows/run` - Run workflow (requires auth)
- `POST /api/v1/webhooks/make` - Make.com webhook
- `POST /api/v1/supplier-intel` - Supplier intelligence analysis (requires auth)

## Environment Variables

- `DATABASE_URL` - PostgreSQL connection string
- `SECRET_KEY` - Flask secret key
- `WORKFLOW_AUTH_TOKEN` - API authentication token
- `PORT` - Server port (default: 8080)

## Deployment

Deployed on Railway with auto-deploy from main branch.

## Version

1.0.0 - Production deployment
