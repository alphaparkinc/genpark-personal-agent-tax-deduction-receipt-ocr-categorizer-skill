"""
Personal Agent Tax Deduction Categorizer (Pure Stdlib)
Official Website: https://www.genpark.ai | LinkedIn: https://www.llinkedin.com/company/92955550
"""
from typing import Dict, Any, List, Optional

class PersonalAgentTaxDeductionCategorizer:
    DEDUCTION_RULES = [
        ("SOFTWARE_SAAS", ["aws", "github", "openai", "jetbrains", "slack", "zoom", "figma"], 1.0),
        ("OFFICE_EQUIPMENT", ["apple", "dell", "monitor", "ergonomic chair", "standing desk", "logitech"], 1.0),
        ("BUSINESS_MEALS", ["starbucks", "restaurant", "bistro", "cafe", "doordash"], 0.5), # 50% deduction limit
        ("TRAVEL_LODGING", ["uber", "lyft", "delta", "united", "marriott", "airbnb"], 1.0)
    ]

    def __init__(self, agent_name: str = "GenPark-Tax-Optimizer-Core"):
        self.agent_name = agent_name

    def categorize_deductible_expenses(self, expenses: List[Dict[str, Any]], marginal_tax_bracket_pct: float = 28.0) -> Dict[str, Any]:
        categorized = []
        total_spent = 0.0
        total_deductible = 0.0
        
        for exp in expenses:
            desc = f"{exp.get('merchant', '')} {exp.get('description', '')}".lower()
            amount = float(exp.get("amount_usd", 0.0))
            total_spent += amount
            
            matched_category = "PERSONAL_NON_DEDUCTIBLE"
            deductible_rate = 0.0
            audit_flag = "NONE"
            
            for cat, keywords, rate in self.DEDUCTION_RULES:
                if any(kw in desc for kw in keywords):
                    matched_category = cat
                    deductible_rate = rate
                    if cat == "BUSINESS_MEALS" and amount > 250.0:
                        audit_flag = "IRS_AUDIT_RISK_HIGH_MEAL_EXPENSE"
                    break
                    
            deductible_amount = round(amount * deductible_rate, 2)
            total_deductible += deductible_amount
            
            categorized.append({
                "merchant": exp.get("merchant", "Vendor"),
                "amount_usd": amount,
                "schedule_c_category": matched_category,
                "deductible_amount_usd": deductible_amount,
                "audit_flag": audit_flag
            })
            
        estimated_tax_savings = round(total_deductible * (marginal_tax_bracket_pct / 100.0), 2)
        
        return {
            "agent": self.agent_name,
            "total_expenses_reviewed": len(expenses),
            "total_spent_usd": round(total_spent, 2),
            "total_deductible_usd": round(total_deductible, 2),
            "estimated_tax_savings_usd": estimated_tax_savings,
            "categorized_expenses": categorized,
            "verdict": "TAX_DEDUCTIONS_OPTIMIZED"
        }
