
import streamlit as st
import sys
from pathlib import Path

# ============================================================
# 1. PROJECT CONFIGURATION
# ============================================================

PROJECT_DIR = Path(__file__).resolve().parent.parent
SRC_DIR = Path(__file__).resolve().parent

sys.path.insert(0, str(SRC_DIR))

from predict import predict_passenger, threshold

st.set_page_config(
    page_title="Titanic | Survival Intelligence",
    page_icon="🚢",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# 2. SESSION STATE
# ============================================================

if "theme" not in st.session_state:
    st.session_state.theme = "Dark"

if "prediction_result" not in st.session_state:
    st.session_state.prediction_result = None

if "passenger_details" not in st.session_state:
    st.session_state.passenger_details = None

# ============================================================
# 3. THEME SELECTION
# ============================================================

st.sidebar.markdown("## 🎨 Appearance")

theme = st.sidebar.radio(
    "Choose your preferred theme",
    ["Dark", "Light"],
    horizontal=True,
    key="theme"
)

# ============================================================
# 4. THEME COLORS
# ============================================================

if theme == "Dark":

    colors = {
        "background": "#07111F",
        "sidebar": "#0A1728",
        "card": "#11263B",
        "hero_start": "#102B45",
        "hero_end": "#164E73",
        "text": "#F1F5F9",
        "muted": "#9DB5CB",
        "border": "#29445F",
        "accent": "#16A6CE",
        "result_start": "#123A50",
        "result_end": "#164E63",
        "input": "#0D1828",
        "success": "#65E6BD",
        "danger": "#FFB4A9",
        "info_bg": "#132D45"
    }

else:

    colors = {
        "background": "#F3F7FC",
        "sidebar": "#FFFFFF",
        "card": "#FFFFFF",
        "hero_start": "#DCEEFF",
        "hero_end": "#B8DCFA",
        "text": "#172B45",
        "muted": "#52677F",
        "border": "#D1DEEC",
        "accent": "#087EAE",
        "result_start": "#D9F0FA",
        "result_end": "#BFE5F2",
        "input": "#FFFFFF",
        "success": "#087C58",
        "danger": "#C03935",
        "info_bg": "#E7F2FC"
    }

# ============================================================
# 5. CUSTOM CSS
# ============================================================

st.markdown(f"""
<style>

@import url(
'https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap'
);

html, body, [class*="css"] {{
    font-family: 'Inter', sans-serif;
}}

.stApp {{
    background: {colors["background"]};
    color: {colors["text"]};
}}

[data-testid="stHeader"] {{
    background: transparent;
}}

[data-testid="stSidebar"] {{
    background: {colors["sidebar"]};
    border-right: 1px solid {colors["border"]};
}}

[data-testid="stSidebar"] p,
[data-testid="stSidebar"] label {{
    color: {colors["text"]};
}}

.hero {{
    background: linear-gradient(
        120deg,
        {colors["hero_start"]},
        {colors["hero_end"]}
    );
    padding: 35px;
    border-radius: 20px;
    border: 1px solid {colors["border"]};
    margin-bottom: 25px;
}}

.hero h1 {{
    font-size: 36px;
    font-weight: 800;
    color: {colors["text"]};
    margin-bottom: 10px;
}}

.hero p {{
    color: {colors["muted"]};
    font-size: 15px;
}}

.section-title {{
    font-size: 21px;
    font-weight: 700;
    color: {colors["text"]};
    margin: 20px 0 12px 0;
}}

.metric-card {{
    background: {colors["card"]};
    border: 1px solid {colors["border"]};
    padding: 20px;
    border-radius: 16px;
    min-height: 110px;
}}

.metric-label {{
    color: {colors["muted"]};
    font-size: 13px;
}}

.metric-value {{
    color: {colors["text"]};
    font-size: 27px;
    font-weight: 800;
    margin-top: 9px;
}}

.result-card {{
    background: linear-gradient(
        135deg,
        {colors["result_start"]},
        {colors["result_end"]}
    );
    border: 1px solid {colors["accent"]};
    border-radius: 18px;
    padding: 28px;
    text-align: center;
    margin-top: 15px;
    min-height: 285px;
}}

.result-card h2 {{
    color: {colors["text"]};
    font-size: 27px;
}}

.result-card p {{
    color: {colors["muted"]};
}}

div[data-testid="stMetric"] {{
    background: {colors["card"]};
    border: 1px solid {colors["border"]};
    padding: 16px;
    border-radius: 14px;
}}

[data-testid="stMetricLabel"],
[data-testid="stMetricValue"] {{
    color: {colors["text"]};
}}

.stProgress > div > div > div > div {{
    background-color: {colors["accent"]};
}}

div.stButton > button {{
    background: linear-gradient(
        90deg,
        {colors["accent"]},
        #20B8D8
    );
    color: white;
    border: none;
    border-radius: 10px;
    height: 48px;
    font-weight: 700;
    width: 100%;
}}

div.stButton > button:hover {{
    opacity: 0.85;
    color: white;
    border: none;
}}

[data-testid="stForm"] {{
    border: 1px solid {colors["border"]};
    border-radius: 14px;
    padding: 15px;
}}

[data-testid="stAlert"] {{
    background: {colors["info_bg"]};
}}

.footer {{
    text-align: center;
    color: {colors["muted"]};
    padding: 30px 10px;
    margin-top: 45px;
    border-top: 1px solid {colors["border"]};
    font-size: 13px;
}}

.footer strong {{
    color: {colors["accent"]};
}}

</style>
""", unsafe_allow_html=True)

# ============================================================
# 6. HEADER
# ============================================================

st.markdown("""
<div class="hero">

    <h1>🚢 Titanic Survival Intelligence</h1>

    <p>
        Machine Learning powered passenger survival prediction.
        Explore passenger information and generate predictions
        using a trained Logistic Regression model.
    </p>

</div>
""", unsafe_allow_html=True)

# ============================================================
# 7. SIDEBAR - PASSENGER INPUT
# ============================================================

st.sidebar.divider()

st.sidebar.markdown("## 🚢 TITANIC ML")
st.sidebar.caption("SURVIVAL PREDICTION SYSTEM")

st.sidebar.markdown("### Passenger Information")

with st.sidebar.form("passenger_form"):

    pclass = st.selectbox(
        "Passenger Class",
        [1, 2, 3],
        format_func=lambda x: {
            1: "1st Class",
            2: "2nd Class",
            3: "3rd Class"
        }[x]
    )

    sex = st.selectbox(
        "Gender",
        ["female", "male"]
    )

    age = st.number_input(
        "Age",
        min_value=0.0,
        max_value=100.0,
        value=25.0,
        step=1.0
    )

    fare = st.number_input(
        "Ticket Fare",
        min_value=0.0,
        max_value=600.0,
        value=80.0,
        step=1.0
    )

    embarked = st.selectbox(
        "Port of Embarkation",
        ["C", "Q", "S"],
        format_func=lambda x: {
            "C": "Cherbourg",
            "Q": "Queenstown",
            "S": "Southampton"
        }[x]
    )

    family_size = st.number_input(
        "Family Size",
        min_value=1,
        max_value=20,
        value=2,
        step=1
    )

    submitted = st.form_submit_button(
        "⚡ Predict Survival"
    )

st.sidebar.divider()

st.sidebar.caption("Model: Logistic Regression")
st.sidebar.caption(f"Decision Threshold: {threshold:.2f}")

# ============================================================
# 8. PROCESS PREDICTION
# ============================================================

if submitted:

    passenger = {
        "Pclass": pclass,
        "Sex": sex,
        "Age": age,
        "Fare": fare,
        "Embarked": embarked,
        "FamilySize": family_size
    }

    try:

        result = predict_passenger(passenger)

        st.session_state.prediction_result = result
        st.session_state.passenger_details = passenger.copy()

    except Exception as error:

        st.session_state.prediction_result = None
        st.session_state.passenger_details = None

        st.error(f"Prediction failed: {error}")

# ============================================================
# 9. PROJECT OVERVIEW
# ============================================================

left, right = st.columns([1.5, 1])

with left:

    st.markdown(
        '<div class="section-title">📊 Project Overview</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Training Accuracy", "80.76%")

    with col2:
        st.metric("Testing Accuracy", "79.89%")

    with col3:
        st.metric("ROC-AUC", "83.93%")

    st.markdown(
        '<div class="section-title">🧠 About the Model</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    This application uses a trained **Logistic Regression**
    model to estimate passenger survival probability.

    **Machine Learning Workflow**

    - Data preprocessing and missing-value imputation
    - Numerical feature scaling
    - Categorical feature encoding
    - Logistic Regression classification
    - Probability-based prediction
    """)

with right:

    st.markdown(
        '<div class="section-title">⚙️ Prediction Settings</div>',
        unsafe_allow_html=True
    )

    st.markdown(f"""
    <div class="metric-card">

        <div class="metric-label">
            CLASSIFICATION THRESHOLD
        </div>

        <div class="metric-value">
            {threshold * 100:.0f}%
        </div>

        <p style="color:{colors["muted"]};font-size:12px;">
            Probability ≥ {threshold * 100:.0f}% → Survived
        </p>

    </div>
    """, unsafe_allow_html=True)

    st.write("")

    st.info(
        "Enter passenger details in the sidebar "
        "and select Predict Survival to generate a result."
    )

# ============================================================
# 10. PREDICTION RESULTS
# ============================================================

if st.session_state.prediction_result is not None:

    result = st.session_state.prediction_result
    passenger = st.session_state.passenger_details

    probability = result["survival_probability"]
    prediction = result["prediction"]

    st.divider()

    st.markdown(
        '<div class="section-title">🎯 Prediction Analysis</div>',
        unsafe_allow_html=True
    )

    result_col, chart_col = st.columns([1, 1])

    # --------------------------------------------------------
    # RESULT CARD
    # --------------------------------------------------------

    with result_col:

        if prediction == 1:

            st.markdown(f"""
            <div class="result-card">

                <h2>🟢 SURVIVED</h2>

                <p>
                    Model predicts a higher survival probability.
                </p>

                <h1 style="color:{colors["success"]};font-size:42px;">
                    {probability * 100:.2f}%
                </h1>

                <p>Predicted survival probability</p>

            </div>
            """, unsafe_allow_html=True)

        else:

            st.markdown(f"""
            <div class="result-card">

                <h2>🔴 DID NOT SURVIVE</h2>

                <p>
                    Model predicts a lower survival probability.
                </p>

                <h1 style="color:{colors["danger"]};font-size:42px;">
                    {probability * 100:.2f}%
                </h1>

                <p>Predicted survival probability</p>

            </div>
            """, unsafe_allow_html=True)

    # --------------------------------------------------------
    # PROBABILITY VISUALIZATION
    # --------------------------------------------------------

    with chart_col:

        st.markdown("### Survival Probability")

        st.progress(
            max(0.0, min(1.0, probability))
        )

        st.write(
            f"Survival: **{probability * 100:.2f}%**"
        )

        st.progress(
            max(0.0, min(1.0, 1 - probability))
        )

        st.write(
            f"Non-survival: **{(1 - probability) * 100:.2f}%**"
        )

        st.markdown(f"""
        <div class="metric-card">

            <div class="metric-label">
                DECISION THRESHOLD
            </div>

            <div class="metric-value">
                {threshold * 100:.0f}%
            </div>

        </div>
        """, unsafe_allow_html=True)

    # --------------------------------------------------------
    # PASSENGER SUMMARY
    # --------------------------------------------------------

    st.markdown("### 👤 Passenger Summary")

    summary1, summary2, summary3 = st.columns(3)

    with summary1:

        st.metric(
            "Passenger Class",
            passenger["Pclass"]
        )

    with summary2:

        st.metric(
            "Age",
            f'{passenger["Age"]:.0f} years'
        )

    with summary3:

        st.metric(
            "Family Size",
            passenger["FamilySize"]
        )

    with st.expander("View complete passenger details"):

        st.json(passenger)

# ============================================================
# 11. FOOTER
# ============================================================

st.markdown("""
<div class="footer">

    <p>
        🚢 Titanic Survival Prediction |
        Machine Learning Project
    </p>

    <p>
        Developed with ❤️ by
        <strong>Anto Sanjay C</strong>
    </p>

    <p>
        Python · Scikit-learn · Pandas · Streamlit
    </p>

    <p>
        Released under the MIT License ·
        © 2026 Anto Sanjay C
    </p>

</div>
""", unsafe_allow_html=True)
