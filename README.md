# Mhalia Nicole P. Paton-og: Streamlit Autobiography and Portfolio App

**Course:** CSIT 349: Applied AI  
**Student Name:** Paton-og, Mhalia Nicole P.  
**Section:** G01  
**Standing:** 4th Year Senior (Graduating)  
**School:** Cebu Institute of Technology - University  
**Institutional Email:** mhalianicole.paton-og@cit.edu  
**Personal Email:** mhalianicole21@gmail.com  
**GitHub:** https://github.com/mhalnicole  

---

## Project Overview
This is an interactive web application built using **Streamlit** and **Python 3.14**, showcasing a personal autobiography, academic milestones, technical skill analytics, and a multi-project machine learning portfolio.

It fully utilizes modern Streamlit components, exceeding the rubric requirements with dynamic controls, interactive simulation models, session state persistence, and responsive UI design.

---

## How to Run Locally

### 1. Prerequisites
Make sure Python is installed on your computer.

### 2. Install Dependencies
Open your Command Prompt or Terminal and run:
```bash
pip install -r requirements.txt
```
*(or run: `pip install streamlit pandas numpy`)*

### 3. Launch the Application
Clone the repository and run the Streamlit app:
```bash
git clone https://github.com/mhalnicole/streamlit-portfolio.git
cd streamlit-portfolio
streamlit run app.py
```
Your browser will automatically open to `http://localhost:8501`.

---

## Streamlit Components and Features Checklist

### Core Components Utilized:
- **Text and Structure:** `st.title`, `st.header`, `st.subheader`, `st.write`, `st.markdown`, `st.caption`
- **Table:** `st.dataframe` with custom column configurations (progress bars, number formatting)
- **Charts:** `st.bar_chart` for skill proficiencies and nutrient impact breakdown
- **Input Controls:**
  - `st.button` (Interactive celebration triggers and milestone actions)
  - `st.slider` (Skill threshold filters, interactive nutrition simulation sliders)
  - `st.select_slider` (5-point feedback rating selector)
  - `st.selectbox` (Portfolio view mode and project filter)
  - `st.checkbox` (Toggle student metrics display)
  - `st.text_input` (Visitor name, email input)
  - `st.text_area` (Feedback and comments message box)
  - `st.multiselect` (Filter skills by category)
- **Layout and Organization:**
  - `st.sidebar` (Student info card, navigation, avatar, social contact links)
  - `st.columns` (Responsive multi-column layouts across all tabs)
- **Extra Features (Rubric: At least 4 extras):**
  1. `st.image`: Profile photograph
  2. `st.tabs`: 5 organized sections (Autobiography, Skills, Course Projects, Regression Simulator, Contact)
  3. `st.metric`: Real-time stat cards with delta trends
  4. `st.form` & `st.form_submit_button`: Structured contact/feedback form
  5. `st.session_state`: Live visitor guestbook message persistence
  6. `st.download_button`: Exportable markdown resume summary
  7. `st.expander`: Collapsible detailed milestone summaries
  8. `st.progress`: Health rating visualization bar
  9. `st.balloons()` & `st.toast()`: Interactive celebratory animations

---

## Featured Course Projects Included
1. **The Shelf Placement Conspiracy (Midterm Project):** Cereal nutrition analysis, K-Means clustering (k=3), PCA, and Multiple Linear Regression (R² = 0.973).
2. **Iris Dataset K-Means Clustering:** Optimal k-evaluation via Elbow Method, botanical alignment (~89%), and centroid evaluation.
3. **Apriori Algorithm Market Basket Analysis:** Association rule mining, Support/Confidence/Lift calculations, and retail shelf strategies.
4. **Interactive Streamlit Web Portfolio:** End-to-end full-stack data app built with Python and Streamlit.

---

## Repository Structure
```text
├── app.py              # Main Streamlit application
├── profile.jpg         # Profile photograph asset
├── requirements.txt    # Project dependencies
└── README.md           # Documentation and run instructions
```

---

## Live Deployment
This application is configured for deployment on **Streamlit Community Cloud**:
- **Repository:** [github.com/mhalnicole/streamlit-portfolio](https://github.com/mhalnicole/streamlit-portfolio)
