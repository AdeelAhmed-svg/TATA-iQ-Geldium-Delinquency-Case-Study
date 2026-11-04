# Credit Card Delinquency: Why the Analysis Recommended a Pilot Instead of a Model

**A case study from the Tata iQ GenAI-Powered Data Analytics job simulation on Forage**

> **Please read first.** This was a self-paced *virtual job simulation* on Forage. It was **not employment, not an internship and not work for a real client**. The client (Geldium Finance) is fictional, and the dataset was supplied by the simulation. I am not and was never an employee of Tata or Tata iQ. The task materials and dataset belong to Forage / Tata iQ and are **not** included in this repository.

**Author:** Adeel Ahmed · **Completed:** October 2026 · [Forage completion certificate](https://www.theforage.com/completion-certificates/ifobHAoMjQs9s6bKS/gMTdCXwDdLYoXZ3wG_ifobHAoMjQs9s6bKS_6abf9ae0934c474e6281eeb4_1792441273401_completion_certificate.pdf) (certifies completion of a simulation)

---

## 1. How this project was done (AI use, stated up front)
The analysis code and the four written deliverables were **drafted and run by Claude (an AI assistant)**. I supplied the simulation materials, asked Claude to explain each concept, worked through the knowledge checks with it, and **submitted the deliverables as drafted, without editing them**. I have not independently rebuilt the analysis from scratch. This repository documents what the project found, not hands-on modelling experience. See [`docs/ai-use-and-authorship.md`](docs/ai-use-and-authorship.md).

## 2. Business problem
Geldium Finance (fictional) wanted to reduce credit card delinquency. The brief asked for four things: understand the customer data, plan a delinquency prediction model, turn findings into a collections strategy, and propose an ethical, explainable agentic-AI approach.

## 3. Objectives
- Assess whether the customer data can predict who becomes delinquent.
- Recommend what a Collections team should do, based on what the data actually supports.
- Keep the approach fair, explainable and human-supervised.

## 4. The headline finding
**The data did not support a reliable prediction model, so the recommendation was not to deploy one.** It proposed a randomised, supportive-outreach pilot to learn what actually reduces delinquency.

| Check | Result |
|---|---|
| Delinquent customers | 80 of 500 (16%) |
| Accuracy of "predict nobody is delinquent" | 84% (so accuracy is a misleading metric here) |
| Logistic regression, 5-fold stratified cross-validation | AUC ≈ 0.46, recall 41%, precision 14% |
| Depth-3 decision tree | AUC ≈ 0.53, recall 48%, precision 16% |
| Meaning | About as good as a coin flip (AUC 0.5) |

## 5. Dataset and privacy
- **Source:** provided inside the Forage simulation; 500 customer records, 19 columns (demographics, income, credit score, utilisation, balances, six months of payment status, and a delinquency flag).
- **Not published here.** The Forage Terms of Use restrict copying and redistributing program content, so no dataset, templates, task text, reports, slides or Forage page screenshots are included.
- The data appears to be synthetic and contains no real personal data, but it is treated as restricted.
- To reproduce the baseline you need your own access through the simulation.

## 6. Task-by-task summary

### Task 1: Exploratory data analysis
- Checked duplicates (none), data types and missing values: Income 7.8%, Loan_Balance 5.8%, Credit_Score 0.4%.
- Compared rows with and without missing values; no significant differences, so the gaps were treated as likely random (missing-not-at-random not ruled out for Income).
- Chose median imputation (mean and median were nearly equal; avoids shrinking a small sample). Standardised inconsistent employment labels.
- **Finding:** correlations with delinquency were near zero (|r| ≤ 0.045, all p > 0.3).
- **Data-quality flags:** `Missed_Payments` does not match the monthly history (r = 0.007); 81 customers have tenure longer than adult age; 4 utilisation values exceed 100%.

### Task 2: Predictive model plan
- Logistic regression (balanced class weights) as the main model, a shallow decision tree as a comparison, evaluated with stratified 5-fold cross-validation.
- Age and location were excluded from the model and kept only for fairness checks.
- Metrics chosen for class imbalance: recall, precision, F1, AUC, confusion matrix.
- **Result:** near-random performance (section 4). Repeated cross-validation gave AUC 0.45 ± 0.06, so the weakness is consistent.
- Code: [`analysis/baseline_model.py`](analysis/baseline_model.py).

### Task 3: Collections strategy report
- Compared delinquency rates across card type, age band, location, employment, utilisation, missed payments and tenure, with 95% confidence intervals.
- The highest-rate groups (age 46–60, Business card, short tenure) did not hold up after allowing for about 25 comparisons. Age 46–60 had p = 0.04 on its own and was treated as a lead to test.
- Compared five options (reminders, hardship plans, personalised plans, financial education, credit-limit cuts). Recommended an **8-week randomised pilot** of early, supportive outreach with a control group. Credit-limit cuts were rejected on fairness and trust grounds.
- The 10% target reduction and the sample-size estimate are planning assumptions, not data-derived results.

### Task 4: Agentic AI framework
- A conceptual framework, **not implemented**: data pipeline → decision engine → action layer → learning loop.
- Human-in-the-loop tiers: AI acts alone on light reminders; humans approve hardship offers; humans lead escalation; disputes go to specialists.
- Controls: permanent control group, shadow mode before launch, accuracy and fairness gates for retraining, automatic rollback if complaints rise.
- Regulatory themes considered: ECOA, GDPR, FCA, FCRA.

## 7. Tools and methods
Python (pandas, scikit-learn, scipy, matplotlib) · median imputation · logistic regression · decision tree · stratified cross-validation · Wilson confidence intervals · chi-square and Fisher tests · disparate-impact (four-fifths rule) checks. All run by Claude; see section 1.

## 8. Limitations
- The model has no predictive value on this data; the recommendation rests on that finding.
- The data looks synthetic and internally inconsistent, so nothing here can be generalised to real customers.
- Segment differences are exploratory; none is statistically reliable.
- Fairness ratios were computed on a near-random model, so they are mostly noise.
- Task 4 is a design, not a tested system. No business outcome was measured.
- A simulation, not a real engagement: no stakeholder feedback and no deployment.
- The analysis was AI-drafted and submitted unedited, and I have not independently reproduced all of it.

## 9. What I learned
- In my own words: data analysis used to take me much longer, and with GenAI's help you can build your strategies and reach a better analysis much faster.
- What the project showed: accuracy is the wrong headline metric on imbalanced data (the trivial baseline scored 84%), and an honest weak result is still a result. Here it meant recommending a controlled test, not a better algorithm.
- Fast AI-assisted analysis still needs checking. Several data fields contradicted each other, and many group comparisons produce false leads unless you account for them.
- Data analysis is not only about finding patterns, but also about knowing when the data does not support a confident conclusion.
- When the data is uncertain, testing and validation are often more valuable than making assumptions.

## 10. Repository structure
```
├── README.md
├── analysis/
│   └── baseline_model.py        # Task 2 baseline (no data included)
├── docs/
│   └── ai-use-and-authorship.md
└── .gitignore                   # blocks datasets and Forage materials
```

## Disclaimer
Independent learning project. Not affiliated with or endorsed by Tata iQ, Geldium Finance or Forage. Company and platform names are used for identification only.
