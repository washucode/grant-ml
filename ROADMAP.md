
# 🛣️ **Grant ML System – Project Roadmap**

A structured roadmap outlining completed work, current development, and future evolution of the Grant Suitability Prediction System.

---

# ✅ **WHAT HAS BEEN COMPLETED SO FAR**

This section documents all the progress already achieved in the project.

### ✔️ **1. Project Setup & Environment**

* Created full project folder structure (`data/`, `src/`, `notebooks/`, `models/`)
* Set up Python environment with required ML + NLP packages
* Installed NLTK stopwords and TF-IDF dependencies
* Successfully tested pipelines inside Jupyter

### ✔️ **2. Preprocessing Pipeline (Full MVP Version)**

All major preprocessing components have been developed and tested:

#### **A. Numeric Cleaner**

* Removes currency symbols (KES, $, £, etc.)
* Converts text numbers to floats
* Handles NaN values
* Cleans comma/percent formatting

#### **B. Financial Ratio Engine**

Implemented 5 domain-specific ratios:

* Grant absorption
* Financial dependency
* Budget leverage
* Liquidity
* Organizational stability

Includes safe division with epsilon (prevents divide-by-zero).

#### **C. Text Cleaner**

* Lowercasing
* Regex punctuation removal
* Stopword removal
* Tokenization
* Cleaned multi-field text support

#### **D. DataFrameWrapper**

* Ensures ColumnTransformer pipelines receive clean DataFrames
* Fixed alignment/shape errors
* Achieved consistent row-wise processing

#### **E. Combined Preprocessor**

* Integrated numeric pipeline, ratio pipeline, and text pipeline
* Added TF-IDF vectorizer with 5000 max features
* Pipeline outputs a unified feature matrix
* Visualized successfully in Jupyter

### ✔️ **3. Synthetic Balanced Training Dataset**

* Designed and generated realistic synthetic NGO applicant data
* Balanced across Low/Medium/High suitability
* Includes numeric + ratio-ready fields + narrative text

### ✔️ **4. Model Training Pipeline**

* Implemented `train.py`
* Loads dataset
* Splits train/test sets
* Fitted Logistic Regression classifier
* Saved model to disk
* Printed evaluation metrics

### ✔️ **5. Prediction Pipeline**

* Implemented `predict.py`
* Accepts dictionary input
* Runs full preprocessing
* Generates suitability class + probabilities
* Produces human-readable output

### ✔️ **6. Documentation**

* Full README.md included
* Methods section written
* System architecture diagram created
* Ratio explanation added
* Model choice section included

### ✔️ **7. Jupyter Testing**

* Tested preprocessing modules individually
* Debugged DataFrameWrapper
* Fixed text + numeric dimension mismatches
* Verified transformed output
* Ensured full pipeline compatibility

---

# 🎯 **VISION**

To develop a transparent, interpretable, and scalable machine learning system capable of evaluating grant applicants using combined numeric, financial ratio, and narrative document features—ultimately supporting real-time decision-making for grantmakers and development programs.

---

# 🧩 **PHASE 1 – MVP Development (Current)**

**Goal:** Build a fully functional prediction engine and front-end prototype.

### ✔️ Deliverables Done

* Full preprocessing pipeline
* Numeric cleaner
* Ratio generator
* Text cleaner
* Combined multistage ColumnTransformer
* Logistic Regression classifier
* Balanced training dataset
* Prediction script
* Debugged Jupyter test notebooks
* Documentation (README + methods)

### 🔧 What Remains in Phase 1

* Build the front-end UI (Streamlit or React)
* Connect front-end to prediction engine

### Status

🟢 **Active**

---

# 🧠 **PHASE 2 – Explainability + API Layer (Near-Term)**

**Goal:** Provide interpretability and allow other systems to connect to the model.

## 2A. SHAP Explainability

* Global explanation
* Local instance-level explanation
* TF-IDF explanation adapters
* Visualizations integrated into UI

## 2B. API Development (FastAPI)

Endpoints needed:

* `/predict`
* `/explain`
* `/predict-multi`
* `/health`

## 2C. Deployment Preparation

* Dockerfile
* Uvicorn/Gunicorn config
* Local Docker deployment

### Status

🟡 **Next Step**

---

# 🚀 **PHASE 3 – Transformer NLP Upgrade (Future)**

Goal: Improve narrative understanding using modern NLP models.

### Candidate Models

* Sentence-BERT
* DistilBERT
* BERT-base
* Longformer (for long proposals)

### Requirements

* Larger dataset
* More compute resources
* Additional labeling

### Status

🔵 **Future**

---

# 📁 **PHASE 4 – Multi-Document Processing (Advanced)**

Goal: Handle the full grant application packet.

### Documents to Process

* Proposal narrative
* Budget
* Workplan
* CVs
* Organizational profile
* Monitoring frameworks

### Multidoc Pipeline

* OCR
* Text extraction
* Embedding per document
* Cross-document attention
* Fusion model

### Status

🔵 **Long-Term**

---

# 🌐 **PHASE 5 – Full Application Deployment (Optional)**

Full-scale application for field or donor use.

### Components

* Front-end (React/Streamlit Pro)
* Backend API
* Authentication
* Monitoring dashboard
* Batch predictions
* Cloud deployment

### Status

🔵 **Later**

---

# 🎓 **PHASE 6 – Research & Academic Contribution**

* Benchmark model
* SHAP analysis
* Comparison vs human evaluators
* Applied AI in governance
* Cambridge or NeurIPS workshop submission

---

# 📊 **Timeline Summary**

| Phase                    | Duration   | Status        |
| ------------------------ | ---------- | ------------- |
| Phase 1 – MVP            | 1–2 weeks  | 🟢 Active     |
| Phase 2 – SHAP + API     | 2–4 weeks  | 🟡 Next       |
| Phase 3 – Transformers   | 1–3 months | 🔵 Future     |
| Phase 4 – Multi-document | 3–6 months | 🔵 Future     |
| Phase 5 – Deployment     | Optional   | 🔵 Future     |
| Phase 6 – Research       | Ongoing    | 🔵 Continuous |

---

# 🧭 **Immediate To-Do List**

* [ ] Build Streamlit UI
* [ ] Add file upload interface
* [ ] Connect to `predict.py`
* [ ] Build FastAPI backend
* [ ] Implement SHAP explainability
* [ ] Package model in Docker
* [ ] Begin transformer experimentation

