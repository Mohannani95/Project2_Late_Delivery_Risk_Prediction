# ============================================================
# APL LOGISTICS — Operations Intelligence Platform
# Premium Enterprise Dashboard
# Author: Mohan | Unified Mentor Internship 2026
# ============================================================

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import joblib
import os

# ============================================================
# PAGE CONFIGURATION
# ============================================================
st.set_page_config(
    page_title="APL Logistics | Operations Intelligence",
    page_icon="📦",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================
# CORPORATE NAVY THEME — Custom CSS
# ============================================================
st.markdown("""
    <style>
    /* Import professional fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Global page background — clean light gray */
    .stApp {
        background-color: #f7f8fa;
        font-family: 'Inter', sans-serif;
    }
    
    /* Hide default Streamlit header */
    header[data-testid="stHeader"] {
        background-color: transparent;
        height: 0px;
    }
    
    .block-container {
        padding-top: 0rem !important;
        padding-bottom: 1rem !important;
        max-width: 100% !important;
    }
    
    /* CORPORATE HEADER BAR */
    .corp-header {
        background: linear-gradient(90deg, #0f2847 0%, #1a3a5c 100%);
        padding: 20px 40px;
        margin: -1rem -2rem 0 -2rem;
        border-bottom: 3px solid #c9a961;
        display: flex;
        justify-content: space-between;
        align-items: center;
        color: white;
    }
    .corp-logo {
        display: flex;
        align-items: center;
        gap: 16px;
    }
    .corp-logo-icon {
        width: 44px;
        height: 44px;
        background: #c9a961;
        border-radius: 6px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 22px;
    }
    .corp-title {
        font-size: 17px;
        font-weight: 600;
        letter-spacing: 0.5px;
        color: white;
        margin: 0;
    }
    .corp-subtitle {
        font-size: 11px;
        color: #c9a961;
        letter-spacing: 2px;
        margin: 0;
    }
    .corp-status {
        display: flex;
        align-items: center;
        gap: 10px;
        font-size: 13px;
        color: white;
    }
    .status-dot {
        width: 8px;
        height: 8px;
        background: #22c55e;
        border-radius: 50%;
        animation: pulse 2s infinite;
    }
    @keyframes pulse {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.5; }
    }
    
    /* SECTION LABEL (small caps above section title) */
    .section-label {
        font-size: 11px;
        color: #6b7280;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        margin-bottom: 4px;
        font-weight: 500;
    }
    .section-title {
        font-size: 22px;
        color: #0f2847;
        font-weight: 600;
        margin: 0 0 24px 0;
    }
    
    /* KPI CARDS — White with colored left border */
    .kpi-card {
        background: white;
        border-radius: 10px;
        padding: 18px 20px;
        border-left: 4px solid #0f2847;
        box-shadow: 0 1px 3px rgba(0,0,0,0.04);
        height: 100%;
    }
    .kpi-card.red { border-left-color: #dc2626; }
    .kpi-card.gold { border-left-color: #c9a961; }
    .kpi-card.green { border-left-color: #16a34a; }
    .kpi-label {
        font-size: 11px;
        color: #6b7280;
        letter-spacing: 0.5px;
        text-transform: uppercase;
        font-weight: 500;
        margin-bottom: 8px;
    }
    .kpi-value {
        font-size: 28px;
        color: #0f2847;
        font-weight: 600;
        line-height: 1.2;
    }
    .kpi-delta {
        font-size: 11px;
        margin-top: 4px;
    }
    .kpi-delta.positive { color: #16a34a; }
    .kpi-delta.negative { color: #dc2626; }
    .kpi-delta.neutral { color: #6b7280; }
    
    /* Chart container */
    .chart-card {
        background: white;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.04);
        margin-bottom: 12px;
    }
    
    /* Tabs styling — sharp corporate look */
    .stTabs [data-baseweb="tab-list"] {
        background: white;
        padding: 0 24px;
        border-bottom: 1px solid #e5e7eb;
        margin: 0 -2rem 24px -2rem;
        gap: 0;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        font-size: 13px;
        font-weight: 500;
        color: #6b7280;
        padding: 0 20px;
        background: transparent;
        border-radius: 0;
    }
    .stTabs [aria-selected="true"] {
        color: #0f2847 !important;
        border-bottom: 2px solid #c9a961 !important;
    }
    
    /* Sidebar */
    section[data-testid="stSidebar"] {
        background: white;
        border-right: 1px solid #e5e7eb;
    }
    section[data-testid="stSidebar"] .block-container {
        padding-top: 2rem;
    }
    .sidebar-title {
        font-size: 11px;
        color: #6b7280;
        letter-spacing: 1.5px;
        font-weight: 600;
        margin-bottom: 16px;
        text-transform: uppercase;
    }
    
    /* Streamlit element overrides */
    .stMetric { background: white; border-radius: 8px; padding: 16px; }
    .stSelectbox label, .stSlider label { 
        color: #4b5563 !important; 
        font-size: 12px !important; 
        font-weight: 500 !important; 
    }
    
    /* Buttons */
    .stButton button {
        background: #0f2847;
        color: white;
        border: none;
        border-radius: 6px;
        font-weight: 500;
        padding: 10px 24px;
    }
    .stButton button:hover {
        background: #1a3a5c;
        color: white;
    }
    
    /* Insight box */
    .insight-box {
        background: white;
        border-radius: 10px;
        padding: 16px 20px;
        border-left: 3px solid #c9a961;
        box-shadow: 0 1px 3px rgba(0,0,0,0.04);
        margin-bottom: 8px;
    }
    .insight-title {
        font-size: 12px;
        color: #6b7280;
        font-weight: 600;
        margin-bottom: 8px;
        letter-spacing: 0.5px;
    }
    .insight-text {
        font-size: 13px;
        color: #1f2937;
        line-height: 1.6;
    }
    
    /* Footer */
    .corp-footer {
        text-align: center;
        padding: 20px;
        color: #6b7280;
        font-size: 11px;
        border-top: 1px solid #e5e7eb;
        margin-top: 32px;
    }
    </style>
""", unsafe_allow_html=True)

# ============================================================
# THEME COLORS — Corporate Navy + Gold Palette
# ============================================================
THEME = {
    'navy': '#0f2847',
    'navy_light': '#1a3a5c',
    'gold': '#c9a961',
    'gold_light': '#e6c989',
    'red': '#dc2626',
    'green': '#16a34a',
    'amber': '#f59e0b',
    'gray': '#6b7280',
    'gray_light': '#e5e7eb',
    'bg': '#f7f8fa',
    'white': '#ffffff'
}

CHART_THEME = {
    'plot_bgcolor': 'white',
    'paper_bgcolor': 'white',
    'font_family': 'Inter, sans-serif',
    'font_color': '#0f2847',
    'title_font_size': 14,
    'axis_color': '#6b7280',
    'grid_color': '#f1f3f5'
}

def style_plotly(fig, height=350):
    """Apply consistent corporate theme to all plotly charts"""
    fig.update_layout(
        plot_bgcolor=CHART_THEME['plot_bgcolor'],
        paper_bgcolor=CHART_THEME['paper_bgcolor'],
        font_family=CHART_THEME['font_family'],
        font_color=CHART_THEME['font_color'],
        height=height,
        margin=dict(l=20, r=20, t=40, b=20),
        title_font_size=CHART_THEME['title_font_size'],
        title_font_color=THEME['navy']
    )
    fig.update_xaxes(
        gridcolor=CHART_THEME['grid_color'],
        linecolor=CHART_THEME['axis_color'],
        tickcolor=CHART_THEME['axis_color'],
        tickfont=dict(size=11, color=CHART_THEME['axis_color'])
    )
    fig.update_yaxes(
        gridcolor=CHART_THEME['grid_color'],
        linecolor=CHART_THEME['axis_color'],
        tickcolor=CHART_THEME['axis_color'],
        tickfont=dict(size=11, color=CHART_THEME['axis_color'])
    )
    return fig

# ============================================================
# DATA LOADING (Cached)
# ============================================================
@st.cache_data
def load_data():
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_path = os.path.join(base_path, 'data', 'APL_Logistics_engineered.csv')
    return pd.read_csv(data_path)

@st.cache_resource
def load_model_artifacts():
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    models_dir = os.path.join(base_path, 'models')
    model = joblib.load(os.path.join(models_dir, 'best_model.pkl'))
    scaler = joblib.load(os.path.join(models_dir, 'scaler.pkl'))
    feature_names = joblib.load(os.path.join(models_dir, 'feature_names.pkl'))
    with open(os.path.join(models_dir, 'best_model_name.txt'), 'r') as f:
        model_name = f.read().strip()
    importance_df = pd.read_csv(os.path.join(models_dir, 'feature_importance.csv'))
    return model, scaler, feature_names, model_name, importance_df

df = load_data()
model, scaler, feature_names, model_name, importance_df = load_model_artifacts()

# ============================================================
# HELPER FUNCTIONS
# ============================================================
def categorize_risk(prob, low_t=0.40, high_t=0.70):
    if prob < low_t: return 'Low Risk'
    elif prob < high_t: return 'Medium Risk'
    return 'High Risk'

def predict_risk(df_subset):
    X = df_subset[feature_names].copy()
    X_scaled = scaler.transform(X)
    return model.predict_proba(X_scaled)[:, 1]

# ============================================================
# CORPORATE HEADER
# ============================================================
st.markdown(f"""
    <div class="corp-header">
        <div class="corp-logo">
            <div class="corp-logo-icon">📦</div>
            <div>
                <p class="corp-title">APL LOGISTICS</p>
                <p class="corp-subtitle">OPERATIONS INTELLIGENCE PLATFORM</p>
            </div>
        </div>
        <div class="corp-status">
            <div class="status-dot"></div>
            <span>Live · {model_name}</span>
        </div>
    </div>
""", unsafe_allow_html=True)

# ============================================================
# SIDEBAR FILTERS
# ============================================================
with st.sidebar:
    st.markdown('<p class="sidebar-title">Filters & Controls</p>', unsafe_allow_html=True)
    
    shipping_modes = ['All'] + sorted(df['Shipping Mode'].unique().tolist())
    selected_mode = st.selectbox("Shipping Mode", shipping_modes)
    
    markets = ['All'] + sorted(df['Market'].unique().tolist())
    selected_market = st.selectbox("Market", markets)
    
    segments = ['All'] + sorted(df['Customer Segment'].unique().tolist())
    selected_segment = st.selectbox("Customer Segment", segments)
    
    st.markdown('<p class="sidebar-title" style="margin-top: 24px;">Risk Thresholds</p>', unsafe_allow_html=True)
    low_thresh = st.slider("Low → Medium", 0.0, 1.0, 0.40, 0.05)
    high_thresh = st.slider("Medium → High", 0.0, 1.0, 0.70, 0.05)
    
    st.markdown("---")
    st.markdown(f"""
        <div style='background: #f7f8fa; padding: 12px; border-radius: 6px; font-size: 11px; color: #4b5563;'>
            <strong style='color: #0f2847;'>Model Info</strong><br>
            Algorithm: {model_name}<br>
            Features: {len(feature_names)}<br>
            Training: 158,360 samples
        </div>
    """, unsafe_allow_html=True)

# Apply filters
filtered_df = df.copy()
if selected_mode != 'All':
    filtered_df = filtered_df[filtered_df['Shipping Mode'] == selected_mode]
if selected_market != 'All':
    filtered_df = filtered_df[filtered_df['Market'] == selected_market]
if selected_segment != 'All':
    filtered_df = filtered_df[filtered_df['Customer Segment'] == selected_segment]

if len(filtered_df) > 0:
    filtered_df = filtered_df.copy()
    filtered_df['Late_Probability'] = predict_risk(filtered_df)
    filtered_df['Risk_Category'] = filtered_df['Late_Probability'].apply(
        lambda p: categorize_risk(p, low_thresh, high_thresh)
    )

# ============================================================
# TABS
# ============================================================
tab1, tab2, tab3, tab4 = st.tabs([
    "  Executive Overview  ", 
    "  Risk Predictor  ", 
    "  Geographic Analytics  ",
    "  Action Queue  "
])

# ============================================================
# TAB 1: EXECUTIVE OVERVIEW
# ============================================================
with tab1:
    if len(filtered_df) == 0:
        st.warning("No orders match current filters.")
    else:
        st.markdown('<p class="section-label">EXECUTIVE SUMMARY</p>', unsafe_allow_html=True)
        st.markdown('<p class="section-title">Delivery risk intelligence</p>', unsafe_allow_html=True)
        
        # KPI ROW
        total_orders = len(filtered_df)
        late_count = (filtered_df['Late_delivery_risk'] == 1).sum()
        late_rate = filtered_df['Late_delivery_risk'].mean() * 100
        high_risk_count = (filtered_df['Risk_Category'] == 'High Risk').sum()
        high_risk_pct = (high_risk_count / total_orders) * 100
        revenue_at_risk = filtered_df[filtered_df['Risk_Category'] == 'High Risk']['Sales'].sum()
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.markdown(f"""
                <div class="kpi-card">
                    <div class="kpi-label">Total Orders</div>
                    <div class="kpi-value">{total_orders:,}</div>
                    <div class="kpi-delta neutral">▲ Active pipeline</div>
                </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
                <div class="kpi-card red">
                    <div class="kpi-label">Late Deliveries</div>
                    <div class="kpi-value">{late_count:,}</div>
                    <div class="kpi-delta negative">▼ {late_rate:.1f}% late rate</div>
                </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown(f"""
                <div class="kpi-card gold">
                    <div class="kpi-label">High Risk Flagged</div>
                    <div class="kpi-value">{high_risk_count:,}</div>
                    <div class="kpi-delta neutral">▲ {high_risk_pct:.1f}% of pipeline</div>
                </div>
            """, unsafe_allow_html=True)
        
        with col4:
            st.markdown(f"""
                <div class="kpi-card green">
                    <div class="kpi-label">Revenue at Risk</div>
                    <div class="kpi-value">${revenue_at_risk/1e6:.1f}M</div>
                    <div class="kpi-delta neutral">Predicted exposure</div>
                </div>
            """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # CHARTS ROW
        col_left, col_right = st.columns([2, 1])
        
        with col_left:
            with st.container():
                st.markdown('<p style="font-size: 13px; color: #0f2847; font-weight: 600; margin-bottom: 12px;">Risk Distribution by Category</p>', unsafe_allow_html=True)
                
                risk_counts = filtered_df['Risk_Category'].value_counts().reindex(
                    ['Low Risk', 'Medium Risk', 'High Risk']).fillna(0)
                
                fig = go.Figure(data=[go.Pie(
                    labels=risk_counts.index,
                    values=risk_counts.values,
                    hole=0.65,
                    marker=dict(colors=[THEME['green'], THEME['gold'], THEME['red']],
                                line=dict(color='white', width=2)),
                    textinfo='label+percent',
                    textfont=dict(size=12, color='white'),
                    hovertemplate='<b>%{label}</b><br>%{value:,} orders<br>%{percent}<extra></extra>'
                )])
                fig.add_annotation(
                    text=f"<b>{total_orders/1000:.0f}K</b><br><span style='font-size:11px'>orders</span>",
                    x=0.5, y=0.5, font_size=20, font_color=THEME['navy'], showarrow=False
                )
                fig = style_plotly(fig, height=320)
                fig.update_layout(showlegend=False, margin=dict(l=0, r=0, t=10, b=10))
                st.plotly_chart(fig, use_container_width=True)
        
        with col_right:
            st.markdown('<p style="font-size: 13px; color: #0f2847; font-weight: 600; margin-bottom: 12px;">Key Insights</p>', unsafe_allow_html=True)
            
            # Auto-generated insights
            top_market = filtered_df.groupby('Market')['Late_delivery_risk'].mean().idxmax()
            top_market_rate = filtered_df.groupby('Market')['Late_delivery_risk'].mean().max() * 100
            top_mode = filtered_df.groupby('Shipping Mode')['Late_delivery_risk'].mean().idxmax()
            top_mode_rate = filtered_df.groupby('Shipping Mode')['Late_delivery_risk'].mean().max() * 100
            
            insights = [
                f"<b>{top_market}</b> leads delays at <b>{top_market_rate:.1f}%</b>",
                f"<b>{top_mode}</b> mode has highest late risk (<b>{top_mode_rate:.1f}%</b>)",
                f"<b>{high_risk_count:,}</b> orders need urgent intervention",
                f"Revenue exposure of <b>${revenue_at_risk/1e6:.1f}M</b> identified"
            ]
            
            for ins in insights:
                st.markdown(f"""
                    <div class="insight-box">
                        <div class="insight-text">▸ {ins}</div>
                    </div>
                """, unsafe_allow_html=True)
        
        # SECOND ROW — Distribution + Mode comparison
        st.markdown("<br>", unsafe_allow_html=True)
        col_a, col_b = st.columns(2)
        
        with col_a:
            st.markdown('<p style="font-size: 13px; color: #0f2847; font-weight: 600; margin-bottom: 12px;">Probability Distribution</p>', unsafe_allow_html=True)
            
            fig = go.Figure()
            fig.add_trace(go.Histogram(
                x=filtered_df['Late_Probability'],
                nbinsx=40,
                marker=dict(color=THEME['navy'], line=dict(color='white', width=0.5)),
                hovertemplate='Probability: %{x:.2f}<br>Orders: %{y:,}<extra></extra>'
            ))
            fig.add_vline(x=low_thresh, line_dash="dash", line_color=THEME['gold'], 
                          annotation_text=f"Low/Med: {low_thresh:.2f}", annotation_position="top")
            fig.add_vline(x=high_thresh, line_dash="dash", line_color=THEME['red'],
                          annotation_text=f"Med/High: {high_thresh:.2f}", annotation_position="top")
            fig = style_plotly(fig, height=300)
            fig.update_layout(xaxis_title="Late Delivery Probability", yaxis_title="Order Count")
            st.plotly_chart(fig, use_container_width=True)
        
        with col_b:
            st.markdown('<p style="font-size: 13px; color: #0f2847; font-weight: 600; margin-bottom: 12px;">Late Rate by Shipping Mode</p>', unsafe_allow_html=True)
            
            mode_data = filtered_df.groupby('Shipping Mode')['Late_delivery_risk'].agg(['mean', 'count']).reset_index()
            mode_data['Rate'] = mode_data['mean'] * 100
            mode_data = mode_data.sort_values('Rate', ascending=True)
            
            fig = go.Figure(go.Bar(
                y=mode_data['Shipping Mode'],
                x=mode_data['Rate'],
                orientation='h',
                marker=dict(color=mode_data['Rate'], colorscale=[[0, THEME['green']], [0.5, THEME['gold']], [1, THEME['red']]]),
                text=[f"{v:.1f}%" for v in mode_data['Rate']],
                textposition='outside',
                hovertemplate='<b>%{y}</b><br>Rate: %{x:.1f}%<extra></extra>'
            ))
            fig = style_plotly(fig, height=300)
            fig.update_layout(xaxis_title="Late Delivery Rate (%)", yaxis_title="", showlegend=False)
            st.plotly_chart(fig, use_container_width=True)

# ============================================================
# TAB 2: RISK PREDICTOR
# ============================================================
with tab2:
    st.markdown('<p class="section-label">ORDER-LEVEL ANALYSIS</p>', unsafe_allow_html=True)
    st.markdown('<p class="section-title">Predict risk for a specific order</p>', unsafe_allow_html=True)
    
    # Input form in a card-like structure
    with st.container():
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("**Order Details**")
            input_quantity = st.number_input("Quantity", 1, 10, 1)
            input_scheduled_days = st.selectbox("Scheduled Days", [0, 1, 2, 3, 4], index=2)
            input_product_price = st.number_input("Product Price ($)", 1.0, 2000.0, 100.0)
        
        with col2:
            st.markdown("**Financial Details**")
            input_discount_rate = st.slider("Discount Rate", 0.0, 0.30, 0.05, 0.01)
            input_sales = st.number_input("Sales Amount ($)", 1.0, 5000.0, 200.0)
            input_profit_ratio = st.slider("Profit Ratio", -1.0, 1.0, 0.15, 0.05)
        
        with col3:
            st.markdown("**Logistics**")
            input_mode = st.selectbox("Shipping Mode ", df['Shipping Mode'].unique().tolist())
            input_market = st.selectbox("Market ", df['Market'].unique().tolist())
            input_segment = st.selectbox("Customer Segment ", df['Customer Segment'].unique().tolist())
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        if st.button("⚡ Generate Risk Prediction", type="primary", use_container_width=True):
            # Find template order
            template = df[
                (df['Shipping Mode'] == input_mode) &
                (df['Market'] == input_market) &
                (df['Customer Segment'] == input_segment)
            ].head(1)
            
            if len(template) == 0:
                template = df.head(1)
            
            new_order = template[feature_names].copy()
            update_map = {
                'Order Item Quantity': input_quantity,
                'Days for shipment (scheduled)': input_scheduled_days,
                'Product Price': input_product_price,
                'Order Item Discount Rate': input_discount_rate,
                'Sales': input_sales,
                'Order Item Profit Ratio': input_profit_ratio
            }
            for col, val in update_map.items():
                if col in new_order.columns:
                    new_order[col] = val
            
            new_order_scaled = scaler.transform(new_order)
            prob = model.predict_proba(new_order_scaled)[0, 1]
            risk_cat = categorize_risk(prob, low_thresh, high_thresh)
            
            st.markdown("---")
            st.markdown('<p class="section-label">PREDICTION RESULT</p>', unsafe_allow_html=True)
            
            # Result KPIs
            risk_color = THEME['green'] if risk_cat == 'Low Risk' else (THEME['gold'] if risk_cat == 'Medium Risk' else THEME['red'])
            
            res_col1, res_col2 = st.columns([1, 1])
            
            with res_col1:
                # Gauge chart
                fig = go.Figure(go.Indicator(
                    mode="gauge+number",
                    value=prob * 100,
                    number={'suffix': "%", 'font': {'size': 36, 'color': THEME['navy']}},
                    gauge={
                        'axis': {'range': [None, 100], 'tickwidth': 1, 'tickcolor': THEME['gray']},
                        'bar': {'color': risk_color, 'thickness': 0.3},
                        'bgcolor': "white",
                        'borderwidth': 0,
                        'steps': [
                            {'range': [0, low_thresh*100], 'color': '#dcfce7'},
                            {'range': [low_thresh*100, high_thresh*100], 'color': '#fef3c7'},
                            {'range': [high_thresh*100, 100], 'color': '#fee2e2'}
                        ],
                    }
                ))
                fig.update_layout(
                    height=280,
                    margin=dict(l=20, r=20, t=20, b=20),
                    paper_bgcolor='white',
                    font_family='Inter'
                )
                st.plotly_chart(fig, use_container_width=True)
            
            with res_col2:
                st.markdown(f"""
                    <div style='background: white; border-radius: 10px; padding: 24px; height: 280px; display: flex; flex-direction: column; justify-content: center;'>
                        <div style='font-size: 11px; color: #6b7280; letter-spacing: 1px;'>RISK ASSESSMENT</div>
                        <div style='font-size: 32px; color: {risk_color}; font-weight: 600; margin: 8px 0;'>{risk_cat}</div>
                        <div style='font-size: 13px; color: #6b7280; line-height: 1.6; margin-top: 12px;'>
                            <strong style='color: #0f2847;'>Probability:</strong> {prob:.1%}<br>
                            <strong style='color: #0f2847;'>Confidence:</strong> {abs(prob-0.5)*200:.0f}%<br>
                            <strong style='color: #0f2847;'>Model:</strong> {model_name}
                        </div>
                    </div>
                """, unsafe_allow_html=True)
            
            # Action recommendation
            st.markdown("<br>", unsafe_allow_html=True)
            if risk_cat == 'High Risk':
                st.error("🚨 **URGENT ACTION REQUIRED:** Reroute to express partner, notify customer of potential delay, escalate to operations manager.")
            elif risk_cat == 'Medium Risk':
                st.warning("⚠️ **MONITOR CLOSELY:** Enable enhanced tracking, consider proactive customer communication, verify SLA capacity.")
            else:
                st.success("✅ **STANDARD PROCESSING:** Low risk detected. Process via standard logistics flow.")
            
            # Top influencing factors
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown('<p class="section-label">TOP RISK DRIVERS</p>', unsafe_allow_html=True)
            
            top5 = importance_df.head(5)
            fig = go.Figure(go.Bar(
                y=top5['Feature'],
                x=top5['Importance'],
                orientation='h',
                marker=dict(color=THEME['gold']),
                text=[f"{v:.3f}" for v in top5['Importance']],
                textposition='outside'
            ))
            fig = style_plotly(fig, height=250)
            fig.update_layout(xaxis_title="Feature Importance", yaxis_title="", showlegend=False)
            fig.update_yaxes(autorange='reversed')
            st.plotly_chart(fig, use_container_width=True)

# ============================================================
# TAB 3: GEOGRAPHIC ANALYTICS
# ============================================================
with tab3:
    st.markdown('<p class="section-label">GEOGRAPHIC ANALYSIS</p>', unsafe_allow_html=True)
    st.markdown('<p class="section-title">Regional & mode risk patterns</p>', unsafe_allow_html=True)
    
    if len(filtered_df) == 0:
        st.warning("No orders match current filters.")
    else:
        col_a, col_b = st.columns(2)
        
        with col_a:
            st.markdown('<p style="font-size: 13px; color: #0f2847; font-weight: 600; margin-bottom: 12px;">Top 10 Regions by Late Rate</p>', unsafe_allow_html=True)
            
            region_data = filtered_df.groupby('Order Region').agg(
                count=('Late_delivery_risk', 'count'),
                rate=('Late_delivery_risk', 'mean')
            ).reset_index()
            region_data = region_data[region_data['count'] > 500]
            region_data['rate_pct'] = region_data['rate'] * 100
            region_data = region_data.sort_values('rate_pct', ascending=True).tail(10)
            
            fig = go.Figure(go.Bar(
                y=region_data['Order Region'],
                x=region_data['rate_pct'],
                orientation='h',
                marker=dict(color=region_data['rate_pct'], 
                            colorscale=[[0, THEME['green']], [0.5, THEME['gold']], [1, THEME['red']]]),
                text=[f"{v:.1f}%" for v in region_data['rate_pct']],
                textposition='outside'
            ))
            fig = style_plotly(fig, height=400)
            fig.update_layout(xaxis_title="Late Rate (%)", yaxis_title="", showlegend=False)
            st.plotly_chart(fig, use_container_width=True)
        
        with col_b:
            st.markdown('<p style="font-size: 13px; color: #0f2847; font-weight: 600; margin-bottom: 12px;">Late Rate by Market</p>', unsafe_allow_html=True)
            
            market_data = filtered_df.groupby('Market')['Late_delivery_risk'].agg(['mean', 'count']).reset_index()
            market_data['rate'] = market_data['mean'] * 100
            market_data = market_data.sort_values('rate', ascending=False)
            
            fig = go.Figure(go.Bar(
                x=market_data['Market'],
                y=market_data['rate'],
                marker=dict(color=THEME['navy']),
                text=[f"{v:.1f}%" for v in market_data['rate']],
                textposition='outside'
            ))
            fig = style_plotly(fig, height=400)
            fig.update_layout(xaxis_title="", yaxis_title="Late Rate (%)", showlegend=False)
            st.plotly_chart(fig, use_container_width=True)
        
        # Heatmap
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown('<p style="font-size: 13px; color: #0f2847; font-weight: 600; margin-bottom: 12px;">Risk Heatmap: Shipping Mode × Market</p>', unsafe_allow_html=True)
        
        heatmap_data = filtered_df.groupby(['Shipping Mode', 'Market'])['Late_delivery_risk'].mean().unstack() * 100
        
        fig = go.Figure(data=go.Heatmap(
            z=heatmap_data.values,
            x=heatmap_data.columns,
            y=heatmap_data.index,
            colorscale=[[0, THEME['green']], [0.5, THEME['gold']], [1, THEME['red']]],
            text=heatmap_data.round(1).values,
            texttemplate='%{text}%',
            textfont={"size": 12, "color": "white"},
            colorbar=dict(title="Late Rate (%)", titlefont=dict(size=11))
        ))
        fig = style_plotly(fig, height=350)
        st.plotly_chart(fig, use_container_width=True)
        
        # Geographic scatter
        if 'Latitude' in filtered_df.columns and 'Longitude' in filtered_df.columns:
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown('<p style="font-size: 13px; color: #0f2847; font-weight: 600; margin-bottom: 12px;">Global Order Distribution by Risk Level</p>', unsafe_allow_html=True)
            
            sample = filtered_df.sample(n=min(3000, len(filtered_df)), random_state=42)
            fig = px.scatter_geo(
                sample, lat='Latitude', lon='Longitude',
                color='Risk_Category',
                color_discrete_map={
                    'Low Risk': THEME['green'],
                    'Medium Risk': THEME['gold'],
                    'High Risk': THEME['red']
                },
                opacity=0.65,
                size_max=5
            )
            fig.update_layout(
                height=500,
                margin=dict(l=0, r=0, t=0, b=0),
                geo=dict(
                    bgcolor='white',
                    showland=True,
                    landcolor='#f7f8fa',
                    showocean=True,
                    oceancolor='#e6f1f9',
                    showcoastlines=True,
                    coastlinecolor='#cbd5e1'
                )
            )
            st.plotly_chart(fig, use_container_width=True)

# ============================================================
# TAB 4: ACTION QUEUE
# ============================================================
with tab4:
    st.markdown('<p class="section-label">OPERATIONS</p>', unsafe_allow_html=True)
    st.markdown('<p class="section-title">Priority action queue</p>', unsafe_allow_html=True)
    
    if len(filtered_df) == 0:
        st.warning("No orders match current filters.")
    else:
        high_risk = filtered_df[filtered_df['Risk_Category'] == 'High Risk'].copy()
        high_risk = high_risk.sort_values('Late_Probability', ascending=False)
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.markdown(f"""
                <div class="kpi-card red">
                    <div class="kpi-label">High Risk Orders</div>
                    <div class="kpi-value">{len(high_risk):,}</div>
                    <div class="kpi-delta negative">Requires action</div>
                </div>
            """, unsafe_allow_html=True)
        
        with col2:
            avg_prob = high_risk['Late_Probability'].mean() if len(high_risk) > 0 else 0
            st.markdown(f"""
                <div class="kpi-card gold">
                    <div class="kpi-label">Avg Risk Score</div>
                    <div class="kpi-value">{avg_prob:.1%}</div>
                    <div class="kpi-delta neutral">Predicted late prob</div>
                </div>
            """, unsafe_allow_html=True)
        
        with col3:
            revenue = high_risk['Sales'].sum() if len(high_risk) > 0 else 0
            st.markdown(f"""
                <div class="kpi-card green">
                    <div class="kpi-label">Revenue Exposure</div>
                    <div class="kpi-value">${revenue/1e6:.2f}M</div>
                    <div class="kpi-delta neutral">If left unaddressed</div>
                </div>
            """, unsafe_allow_html=True)
        
        with col4:
            top_mode = high_risk['Shipping Mode'].mode().iloc[0] if len(high_risk) > 0 else 'N/A'
            st.markdown(f"""
                <div class="kpi-card">
                    <div class="kpi-label">Top Risk Mode</div>
                    <div class="kpi-value" style="font-size: 18px;">{top_mode}</div>
                    <div class="kpi-delta neutral">Most flagged</div>
                </div>
            """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        if len(high_risk) > 0:
            st.markdown('<p style="font-size: 13px; color: #0f2847; font-weight: 600; margin-bottom: 12px;">Top 50 Priority Orders</p>', unsafe_allow_html=True)
            
            display_cols = ['Late_Probability', 'Risk_Category', 'Shipping Mode', 
                            'Market', 'Customer Segment', 'Sales', 
                            'Days for shipment (scheduled)', 'Order Item Quantity']
            display_cols = [c for c in display_cols if c in high_risk.columns]
            
            display_df = high_risk[display_cols].head(50).copy()
            display_df['Late_Probability'] = (display_df['Late_Probability'] * 100).round(1).astype(str) + '%'
            if 'Sales' in display_df.columns:
                display_df['Sales'] = display_df['Sales'].apply(lambda x: f"${x:,.2f}")
            
            st.dataframe(
                display_df,
                use_container_width=True,
                hide_index=True,
                column_config={
                    "Late_Probability": st.column_config.TextColumn("Risk %", width="small"),
                    "Risk_Category": st.column_config.TextColumn("Category", width="small"),
                    "Sales": st.column_config.TextColumn("Revenue", width="small"),
                }
            )
            
            csv = high_risk.head(50).to_csv(index=False)
            st.download_button(
                "📥 Export Priority Queue (CSV)",
                csv,
                "apl_priority_orders.csv",
                "text/csv",
                use_container_width=True
            )
            
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown("""
                <div style='background: white; border-radius: 10px; padding: 20px; border-left: 3px solid #c9a961;'>
                    <div style='font-size: 12px; color: #6b7280; letter-spacing: 1px; margin-bottom: 12px;'>RECOMMENDED ACTIONS</div>
                    <div style='font-size: 13px; color: #1f2937; line-height: 1.8;'>
                        <strong style='color: #0f2847;'>1. Reroute:</strong> Move high-risk express shipments to alternate carriers<br>
                        <strong style='color: #0f2847;'>2. Communicate:</strong> Proactively notify customers of potential delays<br>
                        <strong style='color: #0f2847;'>3. Allocate:</strong> Prioritize warehouse processing for flagged orders<br>
                        <strong style='color: #0f2847;'>4. Track:</strong> Enable real-time visibility on at-risk shipments<br>
                        <strong style='color: #0f2847;'>5. Escalate:</strong> Brief operations manager on top 10 priorities daily
                    </div>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.success("✅ No high-risk orders in current filter view.")

# ============================================================
# FOOTER
# ============================================================
st.markdown(f"""
    <div class="corp-footer">
        APL Logistics Operations Intelligence Platform · Powered by {model_name} · 
        Built by Mohan · Unified Mentor Internship 2026
    </div>
""", unsafe_allow_html=True)