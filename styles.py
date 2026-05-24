import streamlit as st


def apply_custom_styles():
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
        }

        .main .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
            max-width: 1200px;
        }

        [data-testid="stSidebar"] {
            background: linear-gradient(180deg, #1a1a2e 0%, #16213e 100%);
        }

        [data-testid="stSidebar"] * {
            color: #e0e0e0 !important;
        }

        [data-testid="stSidebar"] .stSlider > div > div > div {
            color: #4fc3f7 !important;
        }

        [data-testid="stMetric"] {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border-radius: 12px;
            padding: 16px 20px;
            box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
        }

        [data-testid="stMetric"] label {
            color: rgba(255, 255, 255, 0.85) !important;
            font-size: 0.85rem !important;
            font-weight: 500 !important;
        }

        [data-testid="stMetric"] [data-testid="stMetricValue"] {
            color: #ffffff !important;
            font-size: 1.8rem !important;
            font-weight: 700 !important;
        }

        h1 {
            color: #ffffff !important;
            font-weight: 700 !important;
            font-size: 2rem !important;
            letter-spacing: -0.5px;
        }

        h2, h3, [data-testid="stSubheader"] {
            color: #e0e0e0 !important;
            font-weight: 600 !important;
        }

        [data-testid="stDataFrame"] {
            border-radius: 12px;
            overflow: hidden;
            box-shadow: 0 2px 12px rgba(0, 0, 0, 0.08);
        }

        .stBarChart, .stScatterChart {
            border-radius: 12px;
            padding: 8px;
            background: rgba(255, 255, 255, 0.05);
            box-shadow: 0 2px 12px rgba(0, 0, 0, 0.2);
        }

        hr {
            border: none;
            height: 1px;
            background: linear-gradient(90deg, transparent, #667eea44, transparent);
            margin: 1.5rem 0;
        }

        .badge-free {
            background: #00b894;
            color: white;
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 0.8rem;
            font-weight: 600;
        }

        .badge-paid {
            background: #6c5ce7;
            color: white;
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 0.8rem;
            font-weight: 600;
        }

        .project-info {
            background: rgba(102, 126, 234, 0.1);
            border-left: 4px solid #667eea;
            border-radius: 8px;
            padding: 20px;
            margin-top: 1rem;
        }

        .project-info p {
            margin: 0;
            color: #e0e0e0;
            line-height: 1.6;
        }

        [data-testid="stSidebar"] [data-testid="stCaption"] {
            background: rgba(79, 195, 247, 0.15);
            border-radius: 8px;
            padding: 8px 12px;
            text-align: center;
            font-weight: 600;
            color: #4fc3f7 !important;
        }
    </style>
    """, unsafe_allow_html=True)
