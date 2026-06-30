"""
Customer Churn Prediction — Streamlit App
Run: streamlit run app.py
"""
import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.graph_objects as go

# ─── Page config ───────────────────────────────────────────
st.set_page_config(
    page_title="Customer Churn Predictor",
    page_icon="📡",
    layout="wide"
)

# ─── Load model ────────────────────────────────────────────
@st.cache_resource
def load_model():
    return joblib.load("models/best_churn_model.pkl")

model = load_model()

# ─── Custom CSS ────────────────────────────────────────────
st.markdown("""
<style>
    .main { padding: 1rem 2rem; }
    .metric-card {
        background: #1e2130;
        border: 1px solid #2d3250;
        border-radius: 10px;
        padding: 16px 20px;
        text-align: center;
        margin-bottom: 10px;
    }
    .metric-label { color: #a0a8c0; font-size: 13px; margin-bottom: 4px; }
    .metric-value { color: #ffffff; font-size: 22px; font-weight: 700; }
    .risk-high   { background:#3d1515; border:1px solid #e74c3c; color:#f5a5a5; padding:15px 18px; border-radius:10px; margin-top:10px; }
    .risk-medium { background:#3d2e00; border:1px solid #f39c12; color:#ffd97a; padding:15px 18px; border-radius:10px; margin-top:10px; }
    .risk-low    { background:#0d2d1a; border:1px solid #27ae60; color:#7ee8a2; padding:15px 18px; border-radius:10px; margin-top:10px; }
    .risk-high strong, .risk-medium strong, .risk-low strong { font-size: 16px; }
    .section-title { font-size: 20px; font-weight: 700; color: #e0e4f0; margin-bottom: 12px; }
    .bullet { margin: 5px 0; font-size: 14px; }
</style>
""", unsafe_allow_html=True)

# ─── Header ────────────────────────────────────────────────
st.title("📡 Customer Churn Prediction")
st.markdown("Enter customer details in the sidebar to predict churn probability in real-time.")
st.markdown("---")

# ─── Sidebar inputs ────────────────────────────────────────
st.sidebar.header("🧑 Customer Profile")
st.sidebar.markdown("Fill in the customer details below:")

with st.sidebar.expander("👤 Demographics", expanded=True):
    gender         = st.selectbox("Gender", ["Male", "Female"])
    senior_citizen = st.selectbox("Senior Citizen", ["No", "Yes"])
    partner        = st.selectbox("Partner", ["No", "Yes"])
    dependents     = st.selectbox("Dependents", ["No", "Yes"])

with st.sidebar.expander("📋 Account Info", expanded=True):
    tenure            = st.slider("Tenure (months)", 0, 72, 12)
    contract          = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
    paperless_billing = st.selectbox("Paperless Billing", ["No", "Yes"])
    payment_method    = st.selectbox("Payment Method",
                                     ["Electronic check", "Mailed check",
                                      "Bank transfer (automatic)", "Credit card (automatic)"])

with st.sidebar.expander("💰 Charges", expanded=True):
    monthly_charges = st.slider("Monthly Charges ($)", 18.0, 120.0, 65.0, 0.5)
    total_charges   = st.slider("Total Charges ($)", 0.0, 9000.0,
                                 float(round(monthly_charges * max(tenure, 1), 2)), 10.0)

with st.sidebar.expander("📞 Phone Services", expanded=False):
    phone_service  = st.selectbox("Phone Service", ["No", "Yes"])
    multiple_lines = st.selectbox("Multiple Lines", ["No", "Yes", "No phone service"])

with st.sidebar.expander("🌐 Internet Services", expanded=False):
    internet_service  = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
    online_security   = st.selectbox("Online Security",   ["No", "Yes", "No internet service"])
    online_backup     = st.selectbox("Online Backup",     ["No", "Yes", "No internet service"])
    device_protection = st.selectbox("Device Protection", ["No", "Yes", "No internet service"])
    tech_support      = st.selectbox("Tech Support",      ["No", "Yes", "No internet service"])
    streaming_tv      = st.selectbox("Streaming TV",      ["No", "Yes", "No internet service"])
    streaming_movies  = st.selectbox("Streaming Movies",  ["No", "Yes", "No internet service"])

# ─── Feature Engineering ───────────────────────────────────
def build_input_df():
    senior       = 1 if senior_citizen == "Yes" else 0
    avg_monthly  = total_charges / (tenure + 1)
    addons       = [online_security, online_backup, device_protection,
                    tech_support, streaming_tv, streaming_movies]
    num_addons   = sum(1 for a in addons if a == "Yes")
    has_multiple = 1 if num_addons >= 3 else 0
    is_new       = 1 if tenure <= 3 else 0

    if   tenure <= 12: t_group = "0-12 months"
    elif tenure <= 24: t_group = "13-24 months"
    elif tenure <= 48: t_group = "25-48 months"
    else:              t_group = "49+ months"

    return pd.DataFrame([{
        "tenure": tenure, "MonthlyCharges": monthly_charges,
        "TotalCharges": total_charges, "AvgMonthlySpend": avg_monthly,
        "NumAddons": num_addons, "IsNewCustomer": is_new,
        "HasMultipleServices": has_multiple,
        "gender": gender, "SeniorCitizen": senior,
        "Partner": partner, "Dependents": dependents,
        "PhoneService": phone_service, "MultipleLines": multiple_lines,
        "InternetService": internet_service, "OnlineSecurity": online_security,
        "OnlineBackup": online_backup, "DeviceProtection": device_protection,
        "TechSupport": tech_support, "StreamingTV": streaming_tv,
        "StreamingMovies": streaming_movies, "Contract": contract,
        "PaperlessBilling": paperless_billing, "PaymentMethod": payment_method,
        "tenure_group": t_group
    }])

# ─── Compute prediction ────────────────────────────────────
input_df    = build_input_df()
churn_prob  = model.predict_proba(input_df)[0][1]
churn_pct   = round(churn_prob * 100, 1)

addons_count = sum(1 for a in [online_security, online_backup, device_protection,
                                tech_support, streaming_tv, streaming_movies] if a == "Yes")

# ─── Layout ────────────────────────────────────────────────
col_l, col_r = st.columns([1, 1], gap="large")

# LEFT — Customer Summary
with col_l:
    st.markdown('<div class="section-title">📊 Customer Summary</div>', unsafe_allow_html=True)

    r1c1, r1c2, r1c3 = st.columns(3)
    with r1c1:
        st.markdown(f'<div class="metric-card"><div class="metric-label">Tenure</div><div class="metric-value">{tenure} mo</div></div>', unsafe_allow_html=True)
    with r1c2:
        st.markdown(f'<div class="metric-card"><div class="metric-label">Monthly Charges</div><div class="metric-value">${monthly_charges:.0f}</div></div>', unsafe_allow_html=True)
    with r1c3:
        st.markdown(f'<div class="metric-card"><div class="metric-label">Contract</div><div class="metric-value">{contract.split()[0]}</div></div>', unsafe_allow_html=True)

    r2c1, r2c2, r2c3 = st.columns(3)
    with r2c1:
        st.markdown(f'<div class="metric-card"><div class="metric-label">Add-on Services</div><div class="metric-value">{addons_count}</div></div>', unsafe_allow_html=True)
    with r2c2:
        st.markdown(f'<div class="metric-card"><div class="metric-label">Senior Citizen</div><div class="metric-value">{senior_citizen}</div></div>', unsafe_allow_html=True)
    with r2c3:
        st.markdown(f'<div class="metric-card"><div class="metric-label">Internet</div><div class="metric-value">{internet_service}</div></div>', unsafe_allow_html=True)

    # Risk factors
    st.markdown("---")
    st.markdown('<div class="section-title">🔍 Risk Analysis</div>', unsafe_allow_html=True)

    fcol1, fcol2 = st.columns(2)
    with fcol1:
        st.markdown("**⚠️ Risk Factors**")
        risk_factors = []
        if contract == "Month-to-month":        risk_factors.append("Month-to-month contract")
        if tenure <= 12:                         risk_factors.append(f"Short tenure ({tenure} mo)")
        if internet_service == "Fiber optic":   risk_factors.append("Fiber optic service")
        if monthly_charges > 80:                risk_factors.append(f"High charges (${monthly_charges:.0f})")
        if online_security == "No" and internet_service != "No": risk_factors.append("No online security")
        if tech_support == "No" and internet_service != "No":    risk_factors.append("No tech support")
        if payment_method == "Electronic check": risk_factors.append("Electronic check payment")
        if risk_factors:
            for r in risk_factors: st.markdown(f'<div class="bullet">🔴 {r}</div>', unsafe_allow_html=True)
        else:
            st.markdown("✅ No major risk factors")

    with fcol2:
        st.markdown("**✅ Positive Signals**")
        positive = []
        if contract in ["One year","Two year"]:  positive.append(f"{contract} contract")
        if tenure > 24:                           positive.append(f"Loyal ({tenure} months)")
        if addons_count >= 3:                     positive.append(f"{addons_count} add-ons")
        if tech_support == "Yes":                 positive.append("Has tech support")
        if online_security == "Yes":              positive.append("Has online security")
        if positive:
            for p in positive: st.markdown(f'<div class="bullet">🟢 {p}</div>', unsafe_allow_html=True)
        else:
            st.markdown("⚠️ Few retention signals")

# RIGHT — Prediction
with col_r:
    st.markdown('<div class="section-title">🔮 Prediction Result</div>', unsafe_allow_html=True)

    # Gauge
    bar_color = '#e74c3c' if churn_prob > 0.6 else '#f39c12' if churn_prob > 0.35 else '#27ae60'
    fig = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        value=churn_pct,
        number={'suffix': '%', 'font': {'size': 44, 'color': 'white'}},
        delta={'reference': 26.5, 'increasing': {'color': '#e74c3c'},
               'decreasing': {'color': '#27ae60'}, 'font': {'size': 14}},
        title={'text': "Churn Probability", 'font': {'size': 18, 'color': '#a0a8c0'}},
        gauge={
            'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': '#a0a8c0',
                     'tickfont': {'color': '#a0a8c0'}},
            'bar': {'color': bar_color, 'thickness': 0.3},
            'bgcolor': 'rgba(0,0,0,0)',
            'bordercolor': 'rgba(0,0,0,0)',
            'steps': [
                {'range': [0,  35], 'color': 'rgba(39,174,96,0.15)'},
                {'range': [35, 60], 'color': 'rgba(243,156,18,0.15)'},
                {'range': [60,100], 'color': 'rgba(231,76,60,0.15)'}
            ],
            'threshold': {'line': {'color': 'white', 'width': 3},
                          'thickness': 0.8, 'value': churn_pct}
        }
    ))
    fig.update_layout(
        height=300,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font={'color': 'white'},
        margin=dict(l=30, r=30, t=50, b=10)
    )
    st.plotly_chart(fig, use_container_width=True)

    # Risk verdict
    if churn_prob > 0.6:
        risk_label  = "🔴 HIGH RISK — Likely to Churn"
        risk_class  = "risk-high"
        action      = "Immediate retention action needed. Offer discount, upgrade, or dedicated support."
        rec_actions = ["🎁 Offer loyalty discount (10–20%)", "📞 Personal outreach from account manager",
                       "⬆️ Upgrade to annual contract incentive", "🔒 Bundle security + tech support"]
    elif churn_prob > 0.35:
        risk_label  = "🟡 MEDIUM RISK — Monitor Closely"
        risk_class  = "risk-medium"
        action      = "Proactive outreach recommended. Consider loyalty incentives."
        rec_actions = ["📧 Send personalized retention email", "🎯 Offer targeted add-on trial",
                       "📋 Highlight contract savings"]
    else:
        risk_label  = "🟢 LOW RISK — Customer Stable"
        risk_class  = "risk-low"
        action      = "Customer appears stable. Continue standard engagement."
        rec_actions = ["✅ Continue standard communication", "🌟 Invite to loyalty rewards program",
                       "📣 Ask for referrals / reviews"]

    st.markdown(f"""
    <div class="{risk_class}">
        <strong>{risk_label}</strong><br>
        <span style="font-size:13px; opacity:0.9">💡 {action}</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("**📌 Recommended Actions:**")
    for a in rec_actions:
        st.markdown(f'<div class="bullet">{a}</div>', unsafe_allow_html=True)

# ─── Footer ────────────────────────────────────────────────
st.markdown("---")
st.caption("Model: Tuned XGBoost | Dataset: Telco Customer Churn (7,043 customers) | ROC-AUC: 0.847")

# ─────────────────────────────────────────────────────────
# SHAP Explanation Section
# ─────────────────────────────────────────────────────────
st.markdown("---")
st.markdown('<div class="section-title">🧠 Why This Prediction? (SHAP Explanation)</div>', unsafe_allow_html=True)
st.caption("This shows exactly which factors pushed the churn probability up or down for this specific customer.")

import shap
import matplotlib.pyplot as plt

@st.cache_resource
def get_shap_explainer():
    clf = model.named_steps['clf']
    return shap.TreeExplainer(clf)

explainer = get_shap_explainer()
pre_step = model.named_steps['pre']

# Transform the current customer's input
input_transformed = pre_step.transform(input_df)
cat_names = pre_step.named_transformers_['cat'].get_feature_names_out(
    ['gender','SeniorCitizen','Partner','Dependents','PhoneService','MultipleLines',
     'InternetService','OnlineSecurity','OnlineBackup','DeviceProtection','TechSupport',
     'StreamingTV','StreamingMovies','Contract','PaperlessBilling','PaymentMethod','tenure_group']
).tolist()
num_names = ['tenure','MonthlyCharges','TotalCharges','AvgMonthlySpend',
             'NumAddons','IsNewCustomer','HasMultipleServices']
all_names = num_names + cat_names

shap_vals = explainer.shap_values(input_transformed)

# Build waterfall plot
explanation = shap.Explanation(
    values=shap_vals[0],
    base_values=explainer.expected_value,
    data=input_transformed[0],
    feature_names=all_names
)

plt.style.use('dark_background')
fig = plt.figure(figsize=(9, 5))
shap.plots.waterfall(explanation, max_display=10, show=False)
fig = plt.gcf()
ax = plt.gca()

# Force dark-mode-friendly colors on every element of the plot
fig.patch.set_facecolor('#0e1117')
ax.set_facecolor('#0e1117')

# Recolor connector/dotted lines and axis elements so they're visible
for line in ax.get_lines():
    line.set_color('#6e7585')
    line.set_alpha(0.9)

for spine in ax.spines.values():
    spine.set_color('#6e7585')

ax.tick_params(colors='#e0e4f0')
ax.xaxis.label.set_color('#e0e4f0')
ax.yaxis.label.set_color('#e0e4f0')
ax.title.set_color('#e0e4f0')

# Also fix any text objects (feature value labels on the left)
for text in ax.texts:
    if text.get_color() in ['black', '#000000', (0, 0, 0, 1)]:
        text.set_color('#e0e4f0')

plt.tight_layout()
st.pyplot(fig, use_container_width=True)
plt.close()
plt.style.use('default')  # reset so it doesn't affect other plots in the app

st.caption("🔴 Red bars push the prediction toward churn. 🔵 Blue bars push it toward staying. "
           "Bars are ranked by impact size — the top bars matter most for this customer.")
