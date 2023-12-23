import pandas as pd

# Load the dataset
file_path = 'loan_payments_transformed_corrected_skew.csv'  # Replace with your actual file path
loan_data = pd.read_csv(file_path)

# Convert date columns to datetime format
loan_data['last_payment_date'] = pd.to_datetime(loan_data['last_payment_date'])
loan_data['issue_date'] = pd.to_datetime(loan_data['issue_date'])

# Analyzing loans that are late on payments and charged off
late_loans = loan_data[loan_data['loan_status'].isin(['Late (16-30 days)', 'Late (31-120 days)'])]
charged_off_loans = loan_data[loan_data['loan_status'] == 'Charged Off']

# Columns of interest
columns_of_interest = ['grade', 'purpose', 'home_ownership']

# Analysis for Charged Off Loans
charged_off_analysis = charged_off_loans[columns_of_interest].apply(lambda x: x.value_counts(normalize=True)).T

# Analysis for Late Loans
late_loans_analysis = late_loans[columns_of_interest].apply(lambda x: x.value_counts(normalize=True)).T

print('Charged Off Loans Analysis:\n', charged_off_analysis)
print('\nLate Loans Analysis:\n', late_loans_analysis)
