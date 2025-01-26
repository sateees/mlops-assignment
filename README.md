# mlops-assignment

This project is developed as part of MLOps assignment1


## Get Started
To get started with the project, follow the steps below:

#### 1. Clone the Repository
Clone the project repository from GitHub:
```bash
git clone https://github.com/sateees/mlops-assignment.git
```
```bash
cd mlops-assignment
```
#### 2. Set Up the Environment
Ensure you have Python 3.8+ installed. Create a virtual environment and install the necessary dependencies:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

#### 3. Train the Model
To train the model, run the following command:

```bash
python main.py 
```

This script will load the data, preprocess it, train the model, and save the trained model to the models/ directory.

#### 4. FastAPI
Start the FastAPI application by running:

```bash
uvicorn app:app --reload
```

#### 5. Docker
To build the Docker image and run the container:

```bash
docker build -t mlops_api .
```
```bash
docker run -p 80:80 mlops_api
```
