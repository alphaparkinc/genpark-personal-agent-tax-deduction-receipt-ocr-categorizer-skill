#!/usr/bin/env python3
import json
import sys
from client import PersonalAgentTaxDeductionCategorizer

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        agent = PersonalAgentTaxDeductionCategorizer()
        items = [
            {"merchant": "GitHub", "amount_usd": 21.0, "description": "Copilot Enterprise subscription"},
            {"merchant": "Starbucks", "amount_usd": 32.0, "description": "Client sync coffee"}
        ]
        res = agent.categorize_deductible_expenses(items, marginal_tax_bracket_pct=30.0)
        assert res["total_deductible_usd"] == 37.0 # 21 + 16 (50% of 32)
        assert res["estimated_tax_savings_usd"] == 11.1
        print(f"[TEST PASS] Tax Savings Estimated: ${res['estimated_tax_savings_usd']}")
        sys.exit(0)

    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            method = req.get("method")
            msg_id = req.get("id")
            if method == "initialize":
                print(json.dumps({"jsonrpc": "2.0", "id": msg_id, "result": {"serverInfo": {"name": "genpark-tax-deduction-agent", "version": "1.0.0"}}}))
            elif method == "tools/list":
                print(json.dumps({"jsonrpc": "2.0", "id": msg_id, "result": {"tools": [{"name": "categorize_deductible_expenses", "description": "Categorize expenses for IRS Schedule C tax deductions"}]}}))
            elif method == "tools/call":
                args = req.get("params", {}).get("arguments", {})
                agent = PersonalAgentTaxDeductionCategorizer()
                out = agent.categorize_deductible_expenses(args.get("expenses", []), float(args.get("marginal_tax_bracket_pct", 28.0)))
                print(json.dumps({"jsonrpc": "2.0", "id": msg_id, "result": {"content": [{"type": "text", "text": json.dumps(out)}]}}))
            else:
                print(json.dumps({"jsonrpc": "2.0", "id": msg_id, "error": {"code": -32601, "message": "Method not found"}}))
            sys.stdout.flush()
        except Exception as e:
            print(json.dumps({"jsonrpc": "2.0", "error": {"code": -32603, "message": str(e)}}))
            sys.stdout.flush()

if __name__ == "__main__":
    main()
