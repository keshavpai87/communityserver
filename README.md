Steps to get started :
Create an empty folder and open it using vs code

**To create a virtual environment,**
In the terminal,

1. **python -m venv myenv** - This will create a virtual environment specific to that particular project
myenv refers to the virtual environment name

2. Activating the same(Copy the relative path)
**myenv\Scripts\Activate.ps1**
To know if its activated, we need to check if the name of the environment is displayed
Here in our case, (myenv) must be displayed

3. To install fastapi and uvicorn,
**pip install fastapi uvicorn**

4. To run uvicorn,
**uvicorn main:app --host 0.0.0.0 --port 8000** - This opens the TCP 8000 port to access from outside
uvicorn main:app --reload

5. SQLAlchemy
To install, we need to execute the following command in the terminal
**pip install sqlalchemy psycopg2**

**pip list** - displays all the packages installed in the machine

6. To deactivate the virtual environment, 
**deactivate** - This will deactivate the virtual environment

7. Loading the FastAPI in the browser
**http://localhost:8000/docs#/**
