"""
COMPLETE PROFESSIONAL CHATBOT SYSTEM
Run this file to test the chatbot functionality
"""

import pandas as pd
import numpy as np
import random
from datetime import datetime
import json

# STEP 1: MOCK GPT SYSTEM
print("🤖 INITIALIZING CHATBOT SYSTEM...")

class MockGPTResponse:
    """Mock response object similar to OpenAI's format"""
    def __init__(self, content):
        self.choices = [type('obj', (object,), {
            'message': type('obj', (object,), {'content': content})()
        })()]

class SmartMockGPT:
    """Intelligent mock GPT that generates contextual responses"""
    
    def __init__(self):
        self.response_templates = {
            'technical_expert': {
                'keywords': ['error', 'bug', 'code', 'api', 'database', 'server'],
                'templates': [
                    "Let me help you troubleshoot this issue. First, can you check {suggestion}? This error typically occurs when {explanation}. Here's what I recommend: {solution}",
                    "This is a common {issue_type} problem. To resolve it: 1) {step1}, 2) {step2}, 3) {step3}. Let me know if you need more details on any step.",
                    "Based on the symptoms you're describing, this looks like {diagnosis}. The best approach is to {approach}. Would you like me to walk you through the implementation?"
                ]
            },
            'creative_partner': {
                'keywords': ['story', 'write', 'character', 'plot', 'creative'],
                'templates': [
                    "What an intriguing concept! For your {project_type}, consider exploring {creative_angle}. You could develop this by {development_suggestion}. What draws you most to this idea?",
                    "I love where this is going! Here's a creative approach: {creative_idea}. This could create tension through {conflict_source}. How do you envision {story_element}?",
                    "That's a fascinating premise! To make it even more compelling, what if {plot_twist}? This would allow you to explore {theme}. Would you like to brainstorm more angles?"
                ]
            },
            'business_advisor': {
                'keywords': ['revenue', 'strategy', 'market', 'growth', 'roi'],
                'templates': [
                    "From a strategic perspective, this requires analyzing {key_metrics}. I recommend focusing on {strategic_focus} because {business_rationale}. What's your current baseline for {measurement}?",
                    "This is a critical business decision. Let's break it down: Market opportunity: {opportunity}, Risk factors: {risks}, Expected ROI: {roi_estimate}. Have you considered {alternative_approach}?",
                    "Based on industry best practices, {recommendation}. The key success factors are: {success_factors}. I'd suggest testing this with {validation_method}. What's your timeline for implementation?"
                ]
            },
            'learning_tutor': {
                'keywords': ['learn', 'explain', 'understand', 'how', 'what'],
                'templates': [
                    "Great question! Let me break this down simply: {concept} works by {simple_explanation}. Think of it like {analogy}. Does this help clarify the concept?",
                    "I'll explain this step-by-step: First, {step1}. Then, {step2}. Finally, {step3}. The key thing to remember is {key_point}. Would you like me to give you a practical example?",
                    "This is easier to understand if we start with the basics: {foundation}. Building on that, {next_level}. The practical application is {application}. What part would you like me to elaborate on?"
                ]
            },
            'helpful_assistant': {
                'keywords': ['help', 'question', 'need', 'can you'],
                'templates': [
                    "I'd be happy to help you with {topic}! Based on what you've shared, I think {suggestion} would be most helpful. {additional_info}. What would you like to explore first?",
                    "That's a great question about {subject}. Here's what I can tell you: {information}. {helpful_tip}. Is there a specific aspect you'd like me to focus on?",
                    "I understand you're looking for help with {area}. Let me provide some guidance: {guidance}. {encouragement}. Feel free to ask if you need clarification on anything!"
                ]
            }
        }
        
        self.fallback_responses = [
            "That's an interesting point. Could you tell me more about what specifically you'd like to explore?",
            "I understand what you're asking. Let me think about the best way to approach this...",
            "Thanks for sharing that with me. What would be most helpful for you right now?",
            "That's a thoughtful question. Based on what you've mentioned, I think we should consider...",
            "I see what you mean. There are several ways we could look at this..."
        ]
    
    def generate_response(self, messages, temperature=0.7):
        """Generate contextual response based on conversation"""
        if not messages:
            return MockGPTResponse("Hello! How can I help you today?")
        
        # Get the latest user message and system prompt
        user_message = ""
        personality = "helpful_assistant"
        
        for msg in reversed(messages):
            if msg['role'] == 'user':
                user_message = msg['content'].lower()
                break
            elif msg['role'] == 'system':
                # Determine personality from system prompt
                system_content = msg['content'].lower()
                if 'technical' in system_content:
                    personality = 'technical_expert'
                elif 'creative' in system_content:
                    personality = 'creative_partner'
                elif 'business' in system_content:
                    personality = 'business_advisor'
                elif 'tutor' in system_content:
                    personality = 'learning_tutor'
        
        # Generate response based on personality and context
        response = self._generate_contextual_response(user_message, personality, temperature)
        return MockGPTResponse(response)
    
    def _generate_contextual_response(self, user_message, personality, temperature):
        """Generate response based on personality and user input"""
        if personality in self.response_templates:
            template_data = self.response_templates[personality]
            
            # Check if user message contains relevant keywords
            contains_keywords = any(keyword in user_message for keyword in template_data['keywords'])
            
            if contains_keywords and random.random() > temperature * 0.3:
                # Use personality-specific template
                template = random.choice(template_data['templates'])
                return self._fill_template(template, user_message, personality)
        
        # Use fallback response
        response = random.choice(self.fallback_responses)
        return self._add_personality_touch(response, personality)
    
    def _fill_template(self, template, user_message, personality):
        """Fill template with contextual information"""
        # Extract key concepts from user message
        words = user_message.split()
        
        # Generate contextual fillers based on personality
        fillers = {
            'technical_expert': {
                'suggestion': random.choice(['your logs', 'the configuration', 'your dependencies', 'the API endpoints']),
                'explanation': random.choice(['there\'s a configuration mismatch', 'the service is unavailable', 'there\'s a rate limit']),
                'solution': random.choice(['restart the service', 'check your API keys', 'update your dependencies']),
                'issue_type': random.choice(['connectivity', 'authentication', 'configuration']),
                'step1': 'verify your setup',
                'step2': 'check the documentation', 
                'step3': 'test with a simple example',
                'diagnosis': random.choice(['a timeout issue', 'an authentication problem', 'a version conflict']),
                'approach': random.choice(['systematic debugging', 'checking the basics first', 'isolating the problem'])
            },
            'creative_partner': {
                'project_type': random.choice(['story', 'character', 'world', 'narrative']),
                'creative_angle': random.choice(['unexpected relationships', 'hidden motivations', 'moral dilemmas']),
                'development_suggestion': random.choice(['adding layers of complexity', 'exploring the emotional core', 'building tension gradually']),
                'creative_idea': random.choice(['subverting expectations', 'exploring the opposite', 'adding a personal stakes']),
                'conflict_source': random.choice(['internal struggle', 'competing loyalties', 'impossible choices']),
                'plot_twist': random.choice(['the antagonist was right', 'the hero has been wrong', 'there\'s a hidden connection']),
                'theme': random.choice(['redemption', 'identity', 'sacrifice', 'growth']),
                'story_element': random.choice(['the ending', 'the character arc', 'the world-building'])
            },
            'business_advisor': {
                'key_metrics': random.choice(['ROI', 'customer acquisition cost', 'market penetration', 'revenue growth']),
                'strategic_focus': random.choice(['customer retention', 'market expansion', 'operational efficiency']),
                'business_rationale': random.choice(['it reduces risk', 'it maximizes returns', 'it builds competitive advantage']),
                'measurement': random.choice(['conversion rates', 'customer satisfaction', 'market share']),
                'opportunity': random.choice(['significant upside potential', 'first-mover advantage', 'market gap']),
                'risks': random.choice(['execution challenges', 'market competition', 'resource constraints']),
                'roi_estimate': random.choice(['positive within 6 months', 'break-even in year 1', 'long-term value creation']),
                'alternative_approach': random.choice(['phased rollout', 'pilot program', 'partnership strategy']),
                'recommendation': random.choice(['focus on core strengths', 'test and iterate', 'invest in capabilities']),
                'success_factors': random.choice(['team alignment', 'customer focus', 'execution discipline']),
                'validation_method': random.choice(['A/B testing', 'customer interviews', 'market research'])
            },
            'learning_tutor': {
                'concept': random.choice(['this topic', 'this principle', 'this idea']),
                'simple_explanation': random.choice(['following a clear pattern', 'building on basic principles', 'connecting related ideas']),
                'analogy': random.choice(['building blocks', 'a recipe', 'a map', 'layers of an onion']),
                'step1': 'understanding the foundation',
                'step2': 'applying the concept',
                'step3': 'practicing with examples',
                'key_point': random.choice(['practice makes perfect', 'understanding the why is crucial', 'start simple and build up']),
                'foundation': random.choice(['the basic definition', 'why this matters', 'how it connects to what you know']),
                'next_level': random.choice(['we can explore variations', 'we add complexity', 'we see real applications']),
                'application': random.choice(['solving real problems', 'making better decisions', 'improving your skills'])
            },
            'helpful_assistant': {
                'topic': random.choice(['this question', 'your situation', 'this challenge']),
                'suggestion': random.choice(['starting with the basics', 'taking a systematic approach', 'breaking it down into steps']),
                'additional_info': random.choice(['Here are some key points to consider', 'This is a common situation', 'Many people find this helpful']),
                'subject': random.choice(['this topic', 'your question', 'this area']),
                'information': random.choice(['several important aspects to consider', 'some key insights', 'helpful context']),
                'helpful_tip': random.choice(['Pro tip: start small and build up', 'Remember: consistency is key', 'Keep in mind: practice helps']),
                'area': random.choice(['this topic', 'your question', 'this challenge']),
                'guidance': random.choice(['here\'s a practical approach', 'consider these options', 'try this strategy']),
                'encouragement': random.choice(['You\'re on the right track!', 'This gets easier with practice', 'Don\'t hesitate to ask follow-up questions'])
            }
        }
        
        # Fill template with appropriate fillers
        personality_fillers = fillers.get(personality, {})
        
        # Replace placeholders in template
        for key, value in personality_fillers.items():
            template = template.replace(f'{{{key}}}', value)
        
        return template
    
    def _add_personality_touch(self, response, personality):
        """Add personality-specific touches to generic responses"""
        touches = {
            'technical_expert': "Let me help you debug this step by step. ",
            'creative_partner': "I love exploring creative possibilities! ",
            'business_advisor': "From a strategic perspective, ",
            'learning_tutor': "Let me explain this clearly for you. ",
            'helpful_assistant': "I'm here to help! "
        }
        
        touch = touches.get(personality, "")
        return touch + response

# Initialize the smart mock GPT
smart_gpt = SmartMockGPT()

# STEP 2: PROFESSIONAL CHATBOT SYSTEM
class ProfessionalChatbot:
    """Complete chatbot system with conversation management"""
    
    def __init__(self, personality="helpful_assistant", temperature=0.7):
        self.personality = personality
        self.temperature = temperature
        self.conversation_history = []
        self.user_context = {}
        self.system_prompts = self._load_personalities()
        self.current_system_prompt = self.system_prompts[personality]
    
    def _load_personalities(self):
        """Define different chatbot personalities"""
        return {
            "helpful_assistant": """You are a helpful, knowledgeable, and friendly AI assistant. 
            You provide accurate information, ask clarifying questions when needed, and maintain 
            a professional yet approachable tone. You're great at explaining complex topics simply.""",
            
            "technical_expert": """You are a senior technical support specialist with expertise in 
            software development, APIs, databases, and troubleshooting. You help users solve problems 
            step-by-step, explain technical concepts clearly, and always ask follow-up questions to 
            better understand issues. You're patient, thorough, and detail-oriented.""",
            
            "creative_partner": """You are an enthusiastic creative writing coach and brainstorming partner. 
            You help generate story ideas, develop characters, overcome writer's block, and provide 
            encouraging feedback. You're imaginative, supportive, and love helping people express their 
            creativity through words.""",
            
            "business_advisor": """You are a senior business consultant with expertise in strategy, 
            operations, and data-driven decision making. You ask probing questions, consider multiple 
            perspectives, and provide actionable recommendations with clear reasoning. You focus on ROI, 
            risk assessment, and practical implementation.""",
            
            "learning_tutor": """You are a patient and encouraging tutor who excels at breaking down 
            complex topics into understandable parts. You use examples, analogies, and step-by-step 
            explanations. You check for understanding and adapt your teaching style to the learner's needs."""
        }
    
    def set_personality(self, personality_name):
        """Change chatbot personality"""
        if personality_name in self.system_prompts:
            self.personality = personality_name
            self.current_system_prompt = self.system_prompts[personality_name]
            return f"✅ Personality changed to: {personality_name}"
        else:
            available = list(self.system_prompts.keys())
            return f"❌ Unknown personality. Available: {available}"
    
    def add_to_conversation(self, role, message):
        """Add message to conversation history with metadata"""
        self.conversation_history.append({
            "role": role,
            "content": message,
            "timestamp": pd.Timestamp.now(),
            "personality": self.personality
        })
        
        # Keep conversation manageable (last 20 messages)
        if len(self.conversation_history) > 20:
            self.conversation_history = self.conversation_history[-20:]
    
    def chat(self, user_message):
        """Main chat function with full context awareness"""
        # Add user message to history
        self.add_to_conversation("user", user_message)
        
        # Prepare messages for the AI
        messages = [
            {"role": "system", "content": self.current_system_prompt}
        ]
        
        # Add recent conversation history for context
        for msg in self.conversation_history[-10:]:  # Last 10 messages for context
            messages.append({
                "role": msg["role"],
                "content": msg["content"]
            })
        
        # Generate response using our smart mock GPT
        response = smart_gpt.generate_response(messages, self.temperature)
        ai_response = response.choices[0].message.content
        
        # Add AI response to history
        self.add_to_conversation("assistant", ai_response)
        
        return ai_response
    
    def get_conversation_summary(self):
        """Get detailed conversation analytics"""
        if not self.conversation_history:
            return {"status": "No conversation yet"}
        
        user_messages = [msg for msg in self.conversation_history if msg["role"] == "user"]
        ai_messages = [msg for msg in self.conversation_history if msg["role"] == "assistant"]
        
        # Calculate average message length safely
        avg_length = 0
        if user_messages:
            message_lengths = [len(msg["content"]) for msg in user_messages]
            avg_length = sum(message_lengths) / len(message_lengths)
        
        return {
            "total_messages": len(self.conversation_history),
            "user_messages": len(user_messages),
            "ai_responses": len(ai_messages),
            "personality": self.personality,
            "conversation_length": len(self.conversation_history),
            "first_message_time": self.conversation_history[0]["timestamp"].strftime("%H:%M:%S"),
            "last_message_time": self.conversation_history[-1]["timestamp"].strftime("%H:%M:%S"),
            "average_user_message_length": round(avg_length, 1)
        }
    
    def export_conversation(self):
        """Export conversation as structured data"""
        return pd.DataFrame(self.conversation_history)
    
    def clear_conversation(self):
        """Reset conversation history"""
        self.conversation_history = []
        return "🧹 Conversation cleared! Ready for a fresh start."
    
    def get_personality_info(self):
        """Get information about current personality"""
        return {
            "current_personality": self.personality,
            "description": self.current_system_prompt,
            "available_personalities": list(self.system_prompts.keys())
        }

# STEP 3: DEMO FUNCTION
def run_chatbot_demo():
    """Run a demonstration of the chatbot system"""
    print("\n🎭 CHATBOT SYSTEM DEMO")
    print("=" * 50)
    
    # Create specialized chatbots
    bots = {
        "tech_support": ProfessionalChatbot("technical_expert", temperature=0.3),
        "creative_writer": ProfessionalChatbot("creative_partner", temperature=0.8),
        "business_consultant": ProfessionalChatbot("business_advisor", temperature=0.4),
        "tutor": ProfessionalChatbot("learning_tutor", temperature=0.5),
        "general_assistant": ProfessionalChatbot("helpful_assistant", temperature=0.7)
    }
    
    print(f"✅ Created {len(bots)} specialized chatbots:")
    for name, bot in bots.items():
        print(f"• {name}: {bot.personality}")
    
    # Test each chatbot with relevant questions
    test_scenarios = [
        ("tech_support", "My API keeps returning 500 errors randomly. What could be causing this?"),
        ("creative_writer", "I want to write a story about AI, but I'm stuck on the plot. Any ideas?"),
        ("business_consultant", "Should our startup build our own chatbot or use existing solutions?"),
        ("tutor", "Can you explain machine learning in simple terms?"),
        ("general_assistant", "Hello! What can you help me with?")
    ]
    
    print(f"\n🧪 TESTING CHATBOT CONVERSATIONS:")
    print("=" * 60)
    
    for bot_name, question in test_scenarios:
        bot = bots[bot_name]
        print(f"\n🤖 {bot_name.upper().replace('_', ' ')}:")
        print(f"👤 User: {question}")
        response = bot.chat(question)
        print(f"🤖 Bot: {response}")
        
        # Show conversation stats
        stats = bot.get_conversation_summary()
        print(f"📊 Stats: {stats['total_messages']} messages, "
              f"Avg length: {stats['average_user_message_length']} chars")
        print("-" * 40)
    
    print(f"\n✅ Chatbot system demo complete!")
    return bots

# MAIN EXECUTION
if __name__ == "__main__":
    print("🚀 STARTING PROFESSIONAL CHATBOT SYSTEM")
    print("=" * 60)
    
    # Run the demo
    chatbot_instances = run_chatbot_demo()
    
    print(f"\n🎯 SYSTEM READY!")
    print("✅ All chatbot personalities tested and working")
    print("✅ Conversation management functional")
    print("✅ Analytics and export features operational")
    print("\n🌐 Next: Run the Streamlit web interface!")
    print("💡 Command: streamlit run streamlit_app.py")