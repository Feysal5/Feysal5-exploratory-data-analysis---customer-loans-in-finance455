# Correcting the date handling and recalculating
import pandas as pd
import matplotlib.pyplot as plt
loan_data = pd.read_csv('loan_payments_transformed_corrected_skew.csv')
# Converting date columns to datetime format
loan_data['last_payment_date'] = pd.to_datetime(loan_data['last_payment_date'])
loan_data['issue_date'] = pd.to_datetime(loan_data['issue_date'])

# Filtering out the charged off loans again
charged_off_loans = loan_data[loan_data['loan_status'] == 'Charged Off']

# Extracting term in months from the term column
charged_off_loans['term_months'] = charged_off_loans['term'].str.extract('(\d+)').astype(int)

# Calculating the elapsed time from issue date to the last payment date in months
charged_off_loans['elapsed_time'] = (charged_off_loans['last_payment_date'].dt.year - charged_off_loans['issue_date'].dt.year) * 12 + (charged_off_loans['last_payment_date'].dt.month - charged_off_loans['issue_date'].dt.month)

# Calculating the remaining term for each loan
charged_off_loans['remaining_term'] = charged_off_loans['term_months'] - charged_off_loans['elapsed_time']

# Projected loss (assuming 'out_prncp' represents the outstanding principal)
projected_loss = charged_off_loans['out_prncp'].sum()

# Potential interest revenue on the outstanding principal for the remaining term
charged_off_loans['potential_interest'] = charged_off_loans['out_prncp'] * (charged_off_loans['int_rate'] / 100) * (charged_off_loans['remaining_term'] / 12)
loss_in_revenue = charged_off_loans['potential_interest'].sum()

# Visualizing the loss by remaining term
loss_by_term = charged_off_loans.groupby('remaining_term')['potential_interest'].sum()
loss_by_term = loss_by_term[loss_by_term > 0]  # Exclude terms with no loss

# Plotting
plt.figure(figsize=(10, 6))
plt.bar(loss_by_term.index, loss_by_term.values, color='red')
plt.xlabel('Remaining Term (Months)')
plt.ylabel('Potential Loss in Revenue')
plt.title('Projected Loss in Revenue Over Remaining Term of Charged Off Loans')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

projected_loss, loss_in_revenue
