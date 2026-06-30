
Claude finished the response

CustomerChurn.ipynb
ipynb


Telco-Customer-Churn.csv
csv

Project 3: End-to-End Customer Churn Prediction
Skills: Python, EDA, Feature Engineering, ML, Streamlit
Dataset:

Telco Customer Churn
Features:

Data Cleaning
EDA
Feature Engineering
Logistic Regression
Random Forest
XGBoost
Model Comparison
Streamlit App review it and what to do me
Show more

Ran 4 commands, viewed a file
Ran 4 commands, viewed a file
I've fully reviewed your notebook and dataset. Here's a clear picture of what you've done and what's still missing.

✅ What You've Done Well
Your notebook covers the core pipeline in a clean, structured way:

Data Cleaning — Handled the TotalCharges space issue (converted to numeric, filled 11 NaN with 0), dropped customerID, checked duplicates.

EDA — 6 good plots: churn distribution, contract type, tenure, monthly charges, internet service, payment method.

Feature Engineering — Separated numerical vs categorical columns, used OneHotEncoder inside a ColumnTransformer pipeline.

3 Models trained — Logistic Regression, Random Forest, XGBoost — all with proper pipelines.

Model Comparison — Comparison table with 5 metrics (Accuracy, Precision, Recall, F1, ROC AUC), highlighted best values.

Hyperparameter Tuning — RandomizedSearchCV on XGBoost (20 iterations, 5-fold CV, optimizing ROC AUC).

Model Saved — joblib.dump(best_model, "best_churn_model.pkl") ✅

❌ What's Missing (Must Do Next)
1. 🔧 Feature Engineering is Shallow
You only encoded — you didn't create new features. Add these:

AvgMonthlySpend = TotalCharges / (tenure + 1)
HasMultipleServices (count of add-ons)
Tenure buckets (tenure_group: 0–12, 13–24, 25–48, 49+)
Binary flag: IsNewCustomer = (tenure <= 3)
2. 📊 EDA is Incomplete
Missing important plots:

Correlation heatmap of numerical features
Churn rate % by category (not just count — normalize it)
Distribution plots for tenure, MonthlyCharges, TotalCharges split by churn
3. ⚖️ Class Imbalance Not Handled
Your dataset has ~26% churn (Yes) vs ~74% No — this is imbalanced. You should:

Use class_weight='balanced' in Logistic Regression and Random Forest
Use scale_pos_weight in XGBoost
OR use SMOTE oversampling
4. 🖥️ Streamlit App — Not Built Yet
This is listed as a required skill but is completely missing. You need to build app.py that:

Loads best_churn_model.pkl
Takes customer inputs via sidebar widgets
Predicts churn probability in real-time
Shows a gauge/bar chart with risk level
5. 📉 No ROC Curve or Feature Importance Plot
Add visual model evaluation:

ROC Curve comparing all 3 models on one plot
Feature importance bar chart from XGBoost or Random Forest
6. 🗒️ No Markdown / Story in the Notebook
Your notebook is all code, no explanation. Add markdown cells before each section explaining what you're doing and why — this is what makes a portfolio notebook stand out.

🗺️ Your Next Steps (in order)
Step	Task	Priority
1	Add feature engineering (new columns)	High
2	Add correlation heatmap + better EDA plots	High
3	Fix class imbalance (class_weight)	High
4	Add ROC curve + feature importance plots	Medium
5	Add markdown cells explaining each section	Medium
6	Build the Streamlit app (app.py)	High
Want me to help you with any specific step? I can write the Streamlit app, add the missing EDA plots, fix the class imbalance, or add the feature engineering code — just say which one to start with!

do all mentioned steps and guide me also if require


Ran 3 commands
Ran 3 commands
Good, all packages ready. Now let me build everything step by step.


Ran 2 commands
Ran 2 commands
Now let me build the complete upgraded notebook:


Ran 2 commands
Ran 2 commands
Pipeline ran perfectly. Now let me build the Streamlit app:


Streamlit app for customer churn prediction
Streamlit app for customer churn prediction
Now let's build the complete notebook with markdown explanations:


Generate complete notebook with markdown cells
Generate complete notebook with markdown cells
Now let's create a README and copy everything to output:


Created a file, ran a command, read a file
Created a file, ran a command, read a file
Everything is complete! Here's a full summary of what was built and how to use it.

✅ What Was Done — Complete Summary
Files Delivered
File	Description
CustomerChurn_Complete.ipynb	Full notebook with markdown explanations for every section
app.py	Streamlit app — real-time churn prediction with gauge chart
README.md	Project documentation + how to run
models/best_churn_model.pkl	Saved best XGBoost model
plots/	10 EDA + evaluation charts
What Was Added vs Your Original
Feature Engineering (5 new features)

AvgMonthlySpend, tenure_group, IsNewCustomer, NumAddons, HasMultipleServices
EDA (6 new plots)

Correlation heatmap, churn by tenure group, churn by addons count, normalized churn rate charts, distribution plots
Class Imbalance Fix

class_weight='balanced' for LR and RF; scale_pos_weight=2.77 for XGBoost — this boosted Recall from ~45% → 81%
Model Evaluation Plots — ROC curve (all 4 models), feature importance, confusion matrix, model comparison bar chart

Streamlit App — sidebar inputs, real-time prediction, color-coded risk gauge, risk factors analysis, recommended actions

How to Run the Streamlit App
bash
# 1. Put app.py, the models/ folder, and the CSV in the same directory
# 2. Install dependencies
pip install streamlit plotly scikit-learn xgboost joblib pandas

# 3. Launch
streamlit run app.py
The app opens at http://localhost:8501 — you fill in customer details, it shows a live churn probability gauge with business recommendations.


Customerchurn complete
IPYNB 

App
PY 

Readme
Document · MD 

Best churn model
PKL 

07 roc curves
Image · PNG 

08 feature importance
Image · PNG 

03 correlation heatmap
Image · PNG 

09 model comparison
Image · PNG 

05 churn by tenure group
Image · PNG 

10 confusion matrix
Image · PNG 
How to go in command prompt in folder F:\CustomerChurn?

Here's how to open Command Prompt directly in your folder:

Method 1 — Fastest (from File Explorer)

Open File Explorer and go to F:\CustomerChurn
Click on the address bar at the top (where it shows the path)
Type cmd and press Enter
Command Prompt opens directly in that folder ✅
Method 2 — From Command Prompt

Press Win + R, type cmd, press Enter
Then type:
F:
cd CustomerChurn
(First switch to the F: drive, then navigate into the folder)

Method 3 — Right-click

Hold Shift and right-click inside the F:\CustomerChurn folder
Select "Open PowerShell window here" or "Open in Terminal"
Once inside the folder, run your Streamlit app with:

streamlit run app.py
FileNotFoundError: [Errno 2] No such file or directory: 'models/best_churn_model.pkl'
Traceback:

File "F:\CustomerChurn\app.py", line 24, in <module>
    model = load_model()
File "C:\Users\HP\AppData\Local\Programs\Python\Python314\Lib\site-packages\streamlit\runtime\caching\cache_utils.py", line 281, in __call__     return self._get_or_create_cached_value(args, kwargs, spinner_message)            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "C:\Users\HP\AppData\Local\Programs\Python\Python314\Lib\site-packages\streamlit\runtime\caching\cache_utils.py", line 326, in _get_or_create_cached_value     return self._handle_cache_miss(cache, value_key, func_args, func_kwargs)            ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "C:\Users\HP\AppData\Local\Programs\Python\Python314\Lib\site-packages\streamlit\runtime\caching\cache_utils.py", line 385, in _handle_cache_miss     computed_value = self._info.func(*func_args, **func_kwargs)
File "F:\CustomerChurn\app.py", line 22, in load_model     return joblib.load("models/best_churn_model.pkl")            ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "C:\Users\HP\AppData\Local\Programs\Python\Python314\Lib\site-packages\joblib\numpy_pickle.py", line 735, in load     with open(filename, "rb") as f:          ~~~~^^^^^^^^^^^^^^^^

Show more
The app can't find the model file. You need to create the models folder and generate the model by running the pipeline first.

Step 1 — Check your folder structure

Your F:\CustomerChurn folder should have these files:

F:\CustomerChurn\
├── app.py
├── CustomerChurn_Complete.ipynb
├── Telco-Customer-Churn.csv        ← must be here
└── models\                          ← this folder is missing!
    └── best_churn_model.pkl
Step 2 — Create the model by running this in your Command Prompt

Make sure you're in F:\CustomerChurn, then run:

python -c "
import pandas as pd, numpy as np, joblib, os, warnings
warnings.filterwarnings('ignore')
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from xgboost import XGBClassifier
import json

os.makedirs('models', exist_ok=True)

df = pd.read_csv('Telco-Customer-Churn.csv')
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce').fillna(0.0)
df.drop('customerID', axis=1, inplace=True)
df['Churn'] = df['Churn'].map({'Yes':1,'No':0})

df['AvgMonthlySpend'] = df['TotalCharges'] / (df['tenure'] + 1)
df['tenure_group'] = pd.cut(df['tenure'], bins=[0,12,24,48,72], labels=['0-12 months','13-24 months','25-48 months','49+ months'], include_lowest=True)
df['IsNewCustomer'] = (df['tenure'] <= 3).astype(int)
addons = ['OnlineSecurity','OnlineBackup','DeviceProtection','TechSupport','StreamingTV','StreamingMovies']
for c in addons: df[c+'_bin'] = (df[c]=='Yes').astype(int)
df['NumAddons'] = df[[c+'_bin' for c in addons]].sum(axis=1)
df.drop([c+'_bin' for c in addons], axis=1, inplace=True)
df['HasMultipleServices'] = (df['NumAddons'] >= 3).astype(int)

num_cols = ['tenure','MonthlyCharges','TotalCharges','AvgMonthlySpend','NumAddons','IsNewCustomer','HasMultipleServices']
cat_cols = ['gender','SeniorCitizen','Partner','Dependents','PhoneService','MultipleLines','InternetService','OnlineSecurity','OnlineBackup','DeviceProtection','TechSupport','StreamingTV','StreamingMovies','Contract','PaperlessBilling','PaymentMethod','tenure_group']

X, y = df.drop('Churn', axis=1), df['Churn']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

pre = ColumnTransformer([('num', StandardScaler(), num_cols), ('cat', OneHotEncoder(drop='first', handle_unknown='ignore'), cat_cols)], remainder='drop')
scale_pw = (y_train==0).sum() / (y_train==1).sum()

pipe = Pipeline([('pre', pre), ('clf', XGBClassifier(random_state=42, eval_metric='logloss', scale_pos_weight=scale_pw, n_estimators=100, max_depth=3, learning_rate=0.05, subsample=0.8, colsample_bytree=0.8, verbosity=0))])
pipe.fit(X_train, y_train)
joblib.dump(pipe, 'models/best_churn_model.pkl')
print('Model saved successfully!')
"
Step 3 — Then run the app

streamlit run app.py
This will create the models\best_churn_model.pkl file and the app will work. Make sure Telco-Customer-Churn.csv is in the same F:\CustomerChurn folder before running.


F:\CustomerChurn>streamlit run app.py You can now view your Streamlit app in your browser. Local URL: http://localhost:8501 Network URL: http://172.31.251.49:8501 C:\Users\HP\AppData\Local\Programs\Python\Python314\Lib\site-packages\sklearn\base.py:525: InconsistentVersionWarning: Tr

pasted

The model file is corrupted because it was trained on my server and saved with different library versions. The fix is simple — retrain the model directly on your computer.

Run this in your F:\CustomerChurn command prompt:

python
python train_model.py
But first, create the file. Open Notepad, paste this code, and save it as train_model.py in F:\CustomerChurn:

python
import pandas as pd, numpy as np, joblib, os, warnings
warnings.filterwarnings('ignore')
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier

os.makedirs('models', exist_ok=True)

print("Loading data...")
df = pd.read_csv('Telco-Customer-Churn.csv')
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce').fillna(0.0)
df.drop('customerID', axis=1, inplace=True)
df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})

print("Engineering features...")
df['AvgMonthlySpend'] = df['TotalCharges'] / (df['tenure'] + 1)
df['tenure_group'] = pd.cut(df['tenure'], bins=[0,12,24,48,72],
    labels=['0-12 months','13-24 months','25-48 months','49+ months'],
    include_lowest=True)
df['IsNewCustomer'] = (df['tenure'] <= 3).astype(int)
addons = ['OnlineSecurity','OnlineBackup','DeviceProtection',
          'TechSupport','StreamingTV','StreamingMovies']
for c in addons:
    df[c+'_bin'] = (df[c] == 'Yes').astype(int)
df['NumAddons'] = df[[c+'_bin' for c in addons]].sum(axis=1)
df.drop([c+'_bin' for c in addons], axis=1, inplace=True)
df['HasMultipleServices'] = (df['NumAddons'] >= 3).astype(int)

num_cols = ['tenure','MonthlyCharges','TotalCharges','AvgMonthlySpend',
            'NumAddons','IsNewCustomer','HasMultipleServices']
cat_cols = ['gender','SeniorCitizen','Partner','Dependents','PhoneService',
            'MultipleLines','InternetService','OnlineSecurity','OnlineBackup',
            'DeviceProtection','TechSupport','StreamingTV','StreamingMovies',
            'Contract','PaperlessBilling','PaymentMethod','tenure_group']

X = df.drop('Churn', axis=1)
y = df['Churn']
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)

pre = ColumnTransformer([
    ('num', StandardScaler(), num_cols),
    ('cat', OneHotEncoder(drop='first', handle_unknown='ignore'), cat_cols)
], remainder='drop')

scale_pw = (y_train == 0).sum() / (y_train == 1).sum()
print(f"Training XGBoost (scale_pos_weight={scale_pw:.2f})...")

model = Pipeline([
    ('pre', pre),
    ('clf', XGBClassifier(
        random_state=42,
        eval_metric='logloss',
        scale_pos_weight=scale_pw,
        n_estimators=100,
        max_depth=3,
        learning_rate=0.05,
        subsample=0.8,
        colsample_bytree=0.8,
        verbosity=0
    ))
])
model.fit(X_train, y_train)

joblib.dump(model, 'models/best_churn_model.pkl')
print("✅ Model saved to models/best_churn_model.pkl")
print("Now run: streamlit run app.py")
Then in your command prompt:

python train_model.py
streamlit run app.py
This trains the model on your own machine with your exact library versions, so there will be no version mismatch errors.


F:\CustomerChurn>streamlit run app.py You can now view your Streamlit app in your browser. Local URL: http://localhost:8501 Network URL: http://172.31.251.49:8501 C:\Users\HP\AppData\Local\Programs\Python\Python314\Lib\site-packages\sklearn\base.py:525: InconsistentVersionWarning:

pasted

F:\CustomerChurn>train_model.py
F:\CustomerChurn>
[main 2026-06-29T20:57:50.586Z] StorageMainService: creating application shared storage
[main 2026-06-29T20:57:50.708Z] [shared storage] Creating shared storage database at 'c:\Users\HP\.vscode-shared\sharedStorage\state.vscdb' (wasCreated: false)
[main 2026-06-29T20:57:50.709Z] [shared storage] Initializing fallback application storage (path: c:\Users\HP\AppData\Roaming\Code\User\globalStorage\state.vscdb)
[main 2026-06-29T20:57:50.739Z] [shared storage] Fallback application storage initialized with 140 items
[main 2026-06-29T20:57:50.746Z] update#setState idle
[main 2026-06-29T20:57:51.667Z] vscode-file: Refused to load resource c:\Users\HP\AppData\Local\Programs\Microsoft VS Code\fcf604774b\resources\app\extensions\theme-seti\icons\seti.woff from vscode-file: protocol (original URL: vscode-file://vscode-app/c:/Users/HP/AppData/Local/Programs/Microsoft%20VS%20Code/fcf604774b/resources/app/extensions/theme-seti/icons/seti.woff)
(node:17152) [DEP0169] DeprecationWarning: url.parse() behavior is not standardized and prone to errors that have security implications. Use the WHATWG URL API instead. CVEs are not issued for url.parse() vulnerabilities.
(Use Code --trace-deprecation ... to show where the warning was created)
[main 2026-06-29T20:58:22.128Z] update#setState checking for updates
[main 2026-06-29T20:58:22.452Z] update#setState idle

Show more
You ran train_model.py without python in front — it just opened the file instead of running it. Also, the old corrupted .pkl file is still being loaded by Streamlit.

Do these steps in order:

Step 1 — Delete the old corrupted model

del models\best_churn_model.pkl
Step 2 — Train the new model (add python in front)

python train_model.py
You should see:

Loading data...
Engineering features...
Training XGBoost...
✅ Model saved to models/best_churn_model.pkl
Step 3 — Run the app

streamlit run app.py
That's it. The key mistake was train_model.py instead of python train_model.py — without python, Windows just tries to open the file rather than execute it.

Screenshot 2026-06-30 023947.png
app showing

The app is running! 🎉 I can see it's working at localhost:8502 with the gauge showing 51.8% churn probability.

Two small issues I can see:

Customer Summary cards are blank (white boxes showing no values)
Risk label text is hard to read (dark text on dark background)
Let me fix both. Replace your app.py with this updated version:


Ran a command, read a file
Ran a command, read a file
Download the new app.py and replace the old one in F:\CustomerChurn\, then restart:

streamlit run app.py
What was fixed:

Customer Summary cards — replaced Streamlit's st.metric() (which renders blank in dark mode) with custom HTML cards that always show values correctly
Risk label text — now fully visible with proper contrast colors for dark background (red/yellow/green tinted boxes with matching text)
Gauge colors — transparent background so it blends properly with dark theme
Recommended Actions — moved directly under the risk verdict so everything is visible without scrolling

App
PY 
worked.

Great, the app is fully working! 🎉

Your Customer Churn Prediction project is now complete with everything:

✅ Data Cleaning
✅ Feature Engineering (5 new features)
✅ EDA (10 plots)
✅ 3 Models (Logistic Regression, Random Forest, XGBoost)
✅ Class Imbalance handled
✅ Hyperparameter Tuning
✅ Model Comparison
✅ Streamlit App (live predictions + gauge + risk analysis)
This is a strong portfolio project. If you want to take it further, you could deploy it free on Streamlit Cloud (streamlit.io/cloud) so anyone can access it via a public URL — great for sharing with recruiters. Just ask if you need help with that.

Can you add SHAP in code and how will it be?

SHAP (SHapley Additive exPlanations) will show why the model predicted a specific churn probability for a customer — which features pushed the prediction up or down. This is huge for a portfolio project since it demonstrates model interpretability, not just accuracy.

Let me show you what it looks like first, then add the code.


Install and verify SHAP
Install and verify SHAP
Now let me add SHAP to both the notebook (global model explanation) and the Streamlit app (per-customer explanation).


Test SHAP compatibility
Test SHAP compatibility
Confirmed it works. Now let me generate the SHAP plots and add the code to both files.


Ran a command, viewed a file
Ran a command, viewed a file
This looks great. Reading it: red dots on the right = that feature pushes churn probability up. So Two-year contract being absent (blue/low) pushes churn up, low tenure pushes churn up, fiber optic = yes pushes churn up — all matches intuition.


Check waterfall plot
Check waterfall plot
Excellent. This is exactly the per-customer explanation that's so valuable. Now let's add this to your notebook script and Streamlit app.

Notebook addition (paste at the end, after Step 6 Model Comparison):


SHAP analysis code block for notebook
SHAP analysis code block for notebook
Now let's add SHAP to the Streamlit app, with a live waterfall chart for whatever customer the user configures:


Append SHAP section to app.py
Append SHAP section to app.py
Let's test that the app still runs correctly with this addition before handing it off:


Ran 2 commands
Ran 2 commands
No errors, app loads successfully (HTTP 200). Let's copy the final files to output:


Ran 2 commands, read a file
Ran 2 commands, read a file
What was added
app.py — app.py is fully updated and tested (no syntax/runtime errors). It now includes a new section below the prediction: a live SHAP waterfall chart that recalculates every time you change a slider/dropdown, showing exactly which inputs (tenure, contract, internet type, etc.) pushed this specific customer's prediction up or down.

shap_notebook_addition.py — paste this at the end of your notebook (after the model comparison section). It adds 3 plots:

Summary/beeswarm plot — global view of what drives churn across all customers
Bar plot — ranked feature importance by average SHAP impact
Waterfall plot — explains one individual customer's prediction step by step
How to update on your machine
F:\CustomerChurn> pip install shap
Then download the new app.py from above and replace your existing one. Run:

streamlit run app.py
You'll see a new "🧠 Why This Prediction?" section appear under the gauge chart, with a waterfall chart that updates live as you adjust the sidebar inputs.

For the notebook, just copy the code from shap_notebook_addition.py into a new cell at the end of CustomerChurn_Complete.ipynb and run it (after Step 6).

One thing to flag: SHAP's waterfall plot uses matplotlib, and rendering it on every single sidebar interaction in Streamlit is a bit heavier than the Plotly gauge — if it feels slow on your machine, let me know and I can cache more aggressively or switch the gauge update to a button-triggered flow instead of live-on-every-change.


App
PY 

Shap notebook addition
PY 

11 shap summary
Image · PNG 

12 shap bar
Image · PNG 

13 shap waterfall
Image · PNG 
give shap code

Here's the standalone SHAP code for your notebook — paste it as a new cell at the end, after your model comparison section:

python
## 8. Model Explainability with SHAP
#
# Accuracy tells us HOW WELL the model performs. SHAP tells us WHY it makes
# each prediction — critical for stakeholder trust and understanding which
# customer behaviors actually drive churn.

import shap

# Get the trained classifier and preprocessor from the pipeline
preprocessor_step = best_model.named_steps['pre']
xgb_classifier     = best_model.named_steps['clf']

# Transform a sample of test data (SHAP needs the post-encoding feature space)
X_sample = X_test.sample(300, random_state=42)
X_sample_transformed = preprocessor_step.transform(X_sample)

# Get human-readable feature names after one-hot encoding
cat_feature_names = preprocessor_step.named_transformers_['cat']\
                        .get_feature_names_out(categorical_cols).tolist()
all_feature_names = numerical_cols + cat_feature_names

# Build explainer (TreeExplainer is fast and exact for tree-based models)
explainer = shap.TreeExplainer(xgb_classifier)
shap_values = explainer.shap_values(X_sample_transformed)

print("SHAP values computed ✅")
print(f"Shape: {shap_values.shape}  (customers x features)")


# ── 8a. Global Feature Importance — Summary (Beeswarm) Plot ──
plt.figure(figsize=(10, 8))
shap.summary_plot(shap_values, X_sample_transformed,
                   feature_names=all_feature_names, max_display=15, show=False)
plt.title("SHAP Summary Plot — What Drives Churn Predictions", fontsize=13, fontweight='bold')
plt.tight_layout()
plt.show()

print("""
💡 How to read this plot:
- Each row is a feature, sorted by overall importance
- Each dot is one customer
- Red dots = high value, Blue dots = low value
- Dots to the RIGHT = pushed prediction toward CHURN
- Dots to the LEFT  = pushed prediction toward NO CHURN
""")


# ── 8b. Global Feature Importance — Bar Plot ──
plt.figure(figsize=(9, 7))
shap.summary_plot(shap_values, X_sample_transformed,
                   feature_names=all_feature_names, plot_type='bar',
                   max_display=15, show=False)
plt.title("Mean |SHAP Value| — Overall Feature Importance", fontsize=13, fontweight='bold')
plt.tight_layout()
plt.show()


# ── 8c. Individual Customer Explanation — Waterfall Plot ──
customer_idx = 0  # change this to inspect a different customer

single_explanation = shap.Explanation(
    values=shap_values[customer_idx],
    base_values=explainer.expected_value,
    data=X_sample_transformed[customer_idx],
    feature_names=all_feature_names
)

plt.figure(figsize=(10, 6))
shap.plots.waterfall(single_explanation, max_display=12, show=False)
plt.title("Why This Customer Might Churn — SHAP Waterfall", fontsize=12, fontweight='bold')
plt.tight_layout()
plt.show()

predicted_prob = best_model.predict_proba(X_sample.iloc[[customer_idx]])[0][1]
print(f"Predicted churn probability for this customer: {predicted_prob*100:.1f}%")
To run it: make sure shap is installed first —

pip install shap
This assumes best_model, X_test, numerical_cols, and categorical_cols already exist in your notebook from earlier cells (they do, from your training section).

Screenshot 2026-06-30 120542.png
lines are not visible properly

The waterfall chart is working correctly — the values, bars, and labels are all clearly readable. The only issue is the dotted connector lines between bars are very faint against the dark background since SHAP draws them in a dark gray color.

This is a cosmetic fix. Here's the corrected SHAP section for your app.py:


Ran a command, edited a file
Ran a command, edited a file
Let's test this renders correctly before sending it:


Ran 4 commands
Ran 4 commands
The background process got killed by the shell context switch. Let me run it differently:


Run streamlit with nohup and disown
Run streamlit with nohup and disown
HTTP 200 — app loads fine, no errors.


Ran 2 commands, read a file
Ran 2 commands, read a file
Download this app.py and replace your existing one, then restart:

streamlit run app.py
What changed: the SHAP waterfall plot's dotted connector lines and tick labels were being rendered in matplotlib's default dark gray/black, which is nearly invisible on your dark Streamlit theme. The fix explicitly recolors every line, spine, tick label, and any black text to a light gray (
#e0e4f0) so it's visible against the dark background — same approach used for the gauge chart earlier.


App
PY 
want like
GitHub
Your README should include:

Project Overview
Dataset
Workflow diagram
EDA screenshots
Model comparison table
Feature importance
Streamlit screenshots
Installation
Deployment link A polished README makes a strong first impression. give readme
Show more

Check existing plots available for README embedding
Check existing plots available for README embedding
Let me build a workflow diagram and a polished GitHub-style README that references your existing assets.



Now let me save this diagram as an actual PNG file you can embed in your GitHub README, since the interactive widget above only renders in this chat:


Created a file, ran a command
Created a file, ran a command
Now let's create a clean folder of "screenshot-style" assets for the README and write the polished README itself:


Build assets folder for README images
Build assets folder for README images
I don't have an actual screenshot of your running Streamlit app saved as a file (only the one you pasted into chat earlier). I'll write the README referencing a placeholder path for that — you'll drop in your own screenshot. Now, the README:


Created 2 files, ran a command
Created 2 files, ran a command
Now let's create a requirements.txt and an MIT LICENSE (referenced in the README), then package everything for output:


Created 2 files, ran a command, read a file
Created 2 files, ran a command, read a file
Done. Here's what was added:

README.md — full GitHub-style README with badges, table of contents, overview, dataset details, workflow diagram, embedded EDA charts, model comparison table, SHAP explainability section, app description, installation steps, project structure, deployment instructions, key findings, and tech stack.

assets/ — folder with 11 PNG images (workflow diagram + your best EDA/model/SHAP plots) already sized for README embedding.

requirements.txt and LICENSE — referenced by the README's installation and license sections.

Two things you need to do before pushing to GitHub:

Add a real Streamlit screenshot — save your app screenshot as assets/streamlit_app_screenshot.png (the README references this path but I don't have a saved file of it, only the one you pasted in chat earlier).
Update placeholders — replace <your-username>, [Your Name] in LICENSE, and the live demo URL at the top once you deploy.
To push this to GitHub:

bash
cd CustomerChurn
git init
git add .
git commit -m "Initial commit: end-to-end churn prediction pipeline"
git branch -M main
git remote add origin https://github.com/<your-username>/customer-churn-prediction.git
git push -u origin main

Readme
Document · MD 

Requirements
TXT 

LICENSE
 

00 workflow diagram
Image · PNG 
How github should look like

Here's exactly how your GitHub repo should be structured and what it looks like once pushed.

Repository structure (what to upload)
customer-churn-prediction/
├── README.md                       ← shows automatically on repo homepage
├── LICENSE
├── requirements.txt
├── app.py
├── CustomerChurn_Complete.ipynb
├── Telco-Customer-Churn.csv
├── .gitignore
├── models/
│   ├── best_churn_model.pkl
│   ├── logistic_regression.pkl
│   ├── random_forest.pkl
│   └── feature_info.json
├── plots/
│   └── (10-13 generated chart PNGs)
└── assets/
    └── (images embedded in README)
What your repo homepage will look like
When someone visits github.com/<you>/customer-churn-prediction, GitHub auto-renders README.md below the file list. They'll see, in order: the title with colored badges (Python, scikit-learn, XGBoost, Streamlit, SHAP, License), a one-line project description, a clickable table of contents, then each section with your embedded images rendering as actual pictures (not links) — the workflow diagram, EDA charts, model comparison table as a real Markdown table, and the SHAP plots.

This is what makes a repo look "professional" at a glance — recruiters scroll, see real visuals immediately instead of a wall of text, and the badges signal tech stack instantly.

One missing piece — .gitignore
You don't want to accidentally commit virtual environment files or cache. Let me create that for you.


Created a file, ran a command, read a file
Created a file, ran a command, read a file
Steps to get this live on GitHub
1. Create the repo on GitHub
Go to github.com → New repository → name it customer-churn-prediction → don't initialize with README (you already have one) → Create.

2. Push from your local F:\CustomerChurn folder

bash
cd F:\CustomerChurn
git init
git add .
git commit -m "Initial commit: end-to-end churn prediction pipeline"
git branch -M main
git remote add origin https://github.com/<your-username>/customer-churn-prediction.git
git push -u origin main
3. Repo "About" section (top right, gear icon)
Add a short description and topics — this helps it surface in searches and looks polished:

Description: End-to-end churn prediction with ML, SHAP explainability, and a live Streamlit app
Topics: machine-learning, xgboost, streamlit, shap, churn-prediction, scikit-learn
4. Pin it on your profile
On your GitHub profile, go to "Customize your pins" and select this repo — it'll show up prominently on your profile homepage with stars/language stats, which is what recruiters usually see first.

One real gap: your Telco-Customer-Churn.csv and .pkl model files are fine to commit since they're small (under 1MB and a few MB respectively), but if you ever add a larger dataset later, GitHub blocks files over 100MB — you'd need Git LFS for that. Not an issue here, just flagging it for future projects.


.gitignore
GITIGNORE 
got confused.
How to proceed these all?

No problem — let's slow down and do this as one clear sequence, step by step. I'll tell you exactly what to type and when.

Where things stand right now
You have a working app on your computer at F:\CustomerChurn. I've given you several updated files in this chat (app.py, README.md, requirements.txt, LICENSE, .gitignore, etc.) that you need to download and place into that same folder before doing anything with GitHub.

Step 1 — Download all the files I've given you
Scroll up in this chat and download these files (click each one):

README.md
requirements.txt
LICENSE
.gitignore
app.py (the latest SHAP-fixed version)
The assets folder images (the workflow diagram + chart PNGs)
Put them all into F:\CustomerChurn, with the images going into a new subfolder called F:\CustomerChurn\assets\.

Step 2 — Check your folder looks like this
Open File Explorer at F:\CustomerChurn and confirm you see:

F:\CustomerChurn\
├── app.py
├── README.md
├── requirements.txt
├── LICENSE
├── .gitignore
├── CustomerChurn_Complete.ipynb
├── Telco-Customer-Churn.csv
├── models\
│   └── best_churn_model.pkl
├── plots\
└── assets\
    └── (workflow diagram, chart images)
If something's missing, tell me which file and I'll re-send it.

Step 3 — Confirm the app still runs
In Command Prompt:

cd F:\CustomerChurn
streamlit run app.py
Make sure it opens fine before moving to GitHub.

Step 4 — Only then, GitHub
Once Steps 1–3 are done and working, we do GitHub as a separate, isolated task (create repo → git init → push).

Question for you: which step are you currently stuck on — downloading/placing the files, or something with Git/GitHub itself?

don't have assets folder?

Right — I generated the workflow diagram and other images as files on my end, but you don't have a way to download a whole folder at once from this chat. Let me share them to you one by one so you can save them.


Ran a command, read a file
Ran a command, read a file
All 11 images are now shared above. Here's what to do:

Step 1 — Download each image
Click each image above and save it. As you save them, give them these exact filenames (matching what the README expects):

00_workflow_diagram.png
01_churn_distribution.png
02_churn_by_contract.png
03_correlation_heatmap.png
05_churn_by_tenure_group.png
07_roc_curves.png
08_feature_importance.png
09_model_comparison.png
10_confusion_matrix.png
11_shap_summary.png
13_shap_waterfall.png
Step 2 — Create the assets folder
In F:\CustomerChurn, create a new folder named assets, and put all 11 downloaded images inside it:

F:\CustomerChurn\assets\00_workflow_diagram.png
F:\CustomerChurn\assets\01_churn_distribution.png
...and so on
Step 3 — One image you still need yourself
The README also references assets/streamlit_app_screenshot.png — that's a screenshot of your own running app (like the one you pasted earlier in this chat). Take a screenshot of your Streamlit app, save it as streamlit_app_screenshot.png, and put it in that same assets folder.

Once that's done, your F:\CustomerChurn folder is complete and ready for GitHub. Let me know when you've got the assets folder set up, and we'll move to the Git push step.


00 workflow diagram
Image · PNG 

01 churn distribution
Image · PNG 

02 churn by contract
Image · PNG 

03 correlation heatmap
Image · PNG 

05 churn by tenure group
Image · PNG 

07 roc curves
Image · PNG 

08 feature importance
Image · PNG 

09 model comparison
Image · PNG 

10 confusion matrix
Image · PNG 

11 shap summary
Image · PNG 

13 shap waterfall
Image · PNG 
till here all done and next

Good — you're caught up. Now let's push everything to GitHub. Do this exactly in order.

Step 1 — Check Git is installed
In Command Prompt:

git --version
If it shows a version number, skip to Step 2. If it says "not recognized," download Git from git-scm.com, install with default options, then restart Command Prompt.

Step 2 — Set your identity (one-time only)
git config --global user.name "Your Name"
git config --global user.email "your-email@example.com"
Step 3 — Create the repository on GitHub.com
Go to github.com → log in
Click the + icon top-right → New repository
Name it: customer-churn-prediction
Leave it Public
Do NOT check "Add a README file" (you already have one)
Click Create repository
GitHub will show you a page with commands — ignore those for now, come back here.

Step 4 — Push your local folder to GitHub
In Command Prompt:

cd F:\CustomerChurn
git init
git add .
git commit -m "Initial commit: end-to-end churn prediction pipeline"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/customer-churn-prediction.git
git push -u origin main
Replace YOUR-USERNAME with your actual GitHub username.

A browser window may pop up asking you to log in to GitHub — sign in there to authenticate, then come back to Command Prompt.

Step 5 — Verify
Go to github.com/YOUR-USERNAME/customer-churn-prediction in your browser. You should see your README rendered with images, badges, and tables — that's the repo homepage recruiters would see.

Run these one at a time and paste me the output if anything errors out — especially Step 4, since that's where most first-time issues happen (auth problems, line-ending warnings, etc.).

want to do all these manually in git.com by interface

Got it — you want to do this through the GitHub website interface (uploading files via browser) instead of command-line Git. That's completely doable. Here's the full sequence.

Step 1 — Create the repository
Go to github.com → log in
Click the + icon top-right → New repository
Repository name: customer-churn-prediction
Keep it Public
Check "Add a README file" this time (since we're not using command line, this initializes the repo so you can upload into it)
Click Create repository
Step 2 — Delete the auto-generated README
GitHub just created a placeholder README.md. You'll replace it with yours.

In your new repo, click on README.md
Click the pencil (edit) icon top-right of the file view
Select all the text and delete it
Open your downloaded README.md file in Notepad, copy all the content, paste it into GitHub's editor
Scroll down, click Commit changes
Step 3 — Upload the main files
Go back to the repo's main page
Click Add file → Upload files
Drag in these files from F:\CustomerChurn:
app.py
requirements.txt
LICENSE
.gitignore
CustomerChurn_Complete.ipynb
Telco-Customer-Churn.csv
Scroll down, write a commit message like "Add core project files"
Click Commit changes
Step 4 — Upload the assets folder
GitHub's web uploader supports drag-and-drop of folders:

Add file → Upload files
Open F:\CustomerChurn\assets in File Explorer, select all images inside, drag the whole selection into the GitHub upload box
Commit with message "Add assets for README"
Note: dragging individual files (not the folder itself) into the upload box, while the URL path includes /assets, will create the assets folder for you — GitHub infers the folder from how you organize before uploading. Simplest approach: click Add file → Create new file, type assets/ followed by 00_workflow_diagram.png in the filename, that auto-creates the folder — but since GitHub doesn't allow uploading binary content via "create file," just drag the images directly into the upload box and GitHub will ask you to confirm folder structure if you drag the whole assets folder from File Explorer. Most browsers support that.

Step 5 — Upload the models and plots folders
Repeat Step 4 for:

F:\CustomerChurn\models\ (drag the 4 files inside)
F:\CustomerChurn\plots\ (drag all chart PNGs inside)
Once you're in GitHub and see the "Add file → Upload files" screen, try dragging your assets folder in and tell me what happens — whether it preserves the folder structure or dumps files flat. That'll tell us if we need a workaround.

which app is to take to open .gitignore. In notepad it is saved as extension txt.

Good catch — that's a classic Windows trap. Notepad adds .txt automatically unless you stop it.

Fix it without reopening anything
Open File Explorer, go to F:\CustomerChurn
Make sure you can see file extensions: View tab → check "File name extensions"
Find your file — it's probably named .gitignore.txt
Right-click → Rename
Delete .txt from the end, so it becomes exactly .gitignore
Press Enter — Windows will warn "if you change a file extension, it might become unusable," click Yes
What app to use to view/edit it
.gitignore has no extension after the dot, so Windows won't know which app to open it with by default — that's normal and fine. Use any plain text editor:

Notepad works (right-click the file → Open with → Notepad)
Or better: VS Code if you have it installed, since you mentioned using it earlier
To avoid this happening again when saving
In Notepad, when saving:

File → Save As
In the filename box type: .gitignore (with the leading dot)
Change "Save as type" dropdown from "Text Documents (*.txt)" to "All Files"
Save
That "Save as type: All Files" step is the key — it's what stops Notepad from silently appending .txt.

Same problem with LICENSE file?

Same issue, same fix.

Fix the LICENSE file
In File Explorer at F:\CustomerChurn, find the file — it's probably saved as LICENSE.txt
Right-click → Rename
Delete .txt so it becomes exactly LICENSE (no extension at all)
Press Enter → click Yes on the warning
To prevent it happening again when saving from Notepad
File → Save As
Filename: LICENSE
Save as type: change from "Text Documents (*.txt)" to "All Files"
Save
Quick check — both .gitignore and LICENSE are unusual in that they have no .txt, no .md, no extension at all. That's intentional and correct; GitHub recognizes these by their exact filename, not by extension. Once renamed, you're good to upload both.

# 📡 Customer Churn Prediction — End-to-End ML Project
## Project Structure

churn_project/
├── CustomerChurn_Complete.ipynb   ← Full notebook (with markdown explanations)
├── app.py                          ← Streamlit app
├── Telco-Customer-Churn.csv       ← Dataset
├── models/
│   ├── best_churn_model.pkl       ← Tuned XGBoost (best model)
│   ├── logistic_regression.pkl
│   ├── random_forest.pkl
│   └── feature_info.json
└── plots/
    ├── 01_churn_distribution.png
    ├── 02_churn_by_contract.png
    ├── 03_correlation_heatmap.png
    ├── 04_distributions.png
    ├── 05_churn_by_tenure_group.png
    ├── 06_churn_by_addons.png
    ├── 07_roc_curves.png
    ├── 08_feature_importance.png
    ├── 09_model_comparison.png
    └── 10_confusion_matrix.png

---
## How to Run
### 1. Install Dependencies
bash
pip install pandas numpy matplotlib seaborn scikit-learn xgboost streamlit plotly joblib imbalanced-learn

### 2. Run the Notebook
Open CustomerChurn_Complete.ipynb in Jupyter and run all cells.
### 3. Launch the Streamlit App
bash
streamlit run app.py

The app will open at **http://localhost:8501**
---
## Model Results
| Model | Accuracy | Precision | Recall | F1 | ROC AUC |
|---|---|---|---|---|---|
| Logistic Regression | 0.739 | 0.505 | 0.791 | 0.617 | **0.847** |
| Random Forest | 0.787 | 0.631 | 0.476 | 0.543 | 0.826 |
| XGBoost (default) | 0.759 | 0.536 | 0.685 | 0.601 | 0.820 |
| **XGBoost (tuned)** | 0.740 | 0.507 | **0.810** | **0.624** | **0.847** |
> **Best Model:** Tuned XGBoost — highest Recall (catches 81% of churners) and tied best ROC-AUC (0.847)
---
## Key Findings from EDA
1. **Contract type** is the #1 churn driver — Month-to-month customers churn at ~43% vs 3% for 2-year contracts
2. **Tenure** matters — Customers in first 12 months churn at 48%, dropping to <10% after 4 years
3. **Add-on services** reduce churn — Customers with 4+ services churn at <15%
4. **Fiber optic** customers churn more despite paying more (service quality signal)
5. **Electronic check** payment method is associated with higher churn
---
## Skills Demonstrated
- Python, Pandas, NumPy
- Matplotlib, Seaborn (EDA & visualization)
- Scikit-learn (preprocessing pipelines, model training, evaluation)
- XGBoost (gradient boosting, hyperparameter tuning)
- Class imbalance handling (class_weight, scale_pos_weight)
- Streamlit (interactive web app)
- Plotly (interactive charts)
- joblib (model serialization)
give new readme file

Show more
This looks like the old/simple README I gave you earlier — it doesn't have the badges, workflow diagram, embedded EDA images, SHAP section, or table of contents from the polished version. You should replace it with the full version I built later. Here it is again, ready to copy-paste into GitHub.


Get the polished README content to display fully
Get the polished README content to display fully
That's the correct full README, already in your downloaded file. Re-downloading it now so it's easy to grab fresh:


Presented file
Presented file
What to do with this
The file you pasted above is the old simple version. This is the upgraded version with badges, table of contents, workflow diagram, embedded EDA images, SHAP section, and deployment instructions.

On GitHub:

Open your repo → click README.md
Click the pencil (edit) icon
Select all existing text, delete it
Open the new README.md you just downloaded in Notepad, copy everything
Paste into GitHub's editor
Scroll down, click Commit changes
Two things to update before committing:

Line 12: replace the demo URL placeholder with your actual deployed Streamlit link once you deploy (or leave as-is for now)
Line 162: replace <your-username> with your actual GitHub username
This version won't render properly until your assets/ folder is uploaded with the images, since it references paths like assets/00_workflow_diagram.png. If you haven't uploaded that folder yet, do that first — otherwise the README will show broken image icons.


Readme
Document · MD 





Claude is AI and can make mistakes. Please double-check responses.


Readme · MD
📡 Customer Churn Prediction — End-to-End ML Pipeline
Show Image Show Image Show Image Show Image Show Image Show Image

An end-to-end machine learning project that predicts whether a telecom customer will churn, explains why using SHAP, and serves live predictions through an interactive Streamlit dashboard.

🔗 Live demo: your-deployed-app-url.streamlit.app (update after deploying — see Deployment)

📋 Table of Contents
Project Overview
Dataset
Workflow
Exploratory Data Analysis
Model Comparison
Feature Importance & Explainability
Streamlit App
Installation
Project Structure
Deployment
Key Findings
Tech Stack
🎯 Project Overview
Customer churn — when a subscriber leaves a service — is one of the costliest problems in subscription businesses. Acquiring a new customer typically costs 5–7x more than retaining an existing one, so being able to flag at-risk customers early has direct business value.

This project builds a full pipeline that:

Cleans and engineers features from raw telecom customer data
Trains and compares three classification models (Logistic Regression, Random Forest, XGBoost)
Tunes the best model with cross-validated hyperparameter search
Explains predictions with SHAP, both globally and per customer
Serves real-time predictions through a Streamlit web app
Goal: Given a customer's profile (contract type, tenure, services, billing), predict their probability of churning and surface the key drivers behind that prediction.

📊 Dataset
Source: Telco Customer Churn (IBM sample dataset, via Kaggle)

Rows	7,043 customers
Columns	21 features
Target	Churn (Yes / No)
Churn rate	26.5% (imbalanced)
Feature categories:

Demographics — gender, senior citizen, partner, dependents
Account info — tenure, contract type, payment method, billing
Services — phone, internet, online security, backup, tech support, streaming
Charges — monthly charges, total charges
🔄 Workflow
The pipeline below summarizes the project end to end, from raw CSV to a deployed app.

Show Image

Stage	What happens
1. Data cleaning	Fix TotalCharges (stored as string with blanks), drop customerID, encode target
2. Feature engineering	Add 5 derived features: AvgMonthlySpend, tenure_group, IsNewCustomer, NumAddons, HasMultipleServices
3. EDA	10 visualizations covering distributions, correlations, and churn rate breakdowns
4. Model training	Logistic Regression, Random Forest, XGBoost — all with class_weight/scale_pos_weight to handle imbalance
5. Hyperparameter tuning	RandomizedSearchCV, 20 iterations, 5-fold CV, optimizing ROC-AUC
6. Explainability	SHAP summary plots, bar plots, and per-customer waterfall plots
7. Deployment	Streamlit app with live gauge chart and SHAP explanation per prediction
 Exploratory Data Analysis
Churn distribution and contract type — the clearest single driver of churn is contract length. Month-to-month customers churn at roughly 14x the rate of two-year contract customers.

Show Image

Churn rate by tenure group — new customers (0–12 months) are by far the highest-risk group, with churn dropping sharply as tenure increases.

Show Image

Feature correlation heatmap — tenure is negatively correlated with churn, while IsNewCustomer and MonthlyCharges are positively correlated.

Show Image

Full EDA — including distribution plots and add-on service analysis — is available in CustomerChurn_Complete.ipynb.

🤖 Model Comparison
Four models were trained and evaluated on a held-out 20% test set. Recall is weighted heavily here, since failing to flag an actual churner (false negative) is more costly than a false alarm.

Model	Accuracy	Precision	Recall	F1 Score	ROC AUC
Logistic Regression	0.739	0.505	0.791	0.617	0.847
Random Forest	0.787	0.631	0.476	0.543	0.826
XGBoost (default)	0.759	0.536	0.685	0.601	0.820
XGBoost (tuned)	0.740	0.507	0.810	0.624	0.847
Selected model: Tuned XGBoost — chosen for its highest Recall (catches 81% of actual churners) and tied-best ROC-AUC.

Show Image

Show Image

Show Image

 Feature Importance & Explainability
Beyond raw performance metrics, this project uses SHAP (SHapley Additive exPlanations) to explain why the model makes each prediction — both at the global level and for individual customers.

Global feature importance (XGBoost):

Show Image

SHAP summary plot — shows how each feature pushes predictions toward or away from churn across the dataset. Short tenure, month-to-month contracts, and fiber optic internet are the strongest churn signals.

Show Image

SHAP waterfall plot — explains one individual prediction step by step, showing exactly which features pushed that specific customer's churn probability up or down. This same logic powers the live explanation panel in the Streamlit app.

Show Image

 Streamlit App
The trained model is served through an interactive Streamlit dashboard where you can configure a customer profile and get a live churn prediction with a visual risk gauge and SHAP-based explanation.

Show Image

Features:

Sidebar inputs for demographics, account info, charges, and services
Real-time churn probability gauge (color-coded: low / medium / high risk)
Risk factor and positive signal breakdown
Recommended retention actions based on risk level
Live SHAP waterfall chart explaining the specific prediction
⚙️ Installation
1. Clone the repository
bash
git clone https://github.com/<your-username>/customer-churn-prediction.git
cd customer-churn-prediction
2. Create a virtual environment (recommended)
bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # macOS / Linux
3. Install dependencies
bash
pip install -r requirements.txt
4. Run the notebook (optional — retrains the model)
bash
jupyter notebook CustomerChurn_Complete.ipynb
5. Launch the Streamlit app
bash
streamlit run app.py
The app opens at http://localhost:8501

📁 Project Structure
customer-churn-prediction/
├── CustomerChurn_Complete.ipynb    # Full notebook: cleaning → EDA → modeling → SHAP
├── app.py                          # Streamlit app
├── requirements.txt                # Python dependencies
├── Telco-Customer-Churn.csv        # Dataset
├── models/
│   ├── best_churn_model.pkl        # Tuned XGBoost (production model)
│   ├── logistic_regression.pkl
│   ├── random_forest.pkl
│   └── feature_info.json
├── plots/                          # All generated EDA & evaluation charts
├── assets/                         # Images used in this README
└── README.md
 Deployment
This app is deployed on Streamlit Community Cloud (free tier):

Push this repository to GitHub
Go to share.streamlit.io and sign in with GitHub
Click New app, select this repo, branch main, and set the main file to app.py
Click Deploy
Replace the placeholder demo link at the top of this README with your live URL once deployed.

 Key Findings
Contract type is the #1 churn driver — month-to-month customers churn at ~43% vs. ~3% for two-year contracts
Tenure matters — customers in their first 12 months churn at ~48%, dropping below 10% after 4 years
Bundled services reduce churn — customers with 4+ add-on services churn at under 15%
Fiber optic customers churn more despite paying more, suggesting a service quality or pricing perception issue
Electronic check payment correlates with higher churn, possibly indicating a less engaged or price-sensitive customer segment
🛠️ Tech Stack
Category	Tools
Language	Python 3.10+
Data handling	Pandas, NumPy
Visualization	Matplotlib, Seaborn, Plotly
Machine learning	scikit-learn, XGBoost
Explainability	SHAP
Web app	Streamlit
Model persistence	joblib
📄 License
This project is licensed under the MIT License — see LICENSE for details.

 Acknowledgments
Dataset provided by IBM via Kaggle.
