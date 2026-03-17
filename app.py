import streamlit as st
import pickle
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from PIL import Image
import base64
import io

# Custom CSS for modern UI
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: 700;
        background: linear-gradient(45deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 2rem;
    }
    .module-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 15px;
        padding: 2rem;
        margin: 1rem 0;
        color: white;
        box-shadow: 0 8px 32px rgba(31, 38, 135, 0.37);
        backdrop-filter: blur(4px);
        border: 1px solid rgba(255, 255, 255, 0.18);
    }
    .result-card {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        border-radius: 15px;
        padding: 2rem;
        margin: 1rem 0;
        color: white;
        box-shadow: 0 8px 32px rgba(31, 38, 135, 0.37);
    }
    .input-container {
        background: rgba(255, 255, 255, 0.1);
        border-radius: 10px;
        padding: 1.5rem;
        margin: 1rem 0;
        backdrop-filter: blur(10px);
    }
    .stButton>button {
        background: linear-gradient(45deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.75rem 2rem;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4);
    }
    .metric-card {
        background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
        border-radius: 10px;
        padding: 1rem;
        margin: 0.5rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        text-align: center;
        color: #333;
    }
    .sidebar-content {
        background: linear-gradient(180deg, #667eea 0%, #764ba2 100%);
        padding: 2rem 1rem;
        border-radius: 15px;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Page configuration
st.set_page_config(
    page_title="🛍️ Shopping Mall Intelligence System",
    page_icon="🛍️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load models
@st.cache_resource
def load_models():
    kmeans = pickle.load(open('models/kmeans_model.pkl', 'rb'))
    rules = pickle.load(open('models/apriori_rules.pkl', 'rb'))
    sentiment_model = pickle.load(open('models/sentiment_model.pkl', 'rb'))
    vectorizer = pickle.load(open('models/vectorizer.pkl', 'rb'))
    return kmeans, rules, sentiment_model, vectorizer

kmeans, rules, sentiment_model, vectorizer = load_models()

# Load sample data for visualizations
@st.cache_data
def load_sample_data():
    customers = pd.read_csv('data/Mall_Customers.csv')
    return customers

customers_df = load_sample_data()

# Main header
st.markdown('<h1 class="main-header">🛍️ Shopping Mall Intelligence System</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center; font-size: 1.2rem; color: #666;">AI-Powered Customer Insights & Product Intelligence</p>', unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.markdown('<div class="sidebar-content">', unsafe_allow_html=True)
st.sidebar.title("🎯 Navigation")
option = st.sidebar.selectbox(
    "Choose Your Module",
    ("🏠 Dashboard", "👥 Customer Segmentation", "🛒 Product Recommendation", "💬 Review Sentiment Analysis"),
    help="Select the AI module you want to use"
)
st.sidebar.markdown('</div>', unsafe_allow_html=True)

# Dashboard
if option == "🏠 Dashboard":
    st.markdown("## 📊 System Overview")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="metric-card">
            <h3>👥 Customer Segmentation</h3>
            <p>AI-powered clustering of customers based on spending patterns and demographics</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="metric-card">
            <h3>🛒 Product Recommendations</h3>
            <p>Smart product suggestions using association rule mining</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="metric-card">
            <h3>💬 Sentiment Analysis</h3>
            <p>Advanced NLP for understanding customer reviews and feedback</p>
        </div>
        """, unsafe_allow_html=True)

    # Customer distribution visualization
    st.markdown("## 📈 Customer Distribution Overview")
    fig = px.scatter(customers_df, x='Annual Income (k$)', y='Spending Score (1-100)',
                     color='Genre', size='Age',
                     title="Customer Segmentation Data Distribution",
                     color_discrete_map={'Male': '#667eea', 'Female': '#764ba2'})
    fig.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig, width='stretch')

# Customer Segmentation Module
elif option == "👥 Customer Segmentation":
    st.markdown('<div class="module-card">', unsafe_allow_html=True)
    st.markdown("## 👥 Customer Segmentation")
    st.markdown("Analyze customer behavior patterns using advanced clustering algorithms")
    st.markdown('</div>', unsafe_allow_html=True)

    col1, col2 = st.columns([1, 2])

    with col1:
        st.markdown('<div class="input-container">', unsafe_allow_html=True)
        st.markdown("### 📝 Customer Information")

        income = st.number_input("Annual Income (k$)", min_value=0, max_value=200, value=50,
                                help="Enter customer's annual income in thousands")
        score = st.number_input("Spending Score (1-100)", min_value=1, max_value=100, value=50,
                               help="Customer's spending score from 1-100")

        analyze_btn = st.button("🔍 Analyze Customer", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        if analyze_btn:
            cluster_labels = {
                0: "💰 Budget Conscious Shoppers",
                1: "👑 VIP High-Value Customers",
                2: "🎯 Value-Driven Spenders",
                3: "💼 Affluent Conservative Buyers",
                4: "🛒 Occasional Shoppers"
            }

            cluster_descriptions = {
                0: "Customers who shop carefully and look for the best deals",
                1: "High-income customers who spend generously - your most valuable segment",
                2: "Customers who find great value despite lower income",
                3: "Wealthy customers who are selective with their purchases",
                4: "Customers who shop infrequently and spend modestly"
            }

            cluster = kmeans.predict([[income, score]])[0]

            st.markdown('<div class="result-card">', unsafe_allow_html=True)
            st.markdown(f"### 🎯 Customer Profile: {cluster_labels[cluster]}")
            st.markdown(f"**Description:** {cluster_descriptions[cluster]}")
            st.markdown('</div>', unsafe_allow_html=True)

            # Visualization
            fig = px.scatter(customers_df, x='Annual Income (k$)', y='Spending Score (1-100)',
                           color=kmeans.labels_.astype(str),
                           title="Customer Clusters Visualization",
                           color_discrete_map={'0': '#FF6B6B', '1': '#4ECDC4', '2': '#45B7D1',
                                             '3': '#96CEB4', '4': '#FFEAA7'})
            fig.add_trace(go.Scatter(x=[income], y=[score], mode='markers',
                                   marker=dict(size=15, color='red', symbol='star'),
                                   name='Your Customer'))
            fig.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
            st.plotly_chart(fig, width='stretch')

# Product Recommendation Module
elif option == "🛒 Product Recommendation":
    st.markdown('<div class="module-card">', unsafe_allow_html=True)
    st.markdown("## 🛒 Smart Product Recommendations")
    st.markdown("Discover products that customers frequently buy together")
    st.markdown('</div>', unsafe_allow_html=True)

    col1, col2 = st.columns([1, 2])

    with col1:
        st.markdown('<div class="input-container">', unsafe_allow_html=True)
        st.markdown("### 🛍️ Product Selection")

        # Get unique products from rules
        available_products = sorted(list(set(rules['Left Hand Side'].unique())))
        product = st.selectbox("Select a product", available_products,
                              help="Choose a product to get recommendations")

        recommend_btn = st.button("🎯 Get Recommendations", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        if recommend_btn:
            recommendations = rules[rules['Left Hand Side'] == product]['Right Hand Side'].tolist()

            if not recommendations:
                st.markdown('<div class="result-card">', unsafe_allow_html=True)
                st.warning("🤔 No recommendations found for this product")
                st.markdown("Try selecting a different product or check our popular recommendations below.")
                st.markdown('</div>', unsafe_allow_html=True)
            else:
                st.markdown('<div class="result-card">', unsafe_allow_html=True)
                st.markdown(f"### 🎁 Recommended Products for: **{product}**")
                st.markdown('</div>', unsafe_allow_html=True)

                # Display recommendations in a nice grid
                cols = st.columns(min(len(recommendations), 3))
                for i, rec in enumerate(recommendations[:9]):  # Limit to 9 recommendations
                    with cols[i % 3]:
                        st.markdown(f"""
                        <div style="background: linear-gradient(135deg, #e0c3fc 0%, #8ec5fc 100%); border-radius: 10px; padding: 1rem; margin: 0.5rem 0; text-align: center; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
                            <h4>🛒 {rec}</h4>
                            <p style="color: #666; margin: 0;">Frequently bought together</p>
                        </div>
                        """, unsafe_allow_html=True)

# Review Sentiment Analysis Module
elif option == "💬 Review Sentiment Analysis":
    st.markdown('<div class="module-card">', unsafe_allow_html=True)
    st.markdown("## 💬 Customer Review Analysis")
    st.markdown("Understand customer sentiment with AI-powered analysis")
    st.markdown('</div>', unsafe_allow_html=True)

    col1, col2 = st.columns([1, 2])

    with col1:
        st.markdown('<div class="input-container">', unsafe_allow_html=True)
        st.markdown("### 📝 Review Input")

        review = st.text_area("Enter customer review", height=150,
                             placeholder="Type or paste a customer review here...",
                             help="Enter the customer review you want to analyze")

        analyze_btn = st.button("🔍 Analyze Sentiment", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        if analyze_btn:
            if review.strip() == "":
                st.markdown('<div class="result-card">', unsafe_allow_html=True)
                st.warning("⚠️ Please enter a review to analyze")
                st.markdown('</div>', unsafe_allow_html=True)
            else:
                text = review.lower()

                # Rule-based checks
                positive_words = ["good","great","clean","nice","excellent","amazing","spacious","beautiful","love","best","perfect","wonderful"]
                negative_words = ["bad","dirty","crowded","expensive","worst","poor","slow","terrible","hate","awful","disgusting","horrible"]

                # Negation detection
                negation_detected = False
                for word in positive_words:
                    if f"not {word}" in text or f"n't {word}" in text:
                        negation_detected = True
                        break

                # Mixed sentiment detection
                mixed_indicators = ["but", "however", "although", "though", "yet", "still"]
                mixed_detected = any(word in text for word in mixed_indicators)

                # ML Prediction
                review_vector = vectorizer.transform([review]).toarray()
                proba = sentiment_model.predict_proba(review_vector)[0]
                pos_score = proba[1]
                neg_score = proba[0]

                # Determine final sentiment
                
                if mixed_detected or abs(pos_score - neg_score) < 0.15:
                    sentiment = "Mixed"
                    emoji = "😐"
                    color = "#FFA726"
                    reason = "Mixed opinions or conflicting sentiments detected"
                elif negation_detected:
                    sentiment = "Negative"
                    emoji = "😞"
                    color = "#FF6B6B"
                    reason = "Negation detected"
                elif pos_score > neg_score:
                    sentiment = "Positive"
                    emoji = "😊"
                    color = "#4ECDC4"
                    reason = "Overall positive sentiment detected"
                else:
                    sentiment = "Negative"
                    emoji = "😞"
                    color = "#FF6B6B"
                    reason = "Overall negative sentiment detected"

                # Display results
                st.markdown(f"""
                <div class="result-card" style="background: linear-gradient(135deg, {color} 0%, {color}88 100%);">
                    <h2>{emoji} Sentiment: {sentiment}</h2>
                    <p><strong>Confidence:</strong> {max(pos_score, neg_score):.2%}</p>
                    <p><strong>Analysis:</strong> {reason}</p>
                </div>
                """, unsafe_allow_html=True)

                # Sentiment scores visualization
                if sentiment == "Mixed":
                    # For mixed, show a 50-50 histogram
                    # Sentiment scores visualization

                    fig = go.Figure()

                    if sentiment == "Mixed":
                        neg_val = 0.5
                        pos_val = 0.5
                        colors = ['#FFA726', '#FFA726']

                    elif sentiment == "Positive":
                        neg_val = 0
                        pos_val = 1
                        colors = ['#FF6B6B', '#4ECDC4']

                    else:  # Negative
                        neg_val = 1
                        pos_val = 0
                        colors = ['#FF6B6B', '#4ECDC4']


                    fig.add_trace(go.Bar(
                        x=['Negative', 'Positive'],
                        y=[neg_val, pos_val],
                        marker_color=colors,
                        text=[f'{neg_val:.2%}', f'{pos_val:.2%}'],
                        textposition='auto'
                    ))

                    fig.update_layout(
                        title="Sentiment Score Breakdown",
                        yaxis=dict(range=[0,1]),
                        plot_bgcolor='rgba(0,0,0,0)',
                        paper_bgcolor='rgba(0,0,0,0)',
                        font=dict(color='white')
                    )

                    st.plotly_chart(fig, width='stretch')

# Footer
st.markdown("---")