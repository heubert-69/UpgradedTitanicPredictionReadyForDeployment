# UpgradedTitanicPredictionReadyForDeployment

This project predicts passenger survival on the Titanic using **Logistic Regression** and **LightGBM**. The workflow includes **data cleaning, feature engineering, model training, evaluation, stress testing, statistical testing, causal inference, and A/B testing**.

> ⚠️ **Important:** This project is **for research and educational purposes only**. It must **not** be used for real-world decision-making, as incorrect predictions can lead to harm or misinterpretation.

---

## **Project Results**

### Logistic Regression (Test Set)
- Accuracy: 0.820
- ROC AUC: 0.891
- F1 Score: 0.821
- Confusion Matrix:  
[[92 18]
[16 53]]

yaml
Copy code

### LightGBM (Test Set)
- Accuracy: 0.858
- ROC AUC: 0.917
- F1 Score: 0.856
- Recall:
- Class 0: 0.818
- Class 1: 0.652

### Ensemble / Stacking
- Accuracy: 0.793
- ROC AUC: 0.837
- F1 Score: 0.730
- Cliff’s delta: 0.110 (negligible)
- McNemar test: p-value 0.118 → no significant improvement over LightGBM

---

## **Stress Testing & Robustness**

| Test | Accuracy | ROC AUC | F1 | Recall0 | Recall1 |
|------|---------|---------|----|---------|---------|
| Noise 5% | 0.749 | 0.806 | 0.662 | 0.818 | 0.638 |
| Noise 10% | 0.754 | 0.806 | 0.676 | 0.809 | 0.667 |
| Noise 20% | 0.771 | 0.806 | 0.701 | 0.818 | 0.696 |
| Domain Shift (more_first_class) | 0.732 | 0.787 | 0.662 | 0.764 | 0.681 |
| Domain Shift (more_third_class) | 0.743 | 0.774 | 0.671 | 0.782 | 0.681 |
| Feature Corruption 10% | 0.749 | 0.796 | 0.667 | 0.809 | 0.652 |

### Subgroup Testing
- First Class: Accuracy 0.667, Recall1 0.800  
- Third Class: Accuracy 0.750, Recall1 0.333  
- Children: Accuracy 0.750, Recall1 0.643  

---

## **Ethical Considerations**

- This model is trained on **historical Titanic data**. Real-world application is **inappropriate**.  
- Incorrect predictions could be harmful if applied to human life or safety decisions.  
- All results are intended for **research, learning, and demonstration purposes only**.

---

## **Installation**

```bash
git clone <your_repo_url>
cd titanic-survival
pip install -r requirements.txt
```

Running the FastAPI App
```bash
Copy code
uvicorn app:app --reload
Open your browser: http://127.0.0.1:8000/docs
```

Send a JSON payload to predict survival.

Docker:
```bash
docker build -t titanic-survival .
docker run -p 8000:8000 titanic-survival
```
API Usage Example:
```bash
Copy code
{
  "Pclass": 1,
  "Sex": "female",
  "Age": 29,
  "SibSp": 0,
  "Parch": 0,
  "Fare": 100
}
```
Response:

```bash
{
  "predicted_survival": 0.92
}
```
