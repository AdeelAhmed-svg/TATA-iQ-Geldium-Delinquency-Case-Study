# Credit Card Delinquency: Why I Recommended a Pilot Instead of a Model

**A case study from the Tata iQ GenAI-Powered Data Analytics job simulation (Forage)**

> **Please read first.** This was a self-paced *virtual job simulation* on Forage. It was **not employment, an internship or work for a real client**. The client (Geldium Finance) is fictional and the dataset was supplied by the simulation. Task materials and the dataset belong to Forage / Tata iQ and are **not** included in this repository.

**Status:** Simulation completed Oct 2026 · [[Certificate:(https://www.theforage.com/completion-certificates/ifobHAoMjQs9s6bKS/gMTdCXwDdLYoXZ3wG_ifobHAoMjQs9s6bKS_6abf9ae0934c474e6281eeb4_1792441273401_completion_certificate.pdf)]] · Author: Adeel Ahmed

---

## 1. Business problem
Geldium Finance wanted to reduce credit card delinquency. The simulated brief asked for four things: understand the customer data, plan a delinquency prediction model, turn findings into a collections strategy, and propose an ethical, explainable agentic-AI approach.

## 2. Objectives
- Assess whether customer data can predict who becomes delinquent.
- Recommend what the Collections team should do, based on what the data actually supports.
- Keep the approach fair, explainable and human-supervised.

## 3. The headline finding
**The data did not support a reliable prediction model, so I recommended against deploying one** and proposed a randomised, supportive-outreach pilot to learn what actually reduces delinquency.

| Check | Result |
|---|---|
| Delinquent customers | 80 of 500 (16%) |
| Accuracy of "predict nobody is delinquent" | 84% (so accuracy is a misleading metric here) |
| Logistic regression, 5-fold stratified CV | AUC ≈ 0.46, recall 41%, precision 14% |
| Depth-3 decision tree | AUC ≈ 0.53, recall 48%, precision 16% |
| Meaning | About as good as a coin flip (AUC 0.5) |

## 4. Dataset and privacy
- **Source:** provided inside the Forage simulation; 500 customer records, 19 columns (demographics, income, credit score, utilisation, balances, six months of payment status, and a delinquency flag).
- **Not published here.** The Forage Terms of Use restrict copying and redistributing program content, so no dataset, templates, task text or Forage page screenshots are included.
- The data appears to be synthetic. It contains no real personal data, but I still treat it as restricted.
- To reproduce the baseline you need your own access to the simulation.

## 5. Task-by-task summary

### Task 1: Exploratory data analysis
- Checked duplicates (none), data types and missing values: Income 7.8%, Loan_Balance 5.8%, Credit_Score 0.4%.
- Compared rows with and without missing values; no significant differences, so I treated the gaps as likely random (MNAR not ruled out for Income).
- Chose median imputation (mean and median were nearly equal; keeps the sample from shrinking). Standardised inconsistent employment labels.
- **Finding:** correlations with delinquency were near zero (|r| ≤ 0.045, all p > 0.3).
- **Data-quality flags:** `Missed_Payments` does not match the monthly history (r = 0.007); 81 customers have tenure longer than adult age; 4 utilisation values exceed 100%.

### Task 2: Predictive model plan
- Logistic regression (balanced class weights) as the main model, a shallow decision tree as comparison, evaluated with stratified 5-fold cross-validation.
- Age and location were excluded from the model and kept only for fairness checks.
- Metrics chosen for imbalance: recall, precision, F1, AUC, confusion matrix.
- **Result:** near-random performance (section 3). Repeated CV (10 times) gave AUC 0.45 ± 0.06, so the weakness is consistent, not bad luck.
- Code: [`analysis/baseline_model.py`](analysis/baseline_model.py).

### Task 3: Collections strategy report
- Compared delinquency rates across card type, age band, location, employment, utilisation, missed payments and tenure, with 95% confidence intervals.
- Highest-rate groups (age 46–60, Business card, short tenure) did not hold up after allowing for about 25 comparisons; age 46–60 had p = 0.04 on its own and was treated as a lead to test.
- Compared five options (reminders, hardship plans, personalised plans, financial education, credit-limit cuts). Recommended an **8-week randomised pilot** of early, supportive outreach with a control group. Credit-limit cuts were rejected on fairness and trust grounds.
- The 10% target reduction is a starting assumption, not derived from data.

### Task 4: Agentic AI framework
- A conceptual framework (not implemented): data pipeline → decision engine → action layer → learning loop.
- Human-in-the-loop tiers: AI acts alone on light reminders; humans approve hardship offers; humans lead escalation; disputes go to specialists.
- Controls: permanent control group, shadow mode before launch, accuracy and fairness gates for retraining, automatic rollback if complaints rise.
- Regulatory themes considered: ECOA, GDPR, FCA, FCRA.

## 6. Tools and methods actually used
Python (pandas, scikit-learn, scipy, matplotlib) · median imputation · logistic regression · decision tree · stratified cross-validation · Wilson confidence intervals · chi-square and Fisher tests · disparate-impact (four-fifths rule) checks.

## 7. How I used AI
I used Claude to explain concepts, help draft Python analysis code, and produce initial drafts of the written deliverables. I reviewed all outputs against the dataset and analysis results before using them. I verified the reported statistics, checked the logic behind the missing data assessment, model evaluation, and fairness considerations, and corrected or rewrote sections where necessary. I made the final decisions on data cleaning, including standardising employment-status labels, choosing median imputation for missing values, excluding Age and Location from the predictive model, and concluding that the model's performance was too weak for operational use. I also revised the recommendations to reflect the evidence from the analysis, resulting in the recommendation for a controlled pilot rather than deployment of the predictive model. I did not use AI to generate or fill in data values. Details in [`docs/ai-use-and-authorship.md`](docs/ai-use-and-authorship.md).

## 8. Limitations
- The model has no predictive value on this data; the recommendation rests on that finding.
- The data looks synthetic and internally inconsistent, so conclusions about real customers can't be drawn.
- Segment differences are exploratory; none is statistically reliable.
- Fairness ratios were computed on a near-random model, so they are mostly noise.
- Task 4 is a design, not a tested system. No business outcome was measured.
- A simulation, not a real engagement: no stakeholder feedback and no deployment.

## 9. What I learned
- Accuracy is the wrong headline metric on imbalanced data; the trivial baseline was 84%.
- A weak result is still a result: the honest recommendation was a controlled test, not a better algorithm.
- Check data consistency before modelling; several fields contradicted each other.
- Many group comparisons produce false leads unless you account for them.
- Data analysis is not only about finding patterns, but also about knowing when the data does not support a confident conclusion.
- Business recommendations should be driven by evidence; when the data is uncertain, testing and validation are often more valuable than making assumptions.

## 10. Repository structure
```
├── README.md
├── analysis/
│   └── baseline_model.py        # Task 2 baseline (no data included)
├── docs/
│   └── ai-use-and-authorship.md # what AI did vs. what I did
└── .gitignore                   # blocks datasets and Forage materials
```

## 11. Certificate
Forage job-simulation completion certificate: [(https://www.theforage.com/completion-certificates/ifobHAoMjQs9s6bKS/gMTdCXwDdLYoXZ3wG_ifobHAoMjQs9s6bKS_6abf9ae0934c474e6281eeb4_1792441273401_completion_certificate.pdf)]. It certifies completion of a self-paced simulation, not employment.

## Disclaimer
Independent learning project. Not affiliated with or endorsed by Tata iQ, Geldium Finance or Forage. Forage and Tata iQ names are used for identification only.
