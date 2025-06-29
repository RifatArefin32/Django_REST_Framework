# Request and Response in Django
- Request and Response are two core components used to handle and return **API data** in a consistent and structured way. 
- They build on Django’s own `HttpRequest` and `HttpResponse` classes but add functionality specifically for building RESTful APIs.

# Request Object (rest_framework.request.Request)
DRF provides its own Request class, which is a wrapper around Django's HttpRequest. 

## Key Features
- Parses incoming data based on `Content-Type` header (e.g., JSON, form data, multipart).
- Provides `.data` attribute to access parsed data
- Supports authentication and permission hooks.

```py
from rest_framework.decorators import api_view

@api_view(['POST'])
def example_view(request):
    name = request.data.get('name')
    return Response({"message": f"Hello, {name}!"})
```

## Attributes
- `request.data` - Parsed request data for POST, PUT, PATCH methods
- `request.query_params` - Access to GET parameters (?page=1)
- `request.user` - The authenticated user (if any)
- `request.auth` - Authentication token or credentials

# Response Object (rest_framework.response.Response)
DRF provides a custom Response class to return data in a consistent, JSON-rendered format.
## Key Features
- Automatically renders `Python data` into `JSON` (or other formats based on the client’s request).
- Handles HTTP content negotiation.
- Supports custom status codes and headers.

```py
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def example_view(request):
    data = {"message": "This is a response"}
    return Response(data, status=status.HTTP_200_OK)
```
## Parameters
- `data` - A Python dict/list to serialize (typically JSON)
- `status` - HTTP status code (e.g., 200, 404, 400)
- `headers` - Custom headers (optional)
- `content_type` - Override content type (e.g., application/xml)