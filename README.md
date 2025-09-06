

# Assignment 3: The MLOps Workflow

This project demonstrates a simple MLOps workflow with **Git best practices**, model versioning, and release management.

---

## 🎯 Objective
To apply professional MLOps practices in a machine learning project, focusing on:
- Ensuring **reproducibility** with versioned code and requirements.
- **Separating code from models/data** using `.gitignore`.
- Managing **releases** with Git tags and deployment branches.

---

## 📌 Scenario
As a junior MLOps engineer, I was tasked with managing a simple ML pipeline. The model is trained on the Iris dataset using scikit-learn, while Git is used for version control, release tagging, and deployment simulation.

---

## 🛠 Required Tools
- Git  
- Python (3.8 or above)  
- scikit-learn, joblib (installed via `requirements.txt`)  
- GitHub repository  

---

## 📂 Project Structure

mlops-project/ │-- train.py          # Training script for Iris dataset │-- requirements.txt  # Dependencies (scikit-learn, joblib) │-- .gitignore        # Ignore models, data, venv │-- README.md         # Documentation

---

## 🚀 Steps to Reproduce

### 1. Clone the Repository
```bash
git clone https://github.com/ayush20025/mlops-project.git
cd mlops-project

2. Create a Virtual Environment & Install Dependencies

python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
pip install -r requirements.txt

3. Run the Training Script

python train.py

This generates model.pkl (ignored by Git).

4. Make Code Changes

Edit train.py (e.g., change hyperparameter n_estimators from 100 → 200) and commit:

git add train.py
git commit -m "feat: Update n_estimators for better performance"

Run again:

python train.py

5. Create a Version Tag

git tag -a v1.0.0 -m "Release v1.0.0"
git push origin v1.0.0

6. Create a Deployment Branch

git checkout -b deployment/v1.0.0
git push origin deployment/v1.0.0


---

📦 Deliverables

GitHub Repository: https://github.com/ayush20025/mlops-project.git

Commit History:

feat: Initial training script and requirements.txt

feat: Update n_estimators for better performance


Ignored Files: model.pkl not committed (per .gitignore).

Release Tag: v1.0.0 visible in GitHub Releases/Tags.

Deployment Branch: deployment/v1.0.0 available in repo.



---

