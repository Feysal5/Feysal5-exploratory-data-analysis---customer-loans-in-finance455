# Exploratory Data Analysis - Online Shopping in Retail

## Introduction
![image](https://github.com/Feysal5/Feysal5-exploratory-data-analysis---customer-loans-in-finance455/assets/87627171/17f8710f-663e-408e-80c6-9a8a4dec8ba6)
This repository contains datasets and Python scripts pertaining to customer activity and related analytics. The datasets provide insights into customer behaviors, while the Python scripts offer utility functions, software logic, and analysis tools to further process and analyze the datasets.

### Table of Contents
- [Project Description](#project-description)
- [Installation Instructions](#installation-instructions)
- [Usage Instructions](#usage-instructions)
- [File Structure](#file-structure)
- [License Information](#license-information)

### Project Description
This project involves performing exploratory data analysis on a financial institution's loan portfolio to identify key patterns and anomalies. This analysis will aid in making informed decisions about loan approvals, risk management, and pricing. The ultimate goal is to enhance the performance and profitability of the loan portfolio.

### Installation Instructions
1. Clone the repository from GitHub.
- `git clone https://github.com/github8585/exploratory-data-analysis---online-shopping-in-retail.git`
3. Ensure you have Python installed on your system.
- `https://realpython.com/installing-python/`
4. Install the required packages.
- `psycopg2`
- `sqlalchemy`
- `pandas`
- `yaml`
- `matplotlib`
- `seaborn`
- `scipy`
- `numpy`
5. Run the main application using:
- `python db_utils.py`.

### Usage Instructions
Navigate to the main dashboard to access the different modules. Each module has its own interface with relevant options for data input, analysis, and visualization.

### File Structure
- `calculateloss.py`: Analyzes 'Charged Off' loans in a loan portfolio, calculating their percentage and the total amount paid towards them.
- `indicateandpossibleloss.py`: Examines 'Charged Off' and late loans, focusing on their characteristics like grade, purpose, and home ownership.
- `projectedloss.py`: Quantifies the financial impact of 'Charged Off' loans, calculating projected loss in principal and potential interest revenue.
- `stateofloans.py`: Assesses the overall financial state of the loan portfolio, including recovery rates and future recovery predictions.

### License Information
This project is licensed under the MIT License. You can use, modify, and distribute this code freely. For more details, refer to the LICENSE file in the repository.
