# OrangeHRM Test Automation Suite

Automated end-to-end test suite for [OrangeHRM](https://opensource-demo.orangehrmlive.com) built with Python, Selenium WebDriver, and pytest — following the Page Object Model design pattern.

---

## Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.13 | Core language |
| Selenium 4.41 | Browser automation |
| pytest | Test runner |
| WebDriver Manager | Automatic driver management |
| Firefox + GeckoDriver | Browser |

---

## Project Structure
```
orangehrm_automation/
├── pages/
│   ├── login_page.py        # Login page locators and actions
│   ├── dashboard_page.py    # Dashboard page locators and actions
│   └── employee_page.py     # Employee search locators and actions
├── tests/
│   ├── test_login.py        # 3 login test cases
│   ├── test_dashboard.py    # 2 dashboard test cases
│   └── test_employee.py     # 2 employee search test cases
├── utils/
│   └── base_page.py         # Shared base class for all pages
├── conftest.py              # pytest fixtures (driver setup/teardown)
├── requirements.txt         # Dependencies
└── README.md
```

---

## Test Coverage

| Module | Test Case | Status |
|--------|-----------|--------|
| Login | Valid login redirects to dashboard | ✅ Pass |
| Login | Invalid credentials shows error | ✅ Pass |
| Login | Empty fields stays on login page | ✅ Pass |
| Dashboard | Heading displays correctly | ✅ Pass |
| Dashboard | Logout redirects to login | ✅ Pass |
| Employee | Search existing employee returns results | ✅ Pass |
| Employee | Search unknown employee shows no records | ✅ Pass |

---

## Setup & Run

### 1. Clone the repo
```bash
git clone https://github.com/safayetsawom/orangehrm-automation.git
cd orangehrm-automation
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run all tests
```bash
pytest -v
```

---

## Design Patterns Used

**Page Object Model (POM):** Each page of the application has a dedicated class that owns its locators and actions. Tests interact only with page methods — never with raw locators. This makes the suite maintainable and scalable.

**Base Page:** A shared `BasePage` class provides reusable methods (`click`, `type`, `get_text`, `is_visible`) that all page classes inherit, eliminating repetition.

**pytest Fixtures:** Driver initialisation and teardown is handled in `conftest.py` via a pytest fixture, keeping test files clean.

---

## Author

**Md.Safayet Hossain Sawom** — CSE Graduate | Aspiring SQA Engineer  
[GitHub](https://github.com/safayetsawom)
