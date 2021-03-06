from flask import Flask, jsonify

app = Flask(__name__)

courses = [
    {
        "Description": "Python programming certification helps you learnpython in the structured learning path with innovative out of the box projects matching the industry standards",
        "course_id": "0",
        "name": "Python Programming Certification",
        "price": "visit Edureka.co to know more",
    },
    {
        "Description": "Data science with python helps you master the data science life cycle processes in a structured a learning path",
        "course id": "1",
        "name": "Data Science With Python Certification",
        "price": "visit edureka.co to know more",
    },
    {
        "Description": "AI and ML certification will help you master AI/ML with top notch projects like speechrecognition, chatbots, etc. ",
        "course id": "2",
        "name": "AI and Machine Learning Certification",
        "price": "visit edureka.co to know more",
    },
    {
        "Description": "ySpark Certification Training is designed to provide you the knowledge and skillsthat are required to become successful Spark Developer using Python and prepareyou for the Cloudera Hadoop and Spark Developer Certification Exan",
        "course_id": "3",
        "name": "Python Spark Certification",
        "price": "visit edureka.co to know more",
    },
    {
        "Description": "Natural Language Processing with Python course will take you through the essentialsof text processing all the way up to classifying texts using Machine Learning algorithms.",
        "course_id": "4",
        "name": "Natural Language Processing With Python Certification",
        "price": "visit edureka.co to know more",
    },
]


@app.route("/")
def index():
    return "Hello, World!"


# get all courses
@app.route("/courses", methods=["GET"])
def get():
    return jsonify({"courses": courses})


# get course using ID
@app.route("/courses/<int:course_id>", methods=["GET"])
def get_course(course_id):
    return jsonify({"course": courses[course_id]})


# add a new course
@app.route("/courses", methods=["POST"])
def create():
    course = {
        "Description": "Natural Language Processing with Python course will take you through the essentialsof text processing all the way up to classifying texts using Machine Learning algorithms.",
        "course_id": "5",
        "name": "Natural Language Processing With Python Certification",
        "price": "visit edureka.co to know more",
    }
    courses.append(course)
    return jsonify({"Created": course})


# update a course
@app.route("/courses/<int:course_id>", methods=["PUT"])
def course_update(course_id):
    courses[course_id]["Description"] = "XYZ"
    return jsonify({"course": courses[course_id]})


# delete a course
@app.route("/courses/<int:course_id>", methods=["DELETE"])
def delete(course_id):
    courses.remove(courses[course_id])
    return jsonify({"result": "success"})


if __name__ == "__main__":
    app.run(debug=True)
