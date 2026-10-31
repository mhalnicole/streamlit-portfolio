import streamlit as st
import pandas as pd
import numpy as np
import os
from datetime import datetime

# -----------------------------------------------------------------------------
# PAGE CONFIGURATION
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Mhalia Nicole Paton-og | Portfolio",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------------------------------------------------------
# SESSION STATE INITIALIZATION (CLEAN EMPTY GUESTBOOK)
# -----------------------------------------------------------------------------
# Clear legacy cached dummy review or likes if present
if "feedback_list" in st.session_state:
    del st.session_state["feedback_list"]

if "project_likes" in st.session_state:
    del st.session_state["project_likes"]

if "portfolio_guestbook" not in st.session_state:
    st.session_state.portfolio_guestbook = []

# -----------------------------------------------------------------------------
# INLINE SVG ICONS (PROFESSIONAL VECTOR ICONS, ZERO EMOJIS, ZERO EM DASHES)
# -----------------------------------------------------------------------------
ICON_GRADUATION = '<svg style="vertical-align:middle;margin-right:6px;" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 10v6M2 10l10-5 10 5-10 5z"/><path d="M6 12v5c3 3 9 3 12 0v-5"/></svg>'
ICON_CODE = '<svg style="vertical-align:middle;margin-right:6px;" width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/></svg>'
ICON_CHART = '<svg style="vertical-align:middle;margin-right:6px;" width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/></svg>'
ICON_MAIL = '<svg style="vertical-align:middle;margin-right:6px;" width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>'
ICON_GITHUB = '<svg style="vertical-align:middle;margin-right:6px;" width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"/></svg>'
ICON_CHECK = '<svg style="vertical-align:middle;margin-right:6px;" width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#10B981" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>'
ICON_LAYERS = '<svg style="vertical-align:middle;margin-right:6px;" width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/><polyline points="2 12 12 17 22 12"/></svg>'
ICON_TERMINAL = '<svg style="vertical-align:middle;margin-right:6px;" width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="4 17 10 11 4 5"/><line x1="12" y1="19" x2="20" y2="19"/></svg>'

# -----------------------------------------------------------------------------
# THEME-ADAPTIVE CSS (CLEAN, PROFESSIONAL, NO EM DASHES)
# -----------------------------------------------------------------------------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

    html, body, [class*="css"], .stMarkdown {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }

    /* Proper top header clearance */
    .block-container {
        padding-top: 4.5rem !important;
        padding-bottom: 3.5rem !important;
        max-width: 1140px !important;
    }

    /* Universal Clean Cards */
    .clean-card {
        background-color: var(--secondary-background-color);
        border: 1px solid rgba(128, 128, 128, 0.2);
        border-radius: 12px;
        padding: 20px 24px;
        margin-bottom: 16px;
        color: var(--text-color);
    }
    .clean-card h3, .clean-card h4 {
        margin-top: 0;
        color: var(--text-color);
        font-weight: 700;
    }
    .clean-card p, .clean-card li {
        color: var(--text-color);
        opacity: 0.92;
        line-height: 1.6;
        font-size: 0.93rem;
    }

    /* Headshot Photo Styling */
    .headshot-wrapper {
        text-align: center;
        max-width: 220px;
        margin: 0 auto;
    }
    .headshot-wrapper img {
        border-radius: 12px !important;
        border: 1px solid rgba(128, 128, 128, 0.25) !important;
        width: 100% !important;
        aspect-ratio: 1 / 1 !important;
        object-fit: cover !important;
        display: block !important;
    }

    /* Status badge */
    .status-badge {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        background-color: rgba(16, 185, 129, 0.12);
        border: 1px solid rgba(16, 185, 129, 0.35);
        color: #10B981 !important;
        font-size: 0.78rem;
        font-weight: 700;
        padding: 4px 12px;
        border-radius: 9999px;
        margin-bottom: 10px;
        letter-spacing: 0.03em;
        text-transform: uppercase;
    }
    .status-dot {
        width: 7px;
        height: 7px;
        background-color: #10B981;
        border-radius: 50%;
        display: inline-block;
    }

    /* Badge Pills */
    .badge-pill {
        display: inline-block;
        background-color: rgba(99, 102, 241, 0.12);
        border: 1px solid rgba(99, 102, 241, 0.3);
        color: #6366F1 !important;
        font-size: 0.8rem;
        font-weight: 600;
        padding: 3px 12px;
        border-radius: 9999px;
        margin-right: 6px;
        margin-bottom: 8px;
    }

    /* Metrics */
    [data-testid="stMetric"] {
        background-color: var(--secondary-background-color) !important;
        border: 1px solid rgba(128, 128, 128, 0.2) !important;
        border-radius: 12px !important;
        padding: 12px 16px !important;
    }

    /* Quote Box */
    .quote-box {
        border-left: 3px solid #6366F1;
        background-color: rgba(99, 102, 241, 0.08);
        padding: 12px 16px;
        border-radius: 0 8px 8px 0;
        font-style: italic;
        color: var(--text-color);
        margin: 12px 0;
        font-size: 0.9rem;
    }

    /* Clean Sidebar & Compact Top Clearance */
    [data-testid="stSidebarContent"] {
        padding-top: 0 !important;
    }
    [data-testid="stSidebarHeader"] {
        padding-top: 0.4rem !important;
        padding-bottom: 0 !important;
        height: 2.2rem !important;
        min-height: 2.2rem !important;
        margin-bottom: 0 !important;
    }
    [data-testid="stSidebarUserContent"] {
        padding-top: 0 !important;
        margin-top: -0.4rem !important;
    }
    [data-testid="stSidebarUserContent"] [data-testid="stVerticalBlock"] > div:first-child {
        margin-top: 0 !important;
        padding-top: 0 !important;
    }
    section[data-testid="stSidebar"] div.block-container {
        padding-top: 0.5rem !important;
    }
    .sidebar-brand {
        padding: 0 0 10px 0;
        border-bottom: 1px solid rgba(128, 128, 128, 0.2);
        margin-bottom: 12px;
        margin-top: 0 !important;
    }
    .sidebar-brand h3 {
        margin-top: 0 !important;
        margin-bottom: 4px !important;
        font-size: 1.25rem !important;
        line-height: 1.25 !important;
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# SIDEBAR
# -----------------------------------------------------------------------------
with st.sidebar:
    st.markdown(f"""
    <div class="sidebar-brand">
        <h3 style="margin-top: 0; margin-bottom: 4px;">Mhalia Nicole Paton-og</h3>
        <p style="opacity: 0.8; font-size: 0.88rem; margin-bottom: 6px;">
            {ICON_GRADUATION} 4th Year Senior (BSIT)<br>
            Cebu Institute of Technology - University
        </p>
        <span style="background: #4F46E5; color: #FFF; font-size: 0.74rem; font-weight: 700; padding: 2px 8px; border-radius: 6px;">SECTION G01</span>
    </div>
    """, unsafe_allow_html=True)

    with st.expander("Academic Credentials", expanded=True):
        st.markdown("""
        **Program:** BS Information Technology  
        **Standing:** 4th Year Senior (Graduating)  
        **School:** Cebu Institute of Technology - University  
        **Course:** CSIT 349: Applied AI  
        **Section:** G01  
        """)

    st.markdown(f"#### {ICON_LAYERS} Quick Links", unsafe_allow_html=True)
    resume_summary = """# MHALIA NICOLE P. PATON-OG
Program: BS Information Technology | 4th Year Senior (Graduating)
University: Cebu Institute of Technology - University (CIT-U)
Section: G01 | Course: CSIT 349: Applied AI (SY 2025-2026)

## CONTACT
Institutional Email: mhalianicole.paton-og@cit.edu
Personal Email: mhalianicole21@gmail.com
GitHub: https://github.com/mhalnicole

## PROFESSIONAL PROFILE
4th Year Information Technology student with hands-on expertise in Applied AI,
data science workflows, unsupervised clustering, multivariate regression, and interactive web tools.

## CORE SKILLS
- Languages: Python, SQL, HTML/CSS, JavaScript Basics
- Machine Learning & Analytics: Pandas, NumPy, Scikit-Learn, Matplotlib, Seaborn, Altair
- Frameworks & Tools: Streamlit, Jupyter Notebooks, Git/GitHub

## FEATURED COURSE PROJECTS
1. The Shelf Placement Conspiracy (Midterm Project: Cereal Dataset, R² = 0.973)
2. Iris Dataset K-Means Clustering & Dimensionality Analysis
3. Apriori Association Rule Mining for Supermarket Market Basket Analysis
4. Streamlit Interactive Portfolio & Web App
"""
    st.download_button(
        label="Download Résumé (.md)",
        data=resume_summary,
        file_name="Paton-og_Mhalia_Resume.md",
        mime="text/markdown",
        icon=":material/download:",
        use_container_width=True
    )
    
    st.markdown(f"""
    <div style="margin-top: 8px;">
        <a href="https://github.com/mhalnicole" target="_blank" style="text-decoration:none;">
            <div style="background-color: var(--secondary-background-color); border:1px solid rgba(128,128,128,0.25); padding:8px; border-radius:8px; text-align:center; color: var(--text-color); font-weight:600; font-size:0.85rem;">
                {ICON_GITHUB} GitHub Profile
            </div>
        </a>
    </div>
    <div style="margin-top: 8px;">
        <a href="https://mail.google.com/mail/?view=cm&fs=1&to=mhalianicole21@gmail.com" target="_blank" style="text-decoration:none;">
            <div style="background-color: var(--secondary-background-color); border:1px solid rgba(128,128,128,0.25); padding:8px; border-radius:8px; text-align:center; color: var(--text-color); font-weight:600; font-size:0.85rem;">
                {ICON_MAIL} Personal Gmail (Web)
            </div>
        </a>
    </div>
    <div style="margin-top: 8px;">
        <a href="https://mail.google.com/mail/?view=cm&fs=1&to=mhalianicole.paton-og@cit.edu" target="_blank" style="text-decoration:none;">
            <div style="background-color: var(--secondary-background-color); border:1px solid rgba(128,128,128,0.25); padding:8px; border-radius:8px; text-align:center; color: var(--text-color); font-weight:600; font-size:0.85rem;">
                {ICON_MAIL} Institutional Email
            </div>
        </a>
    </div>
    """, unsafe_allow_html=True)

    st.divider()
    show_fun_stats = st.checkbox("Show Student Metrics", value=True)

# -----------------------------------------------------------------------------
# HERO SECTION
# -----------------------------------------------------------------------------
script_dir = os.path.dirname(__file__)
user_photo_path = os.path.join(script_dir, "profile.jpg")
if not os.path.exists(user_photo_path):
    user_photo_path = os.path.join(script_dir, "Mhalia Paton-og.jpg")

col_hero_text, col_hero_img = st.columns([2.4, 1], gap="medium")

with col_hero_text:
    st.markdown("""
    <div class="status-badge">
        <span class="status-dot"></span> Graduating Senior | Class of 2026 | CIT-U
    </div>
    """, unsafe_allow_html=True)
    
    st.title("Mhalia Nicole P. Paton-og")
    st.subheader("BS Information Technology | Applied AI & Machine Learning")
    
    st.markdown("""
    Welcome to my academic portfolio. As a graduating 4th-year senior in Information Technology at 
    **Cebu Institute of Technology - University**, I combine statistical modeling and machine learning 
    with responsive web development to create user-centered data solutions.
    """)
    
    st.markdown("""
    <span class="badge-pill">Python 3.14</span>
    <span class="badge-pill">Scikit-Learn</span>
    <span class="badge-pill">Streamlit</span>
    <span class="badge-pill">Pandas & NumPy</span>
    <span class="badge-pill">Linear Regression</span>
    <span class="badge-pill">K-Means & PCA</span>
    """, unsafe_allow_html=True)
    
    st.write("")
    btn1, btn2, btn3 = st.columns([1, 1, 1.4])
    with btn1:
        if st.button("Celebrate", icon=":material/celebration:", use_container_width=True):
            st.balloons()
            st.toast("Thank you for visiting my portfolio.")
    with btn2:
        st.link_button("GitHub", "https://github.com/mhalnicole", icon=":material/code:", use_container_width=True)
    with btn3:
        st.link_button("Email Gmail", "https://mail.google.com/mail/?view=cm&fs=1&to=mhalianicole21@gmail.com", icon=":material/mail:", use_container_width=True)

with col_hero_img:
    if os.path.exists(user_photo_path):
        st.markdown('<div class="headshot-wrapper">', unsafe_allow_html=True)
        st.image(user_photo_path, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
        st.caption("<div style='text-align: center; margin-top: 4px;'><b>Paton-og, Mhalia Nicole P.</b><br>CSIT 349 | Section G01</div>", unsafe_allow_html=True)
    else:
        st.info("Mhalia Paton-og Portrait")

# -----------------------------------------------------------------------------
# METRICS ROW (CONCISE VALUES TO PREVENT ANY TRUNCATION AT 100% ZOOM)
# -----------------------------------------------------------------------------
st.write("")
m1, m2, m3, m4 = st.columns(4)
with m1:
    st.metric(label="Academic Status", value="4th Year", delta="Graduating Senior")
with m2:
    st.metric(label="Course Projects", value="4", delta="Completed & Live")
with m3:
    st.metric(label="Model Fit", value="0.973 R²", delta="Linear Regression")
with m4:
    st.metric(label="Primary Stack", value="Python", delta="Streamlit & Sklearn")

if show_fun_stats:
    st.write("")
    f1, f2, f3 = st.columns(3)
    with f1:
        st.caption("Estimated coffee consumed during college: **380+ cups**")
    with f2:
        st.caption("Code cells executed across notebooks: **1,600+ runs**")
    with f3:
        st.caption("Outliers investigated & imputed: **45+ records**")

st.divider()

# -----------------------------------------------------------------------------
# MAIN APP TABS
# -----------------------------------------------------------------------------
tab_bio, tab_skills, tab_projects, tab_lab, tab_contact = st.tabs([
    "Autobiography",
    "Skills & Analytics",
    "Course Projects",
    "Regression Simulator",
    "Contact & Guestbook"
])

# =============================================================================
# TAB 1: AUTOBIOGRAPHY
# =============================================================================
with tab_bio:
    col_b_main, col_b_side = st.columns([1.8, 1], gap="medium")
    
    with col_b_main:
        st.markdown(f"""
        <div class="clean-card">
            <h4>{ICON_GRADUATION} My Story & Academic Journey</h4>
            <p>
                Hello! I am <b>Mhalia Nicole P. Paton-og</b>, a graduating 4th-year <b>BS Information Technology</b> student 
                at <b>Cebu Institute of Technology - University (CIT-U)</b>, enrolled in <b>CSIT 349 (Applied AI)</b> 
                under section <b>G01</b>.
            </p>
            <p>
                Throughout my 4 years in Information Technology, I've discovered that data is far more than abstract numbers: it 
                tells stories about how people behave, how products are placed, and how software can support smarter everyday decisions. 
                What started with writing basic programming logic has grown into hands-on data preprocessing, unsupervised clustering, 
                multivariate regression, and interactive web dashboard development.
            </p>
            <div class="quote-box">
                "Learning technology is not just about memorizing syntax; it's about solving real human challenges through logic and creative design."
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div class="clean-card">
            <h4>{ICON_LAYERS} Academic Pillars at CIT University</h4>
            <ul>
                <li><b>Analytical Problem Solving:</b> Translating operational challenges into clear algorithmic steps.</li>
                <li><b>Data Preprocessing & Cleansing:</b> Addressing missing data with median imputation and feature standardization.</li>
                <li><b>Applied Machine Learning:</b> Implementing unsupervised models (K-Means, PCA) and supervised models (Multiple Linear Regression).</li>
                <li><b>Interactive UI Delivery:</b> Designing responsive dashboards using Streamlit to present findings clearly.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with col_b_side:
        st.markdown(f"""
        <div class="clean-card" style="border-left: 3px solid #6366F1;">
            <h4>{ICON_CHECK} Fast Facts</h4>
            <p><b>Name:</b> Mhalia Nicole P. Paton-og</p>
            <p><b>Standing:</b> 4th Year Senior (Graduating)</p>
            <p><b>Degree:</b> BS Information Technology</p>
            <p><b>University:</b> CIT - University</p>
            <p><b>Course:</b> CSIT 349 (Applied AI)</p>
            <p><b>Section:</b> G01</p>
            <p><b>Favorite Model:</b> Multiple Linear Regression</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("##### Academic Milestones")
        milestones = [
            ("Year 1 (2022-2023)", "Mastered foundational computing logic and algorithms at CIT-U."),
            ("Year 2 (2023-2024)", "Deepened expertise in OOP, data structures, and relational databases."),
            ("Year 3 (2024-2025)", "Dove into Python analytics, exploratory data analysis, and software design."),
            ("Year 4 (2025-2026)", "Mastered Applied AI: K-Means clustering, PCA, regression, and Streamlit apps."),
            ("Upcoming 2026", "Graduating with BSIT and launching an industry career in data & tech.")
        ]
        
        for period, desc in milestones:
            with st.expander(period):
                st.write(desc)

# =============================================================================
# TAB 2: SKILLS & ANALYTICS
# =============================================================================
with tab_skills:
    st.markdown(f"### {ICON_CHART} Technical Competency & Analytics", unsafe_allow_html=True)
    st.write("A quantitative breakdown of technical proficiencies developed across 4 years of IT education.")
    
    skills_data = pd.DataFrame({
        "Skill": [
            "Python Programming", 
            "Pandas & Data Cleaning", 
            "Scikit-Learn (ML Models)", 
            "Streamlit App Dev", 
            "Data Visualization", 
            "SQL & Databases", 
            "Git & Version Control", 
            "UI/UX Design"
        ],
        "Category": [
            "Programming", 
            "Data Science", 
            "Machine Learning", 
            "Web Development", 
            "Visualization", 
            "Database", 
            "Developer Tools", 
            "Design"
        ],
        "Proficiency": [94, 91, 87, 90, 88, 82, 84, 86],
        "Experience_Yrs": [3.5, 3.0, 2.0, 1.5, 2.5, 2.5, 2.0, 3.0]
    })
    
    col_ctrl1, col_ctrl2 = st.columns([2, 1])
    with col_ctrl1:
        min_prof = st.slider(
            "Filter skills by minimum proficiency level (%):",
            min_value=50, max_value=95, value=75, step=5
        )
    with col_ctrl2:
        selected_cats = st.multiselect(
            "Filter categories:",
            options=skills_data["Category"].unique().tolist(),
            default=skills_data["Category"].unique().tolist()
        )
        
    filtered_skills = skills_data[
        (skills_data["Proficiency"] >= min_prof) & 
        (skills_data["Category"].isin(selected_cats))
    ]
    
    col_s_chart, col_s_table = st.columns([1.6, 1], gap="medium")
    
    with col_s_chart:
        st.markdown("##### Skill Proficiency Overview")
        if not filtered_skills.empty:
            chart_df = filtered_skills.set_index("Skill")[["Proficiency"]]
            st.bar_chart(chart_df, color="#6366F1")
        else:
            st.warning("No skills match your current filter.")
            
    with col_s_table:
        st.markdown("##### Detailed Competency Table")
        st.dataframe(
            filtered_skills,
            column_config={
                "Proficiency": st.column_config.ProgressColumn(
                    "Self-Rating",
                    format="%d%%",
                    min_value=0,
                    max_value=100
                ),
                "Experience_Yrs": st.column_config.NumberColumn(
                    "Experience",
                    format="%.1f yrs"
                )
            },
            hide_index=True,
            use_container_width=True
        )

# =============================================================================
# TAB 3: COURSE PROJECTS
# =============================================================================
with tab_projects:
    st.markdown(f"### {ICON_CODE} Featured Course Projects", unsafe_allow_html=True)
    
    proj_type = st.selectbox(
        "Filter projects by track:",
        ["All Projects", "Machine Learning & Clustering", "Supervised Regression", "Interactive Web Apps"]
    )
    
    # Project 1: Cereal Shelf Placement Conspiracy
    if proj_type in ["All Projects", "Machine Learning & Clustering", "Supervised Regression"]:
        st.markdown(f"""
        <div class="clean-card">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
                <h3 style="margin:0;">The Shelf Placement Conspiracy (Midterm Project)</h3>
                <span class="badge-pill" style="color: #10B981 !important; border-color: #10B981;">FEATURED PROJECT</span>
            </div>
            <p style="opacity: 0.8; margin-bottom:12px; font-size:0.88rem;">
                <b>Course:</b> CSIT 349: Applied AI | <b>Partner:</b> Louise Daniella Quizana | <b>Role:</b> Data Analyst & Regression Lead
            </p>
            <div style="margin-bottom:12px;">
                <span class="badge-pill">Python</span>
                <span class="badge-pill">Pandas</span>
                <span class="badge-pill">Scikit-Learn</span>
                <span class="badge-pill">K-Means</span>
                <span class="badge-pill">Multiple Linear Regression</span>
                <span class="badge-pill">PCA</span>
            </div>
            <p>
                • <b>Market Placement Trick:</b> Discovered that cereals placed on <b>Shelf 2</b> (kid eye-level) average <b>9.62g of sugar</b> (nearly double Shelf 1 at 5.2g), confirming retail placement psychology.<br>
                • <b>Predictive Model:</b> Multiple Linear Regression achieved an exceptional <b>R² = 0.973</b>. Dietary fiber adds <b>+2.87 pts/g</b>, while fat (<b>-3.47</b>) and sugars (<b>-1.99</b>) heavily penalize rating.<br>
                • <b>Market Archetypes:</b> Segmented cereals into 3 distinct clusters: <i>Kid Sugar Bombs</i>, <i>Standard Grain Flakes</i>, and <i>High-Fiber Champions</i>.
            </p>
        </div>
        """, unsafe_allow_html=True)

    # Project 2: Iris Flower Clustering
    if proj_type in ["All Projects", "Machine Learning & Clustering"]:
        st.markdown(f"""
        <div class="clean-card">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
                <h3 style="margin:0;">Iris Flower K-Means Clustering & Boundary Analysis</h3>
                <span class="badge-pill">PAIRED ACTIVITY</span>
            </div>
            <p style="opacity: 0.8; margin-bottom:12px; font-size:0.88rem;">
                <b>Course:</b> CSIT 349: Applied AI | <b>Role:</b> Algorithm Evaluator & Student Report Author
            </p>
            <div style="margin-bottom:12px;">
                <span class="badge-pill">Python</span>
                <span class="badge-pill">NumPy</span>
                <span class="badge-pill">Matplotlib</span>
                <span class="badge-pill">Elbow Method</span>
                <span class="badge-pill">K-Means</span>
            </div>
            <p>
                • Tested unsupervised clustering on Fisher's Iris dataset across 4 botanical dimensions.<br>
                • Evaluated inertia drop to mathematically justify <b>k = 3</b> at the elbow bend.<br>
                • Achieved 100% clean isolation for <i>Iris setosa</i>, and documented natural boundary overlap for <i>versicolor</i> and <i>virginica</i> (~89% alignment).
            </p>
        </div>
        """, unsafe_allow_html=True)

    # Project 3: Apriori Association Rules
    if proj_type in ["All Projects", "Machine Learning & Clustering"]:
        st.markdown(f"""
        <div class="clean-card">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
                <h3 style="margin:0;">Apriori Market Basket Association Mining</h3>
                <span class="badge-pill">PAIRED ACTIVITY</span>
            </div>
            <p style="opacity: 0.8; margin-bottom:12px; font-size:0.88rem;">
                <b>Course:</b> CSIT 349: Applied AI | <b>Role:</b> Mathematical Pruning & Rule Evaluation
            </p>
            <div style="margin-bottom:12px;">
                <span class="badge-pill">Python</span>
                <span class="badge-pill">Pandas</span>
                <span class="badge-pill">Apriori Algorithm</span>
                <span class="badge-pill">Support & Confidence</span>
                <span class="badge-pill">Lift Metric</span>
            </div>
            <p>
                • Executed full candidate itemset generation across k=1, k=2, and k=3 iterations using the downward-closure property.<br>
                • Mined frequent purchasing rules with lift exceeding <b>1.85x</b>, formulating actionable retail shelf placement recommendations.
            </p>
        </div>
        """, unsafe_allow_html=True)

    # Project 4: Streamlit Interactive Portfolio
    if proj_type in ["All Projects", "Interactive Web Apps"]:
        st.markdown(f"""
        <div class="clean-card">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
                <h3 style="margin:0;">Streamlit Autobiography & AI Interactive App</h3>
                <span class="badge-pill" style="color: #6366F1 !important; border-color: #6366F1;">CURRENT APP</span>
            </div>
            <p style="opacity: 0.8; margin-bottom:12px; font-size:0.88rem;">
                <b>Course:</b> CSIT 349: Applied AI | <b>Role:</b> Sole Designer & Full-Stack Developer
            </p>
            <div style="margin-bottom:12px;">
                <span class="badge-pill">Python 3.14</span>
                <span class="badge-pill">Streamlit</span>
                <span class="badge-pill">Pandas</span>
                <span class="badge-pill">Altair</span>
                <span class="badge-pill">CSS Injection</span>
                <span class="badge-pill">Session State</span>
            </div>
            <p>
                • Built a modern interactive web app featuring multi-component navigation, dynamic charts, live regression simulator, and session state guestbook.<br>
                • Fully packaged for Streamlit Community Cloud deployment.
            </p>
        </div>
        """, unsafe_allow_html=True)

# =============================================================================
# TAB 4: REGRESSION SIMULATOR
# =============================================================================
with tab_lab:
    st.markdown(f"### {ICON_TERMINAL} Regression Simulator: Cereal Health Score", unsafe_allow_html=True)
    st.write(
        "Test the real linear regression formula derived from our Midterm Project. "
        "Adjust nutritional values per serving to see how the predicted consumer rating changes dynamically."
    )
    
    sim_c1, sim_c2 = st.columns(2, gap="medium")
    
    with sim_c1:
        st.markdown("""
        <div class="clean-card">
            <h4>Nutritional Input (per serving):</h4>
        """, unsafe_allow_html=True)
        in_sugars = st.slider("Sugars (grams):", 0.0, 16.0, 6.0, 0.5)
        in_fiber = st.slider("Dietary Fiber (grams):", 0.0, 14.0, 3.0, 0.5)
        in_fat = st.slider("Fat (grams):", 0.0, 6.0, 1.0, 0.5)
        in_sodium = st.slider("Sodium (milligrams):", 0, 320, 160, 10)
        in_calories = st.slider("Calories (kcal):", 50, 160, 110, 5)
        st.markdown('</div>', unsafe_allow_html=True)
        
    with sim_c2:
        st.markdown("""
        <div class="clean-card">
            <h4>Live Regression Output</h4>
        """, unsafe_allow_html=True)
        
        baseline = 54.0
        predicted = (
            baseline + 
            (in_fiber * 2.87) - 
            (in_sugars * 1.99) - 
            (in_fat * 3.47) - 
            (in_sodium * 0.057) + 
            (in_calories * 0.02)
        )
        predicted = max(15.0, min(95.0, predicted))
        
        st.metric(
            label="Predicted Health Rating",
            value=f"{predicted:.1f} / 100",
            delta=f"{(predicted - 50.0):+.1f} vs Avg (50.0)"
        )
        
        st.progress(int(predicted))
        
        if predicted >= 60.0:
            st.success("Classification: Health Champion (High fiber and low sugar)")
        elif predicted >= 40.0:
            st.info("Classification: Standard Grain Flake (Balanced profile)")
        else:
            st.error("Classification: Sugar Bomb Warning (High sugar or fat penalty)")
            
        st.markdown("###### Point Contribution Breakdown:")
        impact_df = pd.DataFrame({
            "Nutrient": ["Fiber (+)", "Calories (+)", "Sugars (-)", "Fat (-)", "Sodium (-)"],
            "Point Impact": [
                in_fiber * 2.87,
                in_calories * 0.02,
                -(in_sugars * 1.99),
                -(in_fat * 3.47),
                -(in_sodium * 0.057)
            ]
        })
        st.bar_chart(impact_df.set_index("Nutrient"), color="#6366F1")
        st.markdown('</div>', unsafe_allow_html=True)

# =============================================================================
# TAB 5: CONTACT & GUESTBOOK
# =============================================================================
with tab_contact:
    st.markdown(f"### {ICON_MAIL} Contact & Guestbook", unsafe_allow_html=True)
    
    col_form_left, col_form_right = st.columns([1.6, 1], gap="medium")
    
    with col_form_left:
        with st.form("guestbook_form", clear_on_submit=True):
            st.markdown("##### Send a Message / Review")
            v_name = st.text_input("Your Name / Professor / Reviewer:", placeholder="e.g. Evaluator")
            v_email = st.text_input("Your Email Address:", placeholder="e.g. evaluator@cit.edu")
            v_cat = st.selectbox(
                "Feedback Category:",
                ["Course Project Evaluation", "Code Review / Feedback", "Collaboration Request", "General Greeting"]
            )
            v_rating = st.select_slider(
                "Rate this Streamlit Portfolio App (1 to 5):",
                options=[1, 2, 3, 4, 5],
                value=5,
                format_func=lambda x: f"{x} / 5"
            )
            v_comment = st.text_area(
                "Comments or Feedback:",
                placeholder="Share your thoughts on the design, layout, or components..."
            )
            
            submitted = st.form_submit_button("Submit Feedback", icon=":material/send:", use_container_width=True)
            
            if submitted:
                if v_name.strip() and v_comment.strip():
                    new_item = {
                        "name": v_name.strip(),
                        "date": datetime.now().strftime("%Y-%m-%d"),
                        "rating": v_rating,
                        "category": v_cat,
                        "comment": v_comment.strip()
                    }
                    st.session_state.portfolio_guestbook.append(new_item)
                    st.balloons()
                    st.success(f"Thank you, {v_name}! Your message has been saved.")
                else:
                    st.error("Please provide both your name and a comment before submitting.")
                    
    with col_form_right:
        st.markdown("##### Recent Guestbook Entries")
        if not st.session_state.portfolio_guestbook:
            st.info("No guestbook entries yet. Submit feedback to add a review.")
        else:
            for msg in reversed(st.session_state.portfolio_guestbook):
                st.markdown(f"""
                <div class="clean-card" style="padding: 14px 18px; margin-bottom: 12px;">
                    <div style="display:flex; justify-content:space-between; margin-bottom:4px;">
                        <b>{msg['name']}</b>
                        <span>Rating: {msg['rating']} / 5</span>
                    </div>
                    <small style="opacity:0.75;">{msg.get('category', 'Feedback')} • {msg['date']}</small>
                    <p style="margin-top:6px; margin-bottom:0; font-size:0.88rem;"><i>"{msg['comment']}"</i></p>
                </div>
                """, unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# FOOTER
# -----------------------------------------------------------------------------
st.write("")
st.divider()
foot_1, foot_2 = st.columns([3, 1])
with foot_1:
    st.caption("Crafted with Streamlit & Python 3.14 | CSIT 349: Applied AI")
    st.caption("© 2026 **Paton-og, Mhalia Nicole P.** | **Section G01** | Cebu Institute of Technology - University")
with foot_2:
    if st.button("Celebrate Milestone", icon=":material/celebration:", use_container_width=True):
        st.balloons()
