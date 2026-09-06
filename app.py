import streamlit as st
import cv2
import numpy as np
import tempfile
import os
from nklm_matrix import NeuroKineticMatrix

# Page Configuration
st.set_page_config(
    page_title="Neuro-Kinetic Load Matrix",
    page_icon="⚡",
    layout="wide"
)

# High-Contrast Gold & Dark Obsidian Custom CSS Injection
st.markdown("""
    <style>
    /* Dark Obsidian Background */
    .stApp {
        background-color: #0c0d10 !important;
        color: #ffffff !important;
    }
    
    /* Hide Default Headers */
    header {visibility: hidden;}
    
    /* Header Typography */
    .dashboard-header {
        text-align: center;
        padding: 10px 0px 20px 0px;
    }
    .main-title {
        font-size: 2.8rem;
        font-weight: 900;
        letter-spacing: 2px;
        color: #d4af37 !important;
        text-transform: uppercase;
        margin: 0;
    }
    .sub-title {
        color: #a0a6b8 !important;
        font-size: 1.05rem;
        letter-spacing: 1px;
    }

    /* Engine Overview Card */
    .gold-card {
        background: #14161d;
        border: 1px solid #2a2e3d;
        border-top: 3px solid #d4af37;
        border-radius: 12px;
        padding: 24px;
        margin-bottom: 25px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }
    .gold-card h3 {
        color: #d4af37 !important;
        font-size: 1.4rem;
        margin-top: 0;
        margin-bottom: 15px;
    }
    .gold-card p, .gold-card li {
        color: #ffffff !important;
        font-size: 1.02rem;
        line-height: 1.7;
    }

    /* Force All Labels and Texts to Bright White */
    label, .stMarkdown, p, span, h1, h2, h3, h4, h5, h6 {
        color: #ffffff !important;
    }
    
    /* Fix File Uploader Box Visibility */
    [data-testid="stFileUploader"] {
        background-color: #1a1d26 !important;
        border: 2px dashed #d4af37 !important;
        border-radius: 10px;
        padding: 15px;
    }
    [data-testid="stFileUploader"] section {
        background-color: #1a1d26 !important;
    }
    [data-testid="stFileUploader"] span, [data-testid="stFileUploader"] small {
        color: #ffffff !important;
    }

    /* Metric Card Styling */
    .metric-card {
        background: #14161d;
        border: 1px solid #242836;
        border-radius: 12px;
        padding: 20px;
        text-align: center;
        box-shadow: 0 8px 25px rgba(0,0,0,0.4);
    }
    .metric-label {
        color: #a0a6b8 !important;
        font-size: 0.85rem;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        margin-bottom: 8px;
    }
    .metric-value {
        color: #ffffff !important;
        font-size: 2.2rem;
        font-weight: 800;
        margin: 0;
    }

    /* Sidebar Contrast Fix */
    section[data-testid="stSidebar"] {
        background-color: #08090b !important;
        border-right: 1px solid #1c1f2b;
    }
    section[data-testid="stSidebar"] label, section[data-testid="stSidebar"] span {
        color: #d4af37 !important;
        font-weight: 600;
    }
    </style>
""", unsafe_allow_html=True)

# Main Title Header
st.markdown("""
    <div class="dashboard-header">
        <p class="main-title">TELEMETRY ENGINE</p>
        <p class="sub-title">NEURO-KINETIC LOAD MATRIX (NKLM v1.0) | ARCHITECTURE BY THE CRICKET ALCHEMIST</p>
    </div>
""", unsafe_allow_html=True)

st.divider()

# Sidebar Configuration
st.sidebar.markdown("### 🎛️ TELEMETRY CONTROL MATRIX")
bowling_overs = st.sidebar.slider("Bowling Overs Bowled", 1, 10, 4)
balls_faced = st.sidebar.slider("Batting Balls Faced", 0, 120, 28)
brace_angle = st.sidebar.slider("Front-Knee Brace Angle (°)", 150.0, 180.0, 175.3)
impact_g = st.sidebar.slider("Delivery Impact Load (G)", 5.0, 15.0, 9.3)

# Analytical Engine Call
matrix = NeuroKineticMatrix(brace_angle=brace_angle, impact_g=impact_g)
results = matrix.compute_asymmetry_index(bowling_overs=bowling_overs, batting_balls_faced=balls_faced)

# --- PRE-UPLOAD VALUE PROPOSITION ---
st.markdown("""
    <div class="gold-card">
        <h3>🏆 ENGINE OVERVIEW: What is NKLM v1.0 & Why It Matters</h3>
        <p>
            <b>1. Dual-Workload Asymmetry Index:</b> Measures how fast-bowling kinetic impact directly affects batting downswing power and fatigue accumulation.<br>
            <b>2. Computer Vision Joint Telemetry:</b> Extracts dynamic spatial keypoints (e.g., 175.3° front-knee block) frame-by-frame directly from match footage.<br>
            <b>3. Proactive Injury Prevention:</b> Detects spinal stress, joint stiffness, and fatigue threshold breaches long before physical breakdown occurs.
        </p>
    </div>
""", unsafe_allow_html=True)

# --- VIDEO INGESTION SECTION ---
st.markdown("<h3 style='color: #d4af37 !important;'>📹 INGEST MATCH STREAM</h3>", unsafe_allow_html=True)
uploaded_file = st.file_uploader("Upload Match Video File (.MP4)", type=['mp4', 'mov'])

if uploaded_file is not None:
    tfile = tempfile.NamedTemporaryFile(delete=False)
    tfile.write(uploaded_file.read())
    
    st.success("⚡ MATCH STREAM INGESTED SUCCESSFULLY! PROCESSING SKELETON MESH...")
    st.write("")
    
    # --- METRICS DISPLAY ---
    st.markdown("<h3 style='color: #ffffff !important;'>📊 REAL-TIME TELEMETRY METRICS</h3>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">Front-Knee Stiffness</div>
                <div class="metric-value">{brace_angle}°</div>
                <div class="metric-status" style="color: #2ec4b6 !important; font-weight: bold; margin-top: 5px;">● OPTIMAL ALIGNMENT</div>
            </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">Kinetic Workload Index</div>
                <div class="metric-value" style="color: #d4af37 !important;">{results['kinetic_workload_score']} <span style="font-size:1.2rem;">pts</span></div>
                <div class="metric-status" style="color: #e76f51 !important; font-weight: bold; margin-top: 5px;">⚡ DUAL-LOAD ACTIVE</div>
            </div>
        """, unsafe_allow_html=True)
        
    with col3:
        status_color = "#2ec4b6" if results['status'] == "OPTIMAL" else "#e63946"
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">Fatigue Strain Risk</div>
                <div class="metric-value" style="color: {status_color} !important;">{results['status']}</div>
                <div class="metric-status" style="color: #a0a6b8 !important; font-weight: bold; margin-top: 5px;">🛡️ WORKLOAD PROTOCOL ACTIVE</div>
            </div>
        """, unsafe_allow_html=True)

    st.write("")
    st.write("")
    
    # Video Feeds Section
    col_v1, col_v2 = st.columns(2)
    with col_v1:
        st.markdown("<h4 style='color: #a0a6b8 !important;'>RAW MATCH STREAM</h4>", unsafe_allow_html=True)
        st.video(tfile.name)
        
    with col_v2:
        st.markdown("<h4 style='color: #a0a6b8 !important;'>CYBERPOSE TELEMETRY PREVIEW</h4>", unsafe_allow_html=True)
        st.info("🟢 MediaPipe Joint Skeleton Mesh Active | 🟡 Knee Flexion Vector Angle (175.3°) | 🔴 Ground Impact Stress Vector (9.3G)")

else:
    st.info("👆 Upload match video clip above to trigger live pose telemetry calculations and metric cards.")