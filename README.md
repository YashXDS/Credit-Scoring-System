# Credit Score Classification App

This project is a machine learning-based credit score classification app. The app allows users to input their financial and credit data to predict whether their credit score is above or below 650. The classification is binary, where:
- **0** indicates a credit score **above 650** (creditworthy).
- **1** indicates a credit score **below 650** (not creditworthy).

## Features

- **User-friendly interface** built with Streamlit for collecting credit and financial data.
- Predicts whether a user is eligible for a loan based on their credit score using a pre-trained **Random Forest model**.
- Utilizes **joblib** for loading the machine learning model and scaler.
- Provides real-time prediction results based on the input data.

## App Demo

![App Demo](link_to_your_app_image_or_gif)

## Project Structure
``` bash
├── app.py                   # Streamlit app code
├── best_model_random_forest.pkl  # Pre-trained model
├── scaler.pkl               # Pre-trained scaler
├── model_1.ipynb            # Jupyter Notebook for training and evaluating the model
├── README.md                # Project documentation
└── requirements.txt         # Python dependencies
```
## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your_username/Credit-Scoring-System.git
   ```
2. Navigate to the project directory:

```bash
cd your_repository_name
```
3. Install the required Python packages:

```bash

pip install -r requirements.txt
```
4. Run the Streamlit app:

```bash

streamlit run app.py
```
## Usage
1. Open the app in your browser (Streamlit will display the URL after running the command).
2. Input your financial and credit details:.
-**Age**: Enter your age (between 18 and 100).
-**Annual Income**: Your yearly income in USD.
-**Years of Employment**: The number of years you have been employed.
-**Grade**: Credit grade (e.g., 0 for B, 1 for A).
-**Loan Amount**: Desired loan amount.
-**Interest Rate**: Loan interest rate as a percentage.
-**Percent of Income**: What percentage of your income is represented by the loan amount.
-**Credit History**: Number of years of credit history.
-**Home Ownership**: Home ownership status (e.g., OWN, RENT, OTHER).
-**Loan Purpose**: Reason for taking the loan (e.g., EDUCATION, PERSONAL, MEDICAL).
-**Default History**: Have you ever defaulted on a loan (Y/N)?
   
**Click the Predict button.**
The app will display whether your credit score is above or below 650.

## Model Details
The model used in this app is a Random Forest Classifier, trained on a dataset containing various financial and credit-related features. The target variable is whether a user's credit score is above or below 650.

### Input Features:
Age, Income, Employment Years, Loan Amount, Interest Rate, Percent of Income, Credit History, Home Ownership Status, Loan Purpose, Default History, Age-Income Ratio, Loan-Income Ratio.
### Target:
```bash
0 (Credit score ≥ 650) or 1 (Credit score < 650).
```
## Model Training
To understand the model training process, check out the model_1.ipynb file, where the data is preprocessed, features are selected, and the Random Forest model is trained.

## Deployment
The app is built using Streamlit, which makes it easy to deploy. Simply run the streamlit run app.py command, and the app will be accessible on your local machine.

## Dependencies
```bash
Python 3.8+
Streamlit
Scikit-learn
Joblib
NumPy
```
All dependencies are listed in the requirements.txt file. You can install them using:

```bash
pip install -r requirements.txt
```

## Contact
If you have any questions or feedback, feel free to reach out:

Email: yapatel9023@gmail.com

## Key Sections Explained:

- **Project Overview**: A description of the app and what it does.
- **Installation**: Instructions to set up the project locally.
- **Usage**: Explains how to use the app and what input fields to provide.
- **Model Details**: Information about the machine learning model and features used.
- **Deployment**: Simple instructions on running the app.
- **Contact**: Information for reaching out if users have questions.






You said:
create this again ├── app.py # Streamlit app code ├── best_model_random_forest.pkl # Pre-trained model ├── scaler.pkl # Pre-trained scaler ├── model_1.ipynb # Jupyter Notebook for training and evaluating the model ├── README.md # Project documentation └── requirements.txt # Python dependencies
ChatGPT said:
ChatGPT
Here is the formatted project structure for your README.md:

bash
Copy code
├── app.py                   # Streamlit app code
├── best_model_random_forest.pkl  # Pre-trained model
├── scaler.pkl               # Pre-trained scaler
├── model_1.ipynb            # Jupyter Notebook for training and evaluating the model
├── README.md                # Project documentation
└── requirements.txt         # Python dependencies
You can paste this directly into your README.md under the "Project Structure" section!







