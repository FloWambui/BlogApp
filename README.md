# BlogApp

#### Created by Florence Wambui.

### Description
A web application that allows users to create and share their blogs, have comments on the blog and delete a comment/blog post.

### Setup Requirements
- Python3
- Pip
- PostgreSQL
- Virtualenv

### Technologies Used
Technologies used to develop this application:

* Python
* Flask 
* Flask-Bootstrap
* HTML
* CSS

### Setup Installation
- Copy the github repository url and clone
- ```git clone https://github.com/FloWambui/BlogApp.git```

- ```cd BlogApp```

- ```python3 -m venv --without pip virtual```

##### Activate the virtual environment
- ```source virtual/bin/activate```
- ```pip install flask```
- ```chmod a+x start.sh```
- ```./start.sh```
- ```python3 manage.py server```

- Open the browser and nagigate http://127.0.0.1:5000/

### Behavior Driven Development (BDD)
A new user:

- Will be able to view quotes consumed from http://quotes.stormconsultancy.co.uk/popular.json API.
- Will be able to view posted blogs.
- Will not be able to create add a blog until the user registers and logs in.
- Will not be able to either comment or view comments until the user registers and logs in.

A Current User:

- Will login with same credentials used to register.
- In instance of wrong credentials will be alerted.
- Will be able to create a blog.
- Will be able to views other peoples blogs.
- Will be able to comment on other peoples blogs.



### Support and contact details
Should you be unable to access the website, have any recommendations and/or questions, feel free to email gflorencewambui@gmail.com

## License
Copyright (c) 2022 Florence Wambui