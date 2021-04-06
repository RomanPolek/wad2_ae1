# Exam Network [![Website shields.io](https://img.shields.io/website-up-down-green-red/http/shields.io.svg)](https://examnetwork.pythonanywhere.com/) 

- [Getting Started](#getting-started)
- [Deploying the Website](#deploying-the-website)
- [Hosting and accessing the Website](#hosting-and-accessing-the-website)

[http://examnetwork.pythonanywhere.com](http://examnetwork.pythonanywhere.com)  

Django based website that facilitates student and teachers to make, conduct and review exams. Teachers will be able to create courses, add students to the courses and make an autograding exam. Teachers can set the deadline and date available in which the students will be able to take exams. Teachers can also view the performance for a course or an exam. Students can take the exams and review it later.

## Getting Started

To setup the project in local machine:

- Open a terminal

- Clone the repository using this command:

  ````bash
  git clone https://github.com/RomanPolek/wad2_ae1.git
  ````

- Change directory to the `wad2_ae1` folder.

- Install the dependencies using the command:

  ```bash
  python -m pip install -r requirements.txt
  ```

Run the script `apply_db_changes.bat` to migrate the database.

- Run the script `create_super_user.bat` to create a superuser.

- To populate the database with mock data, run the command:

  ```bash
  python populate_exam_network.py
  ```

## Deploying the Website

To deploy the project in local machine, run this command:

```bash
python manage.py runserver
```

By default, the website will be deployed in IP address 127.0.0.1 and port 8000. An IP address and a port number can be supplied to deploy in a different IP address and port number. 

To access the website with default settings, open browser and go to [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Hosting and accessing the Website

The website is currently being hosted using Python Anywhere platform.

The website can be accessed from this link:

### 				[Exam Network Website](http://examnetwork.pythonanywhere.com)