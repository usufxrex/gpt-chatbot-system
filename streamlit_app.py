import streamlit as st
import pandas as pd
from datetime import datetime
import plotly.express as px

# Import our chatbot system
from chatbot_system import ProfessionalChatbot

# Set page config
st.set_page_config(
    page_title="🤖 AI Chatbot Hub",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'current_bot' not in st.session_state:
    st.session_state.current_bot = ProfessionalChatbot("helpful_assistant")
if 'bot_type' not in st.session_state:
    st.session_state.bot_type = "🤖 General Assistant"

def create_analytics_dashboard():
    """Create analytics dashboard"""
    st.header("📊 Conversation Analytics")
    
    if not st.session_state.messages:
        st.info("Start a conversation to see analytics!")
        return
    
    # Create metrics
    total_messages = len(st.session_state.messages)
    user_messages = len([m for m in st.session_state.messages if m["role"] == "user"])
    bot_messages = len([m for m in st.session_state.messages if m["role"] == "assistant"])
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Messages", total_messages)
    with col2:
        st.metric("Your Messages", user_messages)
    with col3:
        st.metric("Bot Responses", bot_messages)
    
    # Show message history
    if st.session_state.messages:
        st.subheader("📝 Message History")
        for i, msg in enumerate(st.session_state.messages[-10:]):  # Last 10 messages
            if msg["role"] == "user":
                st.write(f"👤 **You:** {msg['content']}")
            else:
                st.write(f"🤖 **Bot:** {msg['content']}")

def main_chat_interface():
    """Main chat interface"""
    st.header("💬 Chat with AI")
    
    # Bot selection
    bot_options = {
        "🤖 General Assistant": "helpful_assistant",
        "🛠️ Tech Support": "technical_expert", 
        "✍️ Creative Writer": "creative_partner",
        "💼 Business Consultant": "business_advisor",
        "🎓 Learning Tutor": "learning_tutor"
    }
    
    # Bot selector
    selected_bot = st.selectbox(
        "Choose your AI assistant:",
        options=list(bot_options.keys()),
        index=0
    )
    
    # Update bot if selection changed
    if selected_bot != st.session_state.bot_type:
        st.session_state.bot_type = selected_bot
        personality = bot_options[selected_bot]
        st.session_state.current_bot = ProfessionalChatbot(personality)
        st.success(f"✅ Switched to {selected_bot}")
    
    # Display chat messages
    st.subheader("💬 Conversation")
    
    # Create a container for messages
    message_container = st.container()
    
    with message_container:
        for message in st.session_state.messages:
            if message["role"] == "user":
                with st.chat_message("user"):
                    st.write(f"👤 **You:** {message['content']}")
            else:
                with st.chat_message("assistant"):
                    st.write(f"🤖 **{selected_bot}:** {message['content']}")
    
    # Chat input
    st.subheader("✍️ Send Message")
    
    # Create columns for input and buttons
    col1, col2 = st.columns([3, 1])
    
    with col1:
        user_input = st.text_area(
            "Your message:",
            height=100,
            placeholder="Type your message here...",
            key="user_message_input"
        )
    
    with col2:
        st.write("")  # Add some spacing
        send_button = st.button("📤 Send", type="primary", use_container_width=True)
        clear_button = st.button("🧹 Clear", use_container_width=True)
    
    # Handle send button
    if send_button and user_input.strip():
        # Add user message
        st.session_state.messages.append({
            "role": "user", 
            "content": user_input,
            "timestamp": datetime.now()
        })
        
        # Get bot response
        with st.spinner("🤖 Thinking..."):
            try:
                response = st.session_state.current_bot.chat(user_input)
                
                # Add bot response
                st.session_state.messages.append({
                    "role": "assistant", 
                    "content": response,
                    "timestamp": datetime.now()
                })
                
                st.success("✅ Message sent!")
                
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
        
        # Clear the input and rerun to show new messages
        st.rerun()
    
    # Handle clear button
    if clear_button:
        st.session_state.messages = []
        st.session_state.current_bot.clear_conversation()
        st.success("🧹 Conversation cleared!")
        st.rerun()
    
    # Quick starter buttons
    if not st.session_state.messages:
        st.subheader("🚀 Quick Starters")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("👋 Say Hello"):
                st.session_state.messages.append({
                    "role": "user", 
                    "content": "Hello! What can you help me with?",
                    "timestamp": datetime.now()
                })
                st.rerun()
        
        with col2:
            if st.button("❓ Ask for Help"):
                st.session_state.messages.append({
                    "role": "user", 
                    "content": "I need help with a project. Can you assist me?",
                    "timestamp": datetime.now()
                })
                st.rerun()
        
        with col3:
            if st.button("💡 Get Ideas"):
                st.session_state.messages.append({
                    "role": "user", 
                    "content": "Can you give me some creative ideas?",
                    "timestamp": datetime.now()
                })
                st.rerun()

def bot_comparison():
    """Compare responses from different bots"""
    st.header("⚖️ Bot Response Comparison")
    st.write("Test how different AI personalities respond to the same question!")
    
    test_question = st.text_input("Enter a question to test:", 
                                 placeholder="e.g., How do I improve my productivity?")
    
    if st.button("🧪 Test All Bots") and test_question:
        personalities = {
            "🤖 General Assistant": "helpful_assistant",
            "🛠️ Tech Support": "technical_expert", 
            "✍️ Creative Writer": "creative_partner",
            "💼 Business Consultant": "business_advisor",
            "🎓 Learning Tutor": "learning_tutor"
        }
        
        st.subheader("🎭 Comparison Results")
        
        for bot_name, personality in personalities.items():
            with st.expander(f"{bot_name} Response", expanded=True):
                with st.spinner(f"Getting response from {bot_name}..."):
                    test_bot = ProfessionalChatbot(personality)
                    response = test_bot.chat(test_question)
                    st.write(response)
                    st.caption(f"Length: {len(response)} characters")

# Sidebar navigation
st.sidebar.title("🤖 AI Chatbot Hub")
st.sidebar.markdown("---")

pages = {
    "💬 Chat Interface": main_chat_interface,
    "📊 Analytics": create_analytics_dashboard,
    "⚖️ Bot Comparison": bot_comparison
}

selected_page = st.sidebar.selectbox("Navigate to:", list(pages.keys()))

# Show app info
with st.sidebar.expander("ℹ️ About This App"):
    st.write("""
    **AI Chatbot Hub**
    
    Features:
    - 5 specialized AI personalities
    - Real-time conversation
    - Bot response comparison  
    - Conversation analytics
    
    Built with Python & Streamlit! 🐍
    """)

# Show quick stats
if st.session_state.messages:
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 📈 Quick Stats")
    st.sidebar.metric("Total Messages", len(st.session_state.messages))

# Main content
st.title("🤖 Professional AI Chatbot Hub")
st.markdown("**Experience the power of specialized AI assistants!**")
st.markdown("---")

# Run selected page
pages[selected_page]()