# Drug Profile Template

Use this structure when presenting drug information summaries.

---

## 💊 {drug_name} ({generic_name})

**Class:** {drug_class} | **Schedule:** {schedule} | **Status:** {availability_status}

### Drug Details

| Field | Value |
|-------|-------|
| Brand Name | {brand_name} |
| Manufacturer | {manufacturer} |
| Route | {route_of_admin} |
| Dosage Forms | {dosage_forms} |
| NDC | {ndc_code} |

### Interactions

| Interacting Drug | Severity | Effect |
|-----------------|----------|--------|
| {interacting_drug} | {severity_emoji} {severity} | {interaction_effect} |

{severity_emoji mapping: minor=✅, moderate=⚠️, major=🚨, contraindicated=⛔}

### Inventory & Pricing

| Metric | Value |
|--------|-------|
| Stock Level | {stock_qty} units |
| Reorder Point | {reorder_point} |
| AWP | ${awp_price} |
| Last Dispensed | {last_dispensed_date} |

{if stock_qty < reorder_point: "⚠️ Below reorder point — initiate purchase order"}
{if severity == "major": "🚨 Major interaction flagged — pharmacist review required"}

---

*Generated from mcp-pharmacy | {timestamp}*
