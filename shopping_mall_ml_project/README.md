# 🛍️ Shopping Mall Intelligence System

A modern, AI-powered web application for shopping mall analytics and customer insights built with Streamlit and Machine Learning.

## ✨ Features

### 👥 Customer Segmentation
- **AI-powered clustering** using K-means algorithm
- **Interactive visualizations** showing customer distribution
- **Real-time analysis** of customer spending patterns
- **5 distinct customer segments** with detailed profiles

### 🛒 Product Recommendation
- **Association rule mining** using Apriori algorithm
- **Smart product suggestions** based on purchase patterns
- **Interactive product selection** with dropdown interface
- **Visual recommendation cards** for better UX

### 💬 Sentiment Analysis
- **Advanced NLP** for customer review analysis
- **Rule-based + ML hybrid approach** for accurate sentiment detection
- **Real-time confidence scores** and reasoning
- **Interactive sentiment visualization** with charts

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone or download** the project files

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   streamlit run app.py
   ```

4. **Open your browser** and navigate to `http://localhost:8501`

## 📊 Dashboard Overview

The application features a beautiful, modern interface with:

- **🏠 Dashboard**: Overview of all modules with data visualizations
- **Responsive design** that works on desktop and mobile
- **Interactive charts** powered by Plotly
- **Gradient backgrounds** and modern UI components
- **Real-time analysis** with instant results

## 🛠️ Technical Stack

- **Frontend**: Streamlit with custom CSS
- **Data Visualization**: Plotly Express & Graph Objects
- **Machine Learning**:
  - Scikit-learn (K-means, Sentiment Analysis)
  - MLxtend (Apriori algorithm)
- **Data Processing**: Pandas, NumPy
- **Styling**: Custom CSS with gradients and animations

## 📁 Project Structure

```
shopping_mall_ml_project/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── data/
│   ├── Mall_Customers.csv         # Customer data
│   ├── Market_Basket_Optimisation.csv  # Transaction data
│   └── Restaurant_Reviews.tsv     # Review data
└── models/
    ├── kmeans_model.pkl          # Customer segmentation model
    ├── apriori_rules.pkl         # Product recommendation rules
    ├── sentiment_model.pkl       # Sentiment analysis model
    └── vectorizer.pkl            # Text vectorizer
```

## 🎯 Usage Examples

### Customer Segmentation
1. Navigate to "👥 Customer Segmentation"
2. Enter customer's annual income and spending score
3. Click "🔍 Analyze Customer"
4. View the customer's segment and visualization

### Product Recommendation
1. Go to "🛒 Product Recommendation"
2. Select a product from the dropdown
3. Click "🎯 Get Recommendations"
4. See products frequently bought together

### Sentiment Analysis
1. Choose "💬 Review Sentiment Analysis"
2. Enter or paste a customer review
3. Click "🔍 Analyze Sentiment"
4. View sentiment result with confidence scores

## 🤝 Contributing

Feel free to fork this project and submit pull requests with improvements!

## 📄 License

This project is open source and available under the MIT License.

---

Built with ❤️ using Streamlit & Machine Learning