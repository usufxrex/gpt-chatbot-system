# INTERACTIVE DEMO SCRIPT FOR CHATBOT SYSTEM
import time
from chatbot_system import ProfessionalChatbot

def demo_conversation_flow():
    """Demonstrate a realistic conversation flow"""
    print("\n🎬 DEMO 1: REALISTIC CONVERSATION FLOW")
    print("-" * 40)
    
    # Create a business consultant bot
    business_bot = ProfessionalChatbot("business_advisor", temperature=0.4)
    
    # Simulate a realistic business conversation
    conversation_flow = [
        "Hi, I need help with my startup's pricing strategy.",
        "We're a SaaS company with 500 users paying $29/month.",
        "Our competitors charge $39-49/month. Should we raise prices?",
        "What metrics should I track to measure the impact?",
        "How do I communicate price changes to existing customers?"
    ]
    
    print("👤 Business Owner consulting with AI advisor:")
    print()
    
    for i, message in enumerate(conversation_flow, 1):
        print(f"👤 User {i}: {message}")
        
        # Simulate thinking time
        print("   🤖 [AI thinking...]", end="")
        for _ in range(3):
            time.sleep(0.3)
            print(".", end="", flush=True)
        print()
        
        response = business_bot.chat(message)
        print(f"🤖 AI: {response}")
        print()
        input("⏸️  Press Enter to continue...")
    
    # Show conversation analytics
    stats = business_bot.get_conversation_summary()
    print("📊 CONVERSATION ANALYTICS:")
    for key, value in stats.items():
        print(f"   • {key}: {value}")

def demo_personality_comparison():
    """Demonstrate how different personalities handle the same question"""
    print(f"\n🎭 DEMO 2: PERSONALITY COMPARISON")
    print("-" * 40)
    
    test_question = "How do I learn programming effectively?"
    
    # Create different personality bots
    personalities = {
        "🎓 Learning Tutor": ProfessionalChatbot("learning_tutor"),
        "🛠️ Tech Expert": ProfessionalChatbot("technical_expert"), 
        "💼 Business Advisor": ProfessionalChatbot("business_advisor"),
        "✍️ Creative Partner": ProfessionalChatbot("creative_partner")
    }
    
    print(f"❓ Question: '{test_question}'")
    print(f"🎯 Testing {len(personalities)} different AI personalities:\n")
    
    for name, bot in personalities.items():
        print(f"{name}:")
        response = bot.chat(test_question)
        # Show first 200 characters
        preview = response[:200] + "..." if len(response) > 200 else response
        print(f"   {preview}")
        print(f"   📏 Length: {len(response)} chars")
        print()
        input("⏸️  Press Enter for next personality...")

def demo_interactive_menu():
    """Interactive demo menu for user testing"""
    print(f"\n🎮 DEMO 3: INTERACTIVE TESTING MENU")
    print("-" * 40)
    
    # Create a general assistant
    assistant = ProfessionalChatbot("helpful_assistant")
    
    while True:
        print(f"\n🤖 CHATBOT TESTING MENU:")
        print("1. 💬 Chat with AI")
        print("2. 🎭 Change personality") 
        print("3. 📊 View stats")
        print("4. 🧹 Clear conversation")
        print("5. 🚪 Exit demo")
        
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == "1":
            message = input("👤 Your message: ")
            if message:
                print("🤖 AI:", assistant.chat(message))
        
        elif choice == "2":
            personalities = list(assistant.system_prompts.keys())
            print("Available personalities:")
            for i, p in enumerate(personalities, 1):
                print(f"   {i}. {p}")
            
            try:
                p_choice = int(input("Choose personality (number): ")) - 1
                if 0 <= p_choice < len(personalities):
                    result = assistant.set_personality(personalities[p_choice])
                    print(result)
            except ValueError:
                print("❌ Invalid choice")
        
        elif choice == "3":
            stats = assistant.get_conversation_summary()
            print("📊 Conversation Statistics:")
            for key, value in stats.items():
                print(f"   • {key}: {value}")
        
        elif choice == "4":
            result = assistant.clear_conversation()
            print(result)
        
        elif choice == "5":
            print("👋 Thanks for testing the chatbot system!")
            break
        
        else:
            print("❌ Invalid choice. Please enter 1-5.")

def main_demo():
    """Run complete demonstration"""
    print("🎉 WELCOME TO THE PROFESSIONAL CHATBOT SYSTEM DEMO!")
    print("🎯 Showcasing advanced conversational AI capabilities")
    print()
    
    demos = [
        ("Business Conversation Flow", demo_conversation_flow),
        ("Personality Comparison", demo_personality_comparison),
        ("Interactive Menu", demo_interactive_menu)
    ]
    
    print("📋 Available Demos:")
    for i, (name, _) in enumerate(demos, 1):
        print(f"   {i}. {name}")
    
    print("\n🚀 Starting demo sequence...")
    
    # Run demos
    for i, (name, demo_func) in enumerate(demos, 1):
        print(f"\n{'='*60}")
        print(f"🎬 DEMO {i}: {name}")
        print(f"{'='*60}")
        
        run_demo = input(f"Run this demo? (y/n): ").lower()
        if run_demo.startswith('y'):
            demo_func()
        
        if i < len(demos):
            input(f"\n⏸️  Press Enter to continue to next demo...")
    
    print(f"\n🎊 DEMO COMPLETE!")
    print("✅ Professional Chatbot System fully functional!")
    print("🌐 Web interface ready for deployment!")
    print("🚀 Ready for production use!")

# Run the demo
if __name__ == "__main__":
    main_demo()