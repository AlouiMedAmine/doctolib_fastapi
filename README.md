Step 1: Install Python
Verify that Python 3.7+ is installed by running:

python3 --version


Step 2: Install pip
Verify that pip is installed by running:

python3 -m pip --version


Step 3: Set Up a Virtual Environment
1.Create a new directory for your project (optional but recommended):

mkdir fastapi-project
cd fastapi-project


2.Create a virtual environment:

python3 -m venv env



3.Activate the virtual environment:

source env/bin/activate


#Desactivate the virtual env

deactivate



4.Install FastAPI and Uvicorn

pip3 install fastapi uvicorn


5.Verify Installation
pip show fastapi uvicorn


6.Run the application

uvicorn main:app --reload
