# API Documentation

Complete API reference for Price Tracker & Alerter.

## Base URL

```
http://localhost:8000/api/v1
```

## Authentication

Currently, no authentication is required. This will be added in future versions.

---

## Products

### List Products

```http
GET /products
```

**Query Parameters:**
- `skip` (int, optional): Number of records to skip (default: 0)
- `limit` (int, optional): Maximum records to return (default: 100)
- `active_only` (bool, optional): Filter active products only (default: false)

**Response:**
```json
[
  {
    "id": 1,
    "url": "https://amazon.com/product",
    "name": "Product Name",
    "current_price": 99.99,
    "currency": "USD",
    "image_url": "https://...",
    "is_active": true,
    "last_checked": "2024-01-15T10:30:00",
    "created_at": "2024-01-01T00:00:00",
    "updated_at": "2024-01-15T10:30:00"
  }
]
```

### Get Product

```http
GET /products/{id}
```

**Path Parameters:**
- `id` (int, required): Product ID

**Query Parameters:**
- `days` (int, optional): Number of days of price history (default: 30)

**Response:**
```json
{
  "id": 1,
  "url": "https://amazon.com/product",
  "name": "Product Name",
  "current_price": 99.99,
  "currency": "USD",
  "image_url": "https://...",
  "is_active": true,
  "last_checked": "2024-01-15T10:30:00",
  "created_at": "2024-01-01T00:00:00",
  "updated_at": "2024-01-15T10:30:00",
  "price_history": [
    {
      "price": 99.99,
      "timestamp": "2024-01-15T10:30:00"
    }
  ]
}
```

### Create Product

```http
POST /products
```

**Request Body:**
```json
{
  "url": "https://amazon.com/product",
  "name": "Product Name",
  "currency": "USD"
}
```

**Response:** `201 Created`
```json
{
  "id": 1,
  "url": "https://amazon.com/product",
  "name": "Product Name",
  "current_price": null,
  "currency": "USD",
  "image_url": null,
  "is_active": true,
  "last_checked": null,
  "created_at": "2024-01-15T10:30:00",
  "updated_at": "2024-01-15T10:30:00"
}
```

### Update Product

```http
PATCH /products/{id}
```

**Path Parameters:**
- `id` (int, required): Product ID

**Request Body:**
```json
{
  "name": "Updated Name",
  "is_active": false
}
```

**Response:**
```json
{
  "id": 1,
  "url": "https://amazon.com/product",
  "name": "Updated Name",
  "current_price": 99.99,
  "currency": "USD",
  "image_url": "https://...",
  "is_active": false,
  "last_checked": "2024-01-15T10:30:00",
  "created_at": "2024-01-01T00:00:00",
  "updated_at": "2024-01-15T10:35:00"
}
```

### Delete Product

```http
DELETE /products/{id}
```

**Path Parameters:**
- `id` (int, required): Product ID

**Response:**
```json
{
  "success": true,
  "message": "Product deleted successfully"
}
```

### Check Product Price

```http
POST /products/{id}/check
```

**Path Parameters:**
- `id` (int, required): Product ID

**Response:**
```json
{
  "id": 1,
  "url": "https://amazon.com/product",
  "name": "Product Name",
  "current_price": 89.99,
  "currency": "USD",
  "image_url": "https://...",
  "is_active": true,
  "last_checked": "2024-01-15T10:40:00",
  "created_at": "2024-01-01T00:00:00",
  "updated_at": "2024-01-15T10:40:00"
}
```

---

## Alerts

### List Alerts

```http
GET /alerts
```

**Query Parameters:**
- `product_id` (int, optional): Filter by product ID
- `active_only` (bool, optional): Filter active alerts only (default: true)

**Response:**
```json
[
  {
    "id": 1,
    "product_id": 1,
    "alert_type": "percentage",
    "target_price": null,
    "percentage_drop": 10.0,
    "is_active": true,
    "created_at": "2024-01-01T00:00:00"
  }
]
```

### Create Alert

```http
POST /alerts
```

**Request Body (Absolute Price):**
```json
{
  "product_id": 1,
  "alert_type": "absolute",
  "target_price": 79.99
}
```

**Request Body (Percentage Drop):**
```json
{
  "product_id": 1,
  "alert_type": "percentage",
  "percentage_drop": 10.0
}
```

**Request Body (Any Drop):**
```json
{
  "product_id": 1,
  "alert_type": "any_drop"
}
```

**Response:** `201 Created`
```json
{
  "id": 1,
  "product_id": 1,
  "alert_type": "percentage",
  "target_price": null,
  "percentage_drop": 10.0,
  "is_active": true,
  "created_at": "2024-01-15T10:30:00"
}
```

### Delete Alert

```http
DELETE /alerts/{id}
```

**Path Parameters:**
- `id` (int, required): Alert ID

**Response:**
```json
{
  "success": true,
  "message": "Alert deleted successfully"
}
```

---

## Notifications

### List Notifications

```http
GET /notifications
```

**Query Parameters:**
- `skip` (int, optional): Number of records to skip (default: 0)
- `limit` (int, optional): Maximum records to return (default: 100)

**Response:**
```json
[
  {
    "id": 1,
    "alert_id": 1,
    "channel": "email",
    "message": "Price dropped to $89.99",
    "sent_at": "2024-01-15T10:30:00",
    "success": true,
    "error_message": null
  }
]
```

---

## Jobs

### Trigger Check All

```http
POST /jobs/check-all
```

**Response:**
```json
{
  "success": true,
  "message": "Price check triggered for all products"
}
```

### Get Scheduler Status

```http
GET /jobs/status
```

**Response:**
```json
{
  "running": true,
  "interval_minutes": 60
}
```

---

## Health

### Health Check

```http
GET /health
```

**Response:**
```json
{
  "status": "healthy",
  "service": "price-tracker"
}
```

---

## Error Responses

All endpoints may return the following error responses:

### 400 Bad Request
```json
{
  "detail": "Invalid URL"
}
```

### 404 Not Found
```json
{
  "detail": "Product not found"
}
```

### 422 Validation Error
```json
{
  "detail": [
    {
      "loc": ["body", "url"],
      "msg": "field required",
      "type": "value_error.missing"
    }
  ]
}
```

### 500 Internal Server Error
```json
{
  "detail": "Internal server error"
}
```

---

## Interactive Documentation

For interactive API documentation with try-it-out functionality, visit:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

---

## Rate Limiting

Currently, no rate limiting is implemented. This will be added in future versions.

---

## Webhooks (Coming Soon)

Future versions will support webhooks for custom integrations.
