import pandas as pd

# Load the dataset
file_path = 'loan_payments_transformed_corrected_skew.csv'  # Replace with your actual file path
loan_data = pd.read_csv(file_path)

# Step 1: Identify and count 'Charged Off' loans
charged_off_loans = loan_data[loan_data['loan_status'] == 'Charged Off']

# Step 2: Calculate the total number of loans
total_loans = len(loan_data)

# Step 3: Calculate the percentage of charged off loans
percentage_charged_off = (len(charged_off_loans) / total_loans) * 100

# Step 4: Sum the total amount paid towards these charged off loans before they were charged off
# Replace 'total_paid_column' with the actual column name that represents the total amount paid
total_paid_to_charged_off = charged_off_loans['total_payment'].sum()

# Print the results
print(f"Percentage of Charged Off Loans: {percentage_charged_off:.2f}%")
print(f"Total Amount Paid to Charged Off Loans: ${total_paid_to_charged_off:,.2f}")

