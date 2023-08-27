### Activate Virtual Env

```
python -m venv venv/
source venv/bin/activate
```

### Install dependencies
```
pip install -r requirements.txt
```

### Migration

```
python manage.py migrate
```

### Run
```
python manage.py runserver
```

### To Test

Postman collections are included.

### Demo Requests

#### Create Post

```
POST http://127.0.0.1:8000/api/v1/posts/

{
    "id": "efafb1ae-604e-4455-9d17-2dbe495d9fa3",
    "content": "a test content message"
}
```

##### Curl

```
curl --location 'http://127.0.0.1:8000/api/v1/posts/' \
--header 'Content-Type: application/json' \
--data '{
    "id": "efafb1ae-604e-4455-9d17-2dbe495d9fa3",
    "content": "a test content message"
}'
```

#### Get Analysis

```
GET http://127.0.0.1:8000/api/v1/posts/efafb1ae-604e-4455-9d17-2dbe495d9fa3/analysis
```

##### Curl

```
curl --location 'http://127.0.0.1:8000/api/v1/posts/efafb1ae-604e-4455-9d17-2dbe495d9fa3/analysis'
```


