# DevOps Assignment: FastAPI with Automated Testing & CI/CD

## 📌 Overview
This project demonstrates setting up a FastAPI backend, automating API testing using `pytest`, and integrating tests into a GitHub Actions CI/CD pipeline. The goal is to implement continuous testing in a DevOps workflow.

---

## 📂 Project Structure
```
📦 DevOps Assignment 2
├── apiserver.py                 # FastAPI backend
├── testAutomation.py            # Basic test script using requests
├── testAutomationPytest.py      # Pytest-based test script
├── .github/
│   └── workflows/
│       └── test.yml             # GitHub Actions workflow for CI/CD
└── README.md                    # Project documentation
```

---

## 🚀 Task Breakdown

### **Task 1: Set Up FastAPI Server**
1. Install dependencies:
   ```bash
   pip install fastapi uvicorn
   ```
2. Create `apiserver.py` with three endpoints: add, subtract, and multiply.
3. Run the server:
   ```bash
   python apiserver.py
   ```
4. Test endpoints in the browser:
   - `GET /add/2/2`
   - `GET /subtract/5/3`
   - `GET /multiply/2/3`

---

### **Task 2: Write Automated Tests**
1. Install `requests`:
   ```bash
   pip install requests
   ```
2. Create `testAutomation.py` to test API endpoints.
3. Run tests:
   ```bash
   python testAutomation.py
   ```

---

### **Task 3: Enhance Tests with Pytest**
1. Install `pytest`:
   ```bash
   pip install pytest
   ```
2. Create `testAutomationPytest.py` using `pytest.mark.parametrize`.
3. Run tests using:
   ```bash
   python -m pytest testAutomationPytest.py
   ```

---

### **Task 4: Integrate with GitHub Actions**
1. Create `.github/workflows/test.yml` with CI/CD configuration.
2. Commit and push:
   ```bash
   git add .
   git commit -m "Added CI/CD automation"
   git push origin main
   ```
3. View test results in the **GitHub Actions** tab.

---

## 📜 CI/CD Workflow (.github/workflows/test.yml)
```yaml
name: API Tests

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v2

      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: "3.10"

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install fastapi uvicorn pytest requests

      - name: Start FastAPI server
        run: |
          nohup python apiserver.py &
        env:
          PYTHONUNBUFFERED: 1

      - name: Wait for server to be ready
        run: sleep 5

      - name: Run tests
        run: pytest testAutomationPytest.py
```

---

## 🔗 Future Enhancements
- Add database integration (PostgreSQL/MongoDB).
- Implement authentication with JWT/OAuth.
- Include logging and performance monitoring.

---

## 👨‍💻 Author
*Ashraf Jamal(500109928)*  
GitHub: Ashraf Jamal (https://github.com/Ashraf2534)  

---

## 📜 License
This project is open-source and available under the [MIT License](LICENSE).
