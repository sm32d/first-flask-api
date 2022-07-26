# First Flask Api

My first Flask API

## Requirements

- Python 3
- Flask
- pycurl

# Run the server

```bash
python app.py
```

Server would open at 5000 port.

# How to:

### Get all courses

Go to `localhost:5000/courses` in your browser.

### Get all course by ID

Go to `localhost:5000/courses/ID` in your browser.
For example, to get course with ID = 2, go to `localhost:5000/courses/2`

### Add a new course

```bash
curl -i -H "Content-Type: Application/json" -X POST http://localhost:5000/courses
```

### Update a course description to 'XYZ'

```bash
curl -i -H "Content-Type: Application/json" -X PUT http://localhost:5000/courses/5
```

The '5' at the end of the URL is the course ID to be updated.

### Delete a course

```bash
curl -i -H "Content-Type: Application/json" -X DELETE http://localhost:5000/courses/5
```

The '5' at the end of the URL is the course ID to be deleted.
