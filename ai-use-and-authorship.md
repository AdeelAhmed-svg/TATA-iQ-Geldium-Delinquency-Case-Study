# AI use and authorship

## What AI (Claude) did
- Explained concepts (EDA, missing-data types, imbalance, fairness metrics).
- Drafted and ran the analysis code in the working session.
- Drafted the written deliverables (EDA report, model plan, collections report, slide deck).

## What I did
- Supplied the simulation materials, dataset, and task requirements.
- Directed the analysis and determined the objectives for each task.
- Reviewed the outputs and checked findings against the dataset.
- Verified key statistics, model metrics, and business conclusions before including them in the final deliverables.
- Decided to standardise Employment_Status labels and use median imputation for missing values.
- Identified and investigated data-quality issues, including inconsistent employment labels, unrealistic tenure values, utilization rates above 100%, and contradictions between payment-history variables.
- Decided to exclude Age and Location from the predictive model and use them only for fairness testing.
- Reviewed and revised the written reports to ensure recommendations reflected the actual evidence from the analysis.
- Determined that the predictive models were not reliable enough for operational use and recommended a controlled pilot rather than model-based targeting.
- Re-ran `analysis/baseline_model.py` myself on [11/3/2026] and confirmed the results in the README.

## What I did not do
- I did not write the original analysis code from scratch. 
- I did not use AI to fill in or invent data values.
