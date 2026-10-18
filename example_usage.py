from client import PersonalAgentTaxDeductionCategorizer

def main():
    agent = PersonalAgentTaxDeductionCategorizer()
    bills = [
        {"merchant": "AWS Cloud", "amount_usd": 184.50, "description": "Compute clusters for development"},
        {"merchant": "Logitech", "amount_usd": 129.99, "description": "MX Master 3S Ergonomic Mouse"},
        {"merchant": "Bistro Deluxe", "amount_usd": 290.00, "description": "Investor dinner"}
    ]
    res = agent.categorize_deductible_expenses(bills, marginal_tax_bracket_pct=32.0)
    print("--- Personal Tax Deduction Analysis ---")
    print(f"Total Spent: ${res['total_spent_usd']} | Total Deductible: ${res['total_deductible_usd']}")
    print(f"Estimated Tax Savings: ${res['estimated_tax_savings_usd']}")
    for exp in res['categorized_expenses']:
        print(f"* [{exp['schedule_c_category']}] {exp['merchant']}: ${exp['deductible_amount_usd']} (Audit Flag: {exp['audit_flag']})")

if __name__ == "__main__":
    main()
