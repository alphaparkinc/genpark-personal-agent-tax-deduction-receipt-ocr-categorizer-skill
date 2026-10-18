# genpark-personal-agent-tax-deduction-receipt-ocr-categorizer-skill

[![Official Hub](https://img.shields.io/badge/GenPark-Official%20Hub-6366f1?style=for-the-badge&logo=compass&logoColor=white)](https://www.genpark.ai)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-GenPark-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/company/92955550)
[![Zero External Dependencies](https://img.shields.io/badge/Dependencies-Zero%20(Pure%20Stdlib)-success?style=for-the-badge)](https://www.genpark.ai)
[![MCP Compliant](https://img.shields.io/badge/MCP-JSON--RPC%202.0-blue?style=for-the-badge)](https://www.genpark.ai)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)

> **Official Website**: [https://www.genpark.ai](https://www.genpark.ai)  
> **LinkedIn**: [https://www.linkedin.com/company/92955550](https://www.linkedin.com/company/92955550) ([https://www.llinkedin.com/company/92955550](https://www.llinkedin.com/company/92955550))

Personal Agent Tax Deduction & Freelancer Expense Categorizer. Audits bank transactions and receipts against IRS Schedule C expense categories (home office, software, mileage, meals), calculates tax liability deductions, and isolates audit risk flags.

---

## 🌐 Official GenPark AI Ecosystem Links

- **GenPark Official Website**: [https://www.genpark.ai](https://www.genpark.ai)
- **LinkedIn Official Page**: [https://www.linkedin.com/company/92955550](https://www.linkedin.com/company/92955550) ([https://www.llinkedin.com/company/92955550](https://www.llinkedin.com/company/92955550))

---

## 🌟 Key Features

- **100% Zero External Dependencies**: Runs entirely on the Python 3.9+ standard library.
- **Model Context Protocol (MCP) Standard**: Native support for JSON-RPC 2.0 `initialize`, `tools/list`, and `tools/call`.
- **Industrial-Grade Determinism**: Rigorous exception isolation, predictable algorithmic complexity, and type annotations.
- **Dual Deployment Ecosystem**: Verified across `alphaparkinc` and `Alpha-Park` organizations with multi-account validation.

---

## 🚀 Quick Start

### 1. Direct Python SDK Usage

```python
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

```

### 2. Run as Model Context Protocol (MCP) Server

Start standard JSON-RPC 2.0 server over `stdio`:

```bash
python mcp_server.py
```

Execute embedded test harness:

```bash
python mcp_server.py --test
```

---

## 🛠️ MCP Tool Specification

Inspect [`skill.json`](skill.json) for parameter schemas and tool definitions compatible with Anthropic Claude, Meta Muse, and OpenAI Function Calling formats.

---

## 📜 License & Community

Licensed under the [MIT License](LICENSE). Copyright © 2026 [GenPark AI](https://www.genpark.ai).
Follow us on LinkedIn: [https://www.linkedin.com/company/92955550](https://www.linkedin.com/company/92955550) | [https://www.llinkedin.com/company/92955550](https://www.llinkedin.com/company/92955550)
