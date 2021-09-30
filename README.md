# Movie Theatre

- Rooms with a designated capacity (number of seats)
- Movies that are playing at a set time every day
- Tickets that are sold to customers


### Features

The API should be able to do the following

- Set up rooms
- Set up movie showtimes
- Sell some tickets
- Look at the list of movie rooms and what they're playing
- Look at the list of movies playing at the theater
- Buy tickets to a movie

### Running API

1. Virtual environment with install django and djangorestframework should be activated
2. Run : python manage.py runserver
3.  API can be access on localhost:8000/rooms


### Routes

API uses Interface from rest framework to test api and api can be interfaced using json format by adding ?format=json in urls

#### Set Up Room

POST Request to [http://localhost:8000/rooms](http://localhost:8000/rooms) as example :

```json
{
  "name" : "<room name, string>",
  "seating_capacity" : "<seats, integer>"
}
```

- As validation no two rooms can have same name


#### Creating Movie

POST Request to [http://localhost:8000/movies](http://localhost:8000/movies) as example :

```json
{
  "title" : "<Movie name, string>",
  "duration_in_minutes" : "<duration, integer>"
}
```

- As validation no two movies can have same name


#### Setting Up Show

POST Request to [http://localhost:8000/shows](http://localhost:8000/shows) as example :


```json
{
  "room": "<room, id>",
  "movie": "<movie, id>",
  "startTime": "<datetime>",
  "price": "<price, decimal/integer>"
}
```


```json

  {
   "room": 2,
   "movie": 3,
   "startTime": "2021-11-30T07:02:00Z",
   "price": 90
}

```

- As validation no two shows clashes each other time



#### Buying a Ticket

POST Request to [http://localhost:8000/tickets](http://localhost:8000/tickets) as example :


```json

 {
    "customer_name": "<string>",
    "show": "<show id>",
    "seats": "<integer>"
}

```


```json

 {
    
    "customer_name": "Neeraj",
    "show": 41,
    "seats": 20,
    
}
```
```json
{
    "id": 22,
    "customer_name": "Neeraj",
    "show": 41,
    "seats": 20,
    "amount": "1980.00"
}
```

- As validation number of requested seats cannot be greater than available seats


#### Get All the Movies Playing in Theatre

GET Request to [http://localhost:8000/movies](http://localhost:8000/movies) as example response will be :

```json
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "count": 4,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 3,
            "title": "Batman",
            "duration_in_mintues": 60
        },
        {
            "id": 4,
            "title": "Document",
            "duration_in_mintues": 30
        },
        {
            "id": 5,
            "title": "Longest",
            "duration_in_mintues": 100
        },
        {
            "id": 6,
            "title": "liaght",
            "duration_in_mintues": 150
        }
    ]
}
```

- As validation no two rooms can have same name

