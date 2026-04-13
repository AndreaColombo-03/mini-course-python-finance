import pandas as pd
import numpy as np

def generate_portfolio(num_loans=1000):
    np.random.seed(42)
    data = {
        'Loan_ID': range(1, num_loans + 1),
        'Outstanding_Balance': np.random.uniform(50000, 300000, num_loans),
        'Current_Rate': np.random.uniform(0.03, 0.06, num_loans),
        'Remaining_Months': np.random.randint(12, 360, num_loans)
    }
    return pd.DataFrame(data)

def analyze_prepayment(df, new_market_rate, threshold=0.01):
    df['Rate_Diff'] = df['Current_Rate'] - new_market_rate
    
    # Flags the loan if the rate difference is greater than the threshold (1%)
    df['Will_Prepay'] = np.where(df['Rate_Diff'] > threshold, True, False)
    
    # Calculates the financial loss for the bank
    df['Estimated_Loss'] = np.where(
        df['Will_Prepay'],
        df['Outstanding_Balance'] * df['Rate_Diff'] * (df['Remaining_Months'] / 12),
        0
    )
    return df

# Execution 
NEW_MARKET_RATE = 0.025

portfolio_df = generate_portfolio()
risk_df = analyze_prepayment(portfolio_df, NEW_MARKET_RATE)

# Results 
total_loans = len(risk_df)
prepaying_loans = risk_df['Will_Prepay'].sum()
total_loss = risk_df['Estimated_Loss'].sum()

print("--- ALM Prepayment Risk Report ---")
print(f"Total Loans: {total_loans}")
print(f"Prepaying Loans: {prepaying_loans}")
print(f"Estimated Portfolio Loss: € {total_loss:,.2f}")
