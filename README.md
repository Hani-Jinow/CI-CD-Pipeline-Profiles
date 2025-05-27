# CI/CD Pipeline for Data Generation and Validation

This project demonstrates a complete CI/CD pipeline in Python for generating, transforming, testing, and deploying customer profile data using GitHub Actions and GitHub Pages.

---

## 🚀 Project Overview

The goal of this project is to simulate a real-world DevOps scenario with a focus on:

- Python scripting
- Unit testing
- Data transformation (CSV → JSON)
- GitHub Actions CI/CD workflows
- Deployment to GitHub Pages

---

## 📦 Features

- `generate.py` — Generates synthetic customer data using `faker`
- `csvtojson.py` — Converts the generated CSV (`profiles1.csv`) into JSON (`data.json`)
- `tests/` — Includes multiple unit tests to verify:
  - CSV file has the correct structure and row count
  - JSON file is correctly formed and complete
- `index.html` + `script.js` — Simple frontend to load and display the generated data

---

## 🧪 Testing

All tests are written using Python’s `unittest` framework and are executed automatically in the pipeline.

Tests include:
- CSV structure (column count, minimum rows)
- JSON structure (row count, number of properties per object)

To run tests locally:

```bash
python -m unittest discover -s tests -p '*Tests.py' -v
```

---

## ⚙️ CI/CD Pipeline (GitHub Actions)

The workflow is triggered on push and pull requests to `main`.  
The pipeline includes:

1. **Dependency Installation**
   - `pandas`
   - `faker`
2. **Script Execution**
   - `generate.py`
   - `csvtojson.py`
3. **Testing**
   - Runs all unit tests from the `tests/` folder
4. **Deployment**
   - Copies `index.html`, `script.js`, and `data.json` to the `dist/` directory
   - Deploys to GitHub Pages via `actions/deploy-pages`

---

## 🌍 Deployment

The site is automatically deployed via GitHub Pages after all tests pass.  
It displays the generated customer data from `data.json`.

---

## ✅ Technologies Used

- Python 
- pandas
- faker
- unittest
- GitHub Actions
- GitHub Pages

---
