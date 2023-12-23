import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = 'loan_payments_transformed_corrected_skew.csv'  # Replace with your actual file path
loan_data = pd.read_csv(file_path)

# Step 1: Calculating the total funded amount and total amount invested
total_funded = loan_data['funded_amount'].sum()
total_invested = loan_data['funded_amount_inv'].sum()

# Step 2: Calculating the total recoveries
total_recoveries = loan_data['recoveries'].sum()

# Step 3: Calculating percentages
percentage_recovered_funded = (total_recoveries / total_funded) * 100
percentage_recovered_invested = (total_recoveries / total_invested) * 100

# Step 4: Visualizing these percentages
fig, ax = plt.subplots()
categories = ['Total Funded', 'Total Invested']
percentages = [percentage_recovered_funded, percentage_recovered_invested]
ax.bar(categories, percentages, color=['blue', 'green'])
ax.set_ylabel('Percentage of Recovery')
ax.set_title('Percentage of Loans Recovered')
ax.set_ylim(0, max(percentages) + 5)  # Setting y-limit for better visualization

# Step 5: For future recovery prediction
# This is a simplistic approach and may not reflect actual future recoveries
months_to_predict = 6
current_month_recovery = total_recoveries / loan_data['last_payment_date'].nunique()
future_recovery = current_month_recovery * months_to_predict
future_recovery_percentage = (future_recovery / total_funded) * 100

# Adding future prediction to the graph
categories.append('Future 6 Months')
percentages.append(future_recovery_percentage)
ax.bar(categories, percentages, color=['blue', 'green', 'red'])

# Displaying the graph
plt.xticks(rotation=45)
plt.show()
