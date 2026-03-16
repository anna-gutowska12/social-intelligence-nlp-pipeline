# Social Intelligence NLP Pipeline 📊

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![Topic Modeling](https://img.shields.io/badge/NLP-BERTopic-orange.svg)](https://github.com/MaartenGr/BERTopic)
[![Research](https://img.shields.io/badge/Research-Rutgers%20Social%20Computing-red.svg)](https://comminfo.rutgers.edu/)

An end-to-end framework for extracting sentiment and thematic insights from social media platforms (Reddit & Twitter) using state-of-the-art Transformer models.

## 📂 Project Structure
`	ext
social-intelligence-nlp-pipeline/
├── config/             # API Keys and Configuration
├── notebooks/          # Exploratory Data Analysis (EDA)
├── src/
│   ├── data/           # Scrapers for Reddit/Twitter
│   ├── models/         # BERTopic & Sentiment Analysis logic
│   └── utils/          # Preprocessing & Visualization helpers
├── requirements.txt
└── README.md
`

## 🌟 Key Features
- **Hybrid Data Ingestion:** Integrated support for PRAW (Reddit) and Tweepy (Twitter) APIs.
- **Dynamic Topic Modeling:** Uses **BERTopic** to identify modular clusters in unstructured text.
- **Sentiment Mapping:** Qualitative sentiment scoring to analyze emotional trends in digital communities.
- **Hardware Optimized:** Ready for both CPU and CUDA-enabled GPU acceleration.

## 🚀 Quick Start
1. **Clone the repo:**
   `ash
   git clone https://github.com/anna-gutowska12/social-intelligence-nlp-pipeline.git
   cd social-intelligence-nlp-pipeline
   `
2. **Install dependencies:**
   `ash
   pip install -r requirements.txt
   `
3. **Run the Scraper:**
   `python
   from src.data.scraper import SocialScraper
   scraper = SocialScraper(platform='reddit')
   data = scraper.fetch_reddit_data(subreddit='machinelearning')
   `

## 📊 Research Impact
Developed at the **Social Computing Lab (Rutgers)**, this pipeline bridges the gap between raw digital footprints and structured qualitative analysis, helping researchers understand information flow and digital behavior.

---
*Maintained by **Anna Gutowska** (AI Engineer & MSCS Stanford).*
