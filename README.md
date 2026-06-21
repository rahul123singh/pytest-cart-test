# Pytest TDD/BDD Practice

A set of small, hands-on projects built to practice Test-Driven Development (TDD) and Behavior-Driven Development (BDD) using Python, `pytest`, and `behave`.

## Why this repo exists

Most testing gets done *after* code is written. This repo flips that order — each feature here was built test-first (RED → GREEN → REFACTOR), then reviewed for edge cases a "looks right" test would miss.

## Projects

### 1. Shopping Cart (`SHOPPING_CART/`)

A simple `Cart` class supporting:
- `add_item(name, price, quantity)` — add a line item
- `remove_item(name)` — remove all entries matching a name
- `get_total()` — sum of price × quantity across all items
- `apply_discount(percent)` — total after a percentage discount
- `get_item_count()` — number of distinct line items
- `total_quantity()` — total units across all items (distinct from item count)
- `show_items()` — formatted string listing cart contents
- `clear_cart()` — empties the cart
- `is_empty()` — checks if the cart has any items

**Tests:** `test_cart.py` — covers core behavior plus edge cases such as:
- Empty cart vs populated cart for `show_items()` and `get_item_count()`
- Removing an item that doesn't exist
- Discount boundaries (e.g. discounts over 100%)
- Distinguishing "line item count" from "total quantity" — a naming ambiguity worth testing explicitly rather than assuming

Run tests:
```bash
cd SHOPPING_CART
pytest test_cart.py -v
```

## What this practice reinforced

- **Write the test before trusting the code.** A password-strength check (in an earlier kata, not in this repo) used Python's `isalnum()` and silently passed despite not requiring both a letter and a digit. A test written *before* the code would have caught it immediately — one written after, almost didn't.
- **A test with no assertion tests nothing.** `cart.remove_item("Bread")` with no `assert` will always show "passed," regardless of what actually happens.
- **Avoid `if/else: assert True/False` patterns.** A direct `assert condition` is clearer and gives a useful failure message; the if/else version doesn't.
- **One test, one behavior.** Bundling many checks into a single test function makes failures harder to diagnose — split them so a failure points directly at what broke.

## Tech stack

- Python 3.13
- `pytest` for unit testing
- `behave` for BDD-style Gherkin scenarios (used in a companion password-validator kata)

---

*Built as part of ongoing practice in test automation and quality engineering.*
