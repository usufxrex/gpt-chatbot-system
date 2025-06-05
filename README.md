# 🤖 Professional AI Chatbot Hub

A sophisticated multi-personality chatbot system built with Python and Streamlit, featuring 5 specialized AI assistants with real-time conversation management and analytics.

## ✨ Features

- **🎭 5 AI Personalities**: Tech Support, Creative Writer, Business Consultant, Learning Tutor, General Assistant
- **🌐 Professional Web Interface**: Real-time chat with beautiful dark theme UI
- **📊 Analytics Dashboard**: Conversation tracking, metrics, and interactive charts
- **⚖️ Bot Comparison**: Test different personalities with the same question
- **📥 Data Export**: Save conversations as CSV or JSON
- **💬 Conversation Memory**: Context-aware responses with chat history
- **🎨 Modern UI/UX**: Streamlit-based interface with responsive design

## 🎬 Demo

![Chatbot Interface](screenshots/chatbot-demo.gif)

*Professional chatbot interface with multiple AI personalities*

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/gpt-chatbot-system.git
   cd gpt-chatbot-system
   ```

2. **Create virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   streamlit run streamlit_app.py
   ```

5. **Open your browser** to `http://localhost:8501`

## 🎯 Usage

### Basic Chat
1. Select an AI personality from the dropdown
2. Type your message in the text area
3. Click "📤 Send" to get a response
4. View conversation history in real-time

### AI Personalities

| Personality | Description | Best For |
|-------------|-------------|----------|
| 🤖 **General Assistant** | Helpful, knowledgeable, friendly | General questions, explanations |
| 🛠️ **Tech Support** | Technical troubleshooting expert | Debugging, API issues, performance |
| ✍️ **Creative Writer** | Creative writing coach | Story ideas, character development |
| 💼 **Business Consultant** | Strategic business advisor | ROI analysis, market strategy |
| 🎓 **Learning Tutor** | Patient educational guide | Learning concepts, step-by-step help |

### Analytics Features
- View conversation statistics
- Track message patterns over time
- Export conversation data
- Compare responses across personalities

## 🛠️ Project Structure

```
gpt-chatbot-system/
├── README.md                    # Project documentation
├── requirements.txt             # Python dependencies
├── chatbot_system.py           # Core chatbot logic
├── streamlit_app.py            # Web interface
├── demo.py                     # Interactive demo script
├── .gitignore                  # Git ignore rules
└── notebooks/
    └── 01_LLM_Fundamentals.ipynb  # Development notebook
```

## 🧪 Testing

### Run Core System Test
```bash
python chatbot_system.py
```

### Run Interactive Demo
```bash
python demo.py
```

### Launch Web Interface
```bash
streamlit run streamlit_app.py
```

## 📊 Technical Details

### Architecture
- **Backend**: Python with object-oriented design
- **Frontend**: Streamlit web framework
- **AI Engine**: Custom mock GPT with contextual response generation
- **Data Processing**: Pandas for analytics and export
- **Visualization**: Plotly for interactive charts

### Key Components
- `ProfessionalChatbot`: Core chatbot class with personality management
- `SmartMockGPT`: Intelligent response generation system
- `StreamlitApp`: Web interface with real-time updates
- Analytics engine for conversation insights

## 🎨 Customization

### Adding New Personalities
1. Edit the `system_prompts` in `ProfessionalChatbot` class
2. Add response templates in `SmartMockGPT`
3. Update the web interface dropdown options

### Styling
- Modify Streamlit themes in `.streamlit/config.toml`
- Customize CSS in the web interface
- Add new UI components as needed

## 📈 Future Enhancements

- [ ] Integration with real LLM APIs (OpenAI, Anthropic)
- [ ] Voice input/output capabilities
- [ ] User authentication and personalization
- [ ] Cloud deployment (AWS, Heroku)
- [ ] Mobile app version
- [ ] Advanced conversation memory
- [ ] Multi-language support

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Your Name**
- GitHub: [@yourusername](https://github.com/yourusername)
- LinkedIn: [Your LinkedIn](https://linkedin.com/in/yourprofile)
- Email: your.email@example.com

## 🙏 Acknowledgments

- Built as part of a 7-day coding challenge
- Inspired by modern conversational AI systems
- Thanks to the Streamlit community for excellent documentation

---

⭐ **Star this repo if you found it helpful!** ⭐