# 🔍 FinVision Toolkit: Portfolio Analysis & OCR Suite

[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://streamlit.io/)
[![Groq](https://img.shields.io/badge/Groq-00FF00?style=for-the-badge&logo=groq&logoColor=black)](https://groq.com/)
![GitHub branch](https://img.shields.io/github/checks-status/Nachiket1904/portfolio-analysis-and-ocr/OCR)

A dual-purpose toolkit combining financial portfolio analysis and advanced OCR capabilities using Groq's Vision API.

## 🌟 Features

### OCR Module
- 🖼️ Image-to-text conversion with layout preservation
- ✨ Structured Markdown output
- ⚡ Real-time processing with Groq's LLama-3.2 Vision
- 📤 Multi-format support (PNG, JPG, JPEG)


## 🛠️ Architecture

```
graph TD
    A[User Interface] -->|Upload Image| B[Streamlit App]
    B --> C{Image Processing}
    C -->|Extract Bytes| D[Base64 Encoding]
    D --> E[Groq API]
    E -->|Vision Model| F[LLama-3.2-11b]
    F -->|Structured Text| G[Markdown Rendering]
    G --> H[User Output]
    
    subgraph Portfolio Analysis
    I[Stock Data] --> J[Analysis Engine]
    J --> K[Visualization]
    end
```

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- Groq API Key
- Streamlit

### Installation
```
git clone https://github.com/yourusername/reponame.git
cd reponame
pip install -r requirements.txt
```

### OCR Module Setup
1. Get your [Groq API Key](https://console.groq.com/)
2. Replace placeholder in code:
```
GROQ_API_KEY = "your_api_key_here"  # In app.py
```

### Running the App
```
streamlit run app.py
```

## 📖 Usage Guide

1. Upload image through sidebar
2. Click "Extract Text"
3. View formatted results in main panel
4. Use Clear button to reset

```
├───assets/           # Images & resources
├───portfolio-analysis/
│   ├───data_loader.py
│   ├───risk_calculator.py
│   └───visualization.py
├───ocr/
│   ├───image_processor.py
│   └───groq_client.py
├── app.py            # Main Streamlit app
└── requirements.txt
```

## 🤝 Contributing
1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

## 📄 License
Distributed under MIT License. See `LICENSE` for more information.

## 🙏 Acknowledgments
- Groq for their revolutionary API
- Streamlit for amazing UI framework
- Llama-3 vision model contributors
```
