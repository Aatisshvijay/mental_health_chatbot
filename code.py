import re
import random
import datetime
from typing import Dict, List, Tuple
import json


class MentalHealthChatbot:
    def __init__(self):
        self.user_name = ""
        self.conversation_history = []
        self.mood_scores = []
        self.session_start = datetime.datetime.now()

        # Emotional keywords and their categories
        self.emotion_keywords = {
            'anxiety': ['anxious', 'worried', 'nervous', 'panic', 'fear', 'scared', 'overwhelmed'],
            'depression': ['sad', 'depressed', 'hopeless', 'empty', 'worthless', 'lonely', 'down'],
            'stress': ['stressed', 'pressure', 'burden', 'exhausted', 'tired', 'overworked'],
            'anger': ['angry', 'frustrated', 'irritated', 'mad', 'furious', 'annoyed'],
            'positive': ['happy', 'good', 'great', 'excited', 'joyful', 'content', 'peaceful']
        }

        # Response templates for different emotional states
        self.responses = {
            'anxiety': [
                "I understand you're feeling anxious. That's a very real and valid feeling. Have you tried any breathing exercises?",
                "Anxiety can be overwhelming. Remember, you're safe right now. What's one thing you can see, hear, and feel around you?",
                "I hear that you're worried. It's okay to feel this way. Would it help to talk about what's causing these feelings?"
            ],
            'depression': [
                "I'm sorry you're going through this difficult time. Your feelings are valid, and you don't have to face this alone.",
                "Depression can make everything feel harder. You're brave for reaching out. What's one small thing that brought you even a tiny bit of comfort recently?",
                "I want you to know that what you're feeling is real, and it's not your fault. Have you been able to talk to anyone else about how you're feeling?"
            ],
            'stress': [
                "Stress can be really challenging to deal with. You're doing your best, and that matters.",
                "It sounds like you have a lot on your plate. What's the most pressing thing you're dealing with right now?",
                "I can hear the pressure you're under. Sometimes breaking things down into smaller steps can help. What feels most manageable to tackle first?"
            ],
            'anger': [
                "It's completely normal to feel angry sometimes. Your emotions are valid. What's been triggering these feelings?",
                "I can sense your frustration. Anger often tells us something important. What do you think might be underneath this feeling?",
                "Thank you for sharing these difficult feelings with me. What usually helps you when you're feeling this way?"
            ],
            'positive': [
                "I'm so glad to hear you're feeling good! What's been going well for you?",
                "That's wonderful to hear! It's important to acknowledge and celebrate these positive moments.",
                "I love hearing about the good things in your life. What's contributing to these positive feelings?"
            ],
            'general': [
                "Thank you for sharing that with me. How are you feeling right now in this moment?",
                "I'm here to listen. What's been on your mind lately?",
                "It takes courage to talk about our feelings. What would be most helpful for you right now?"
            ]
        }

        # Coping strategies
        self.coping_strategies = {
            'anxiety': [
                "Try the 4-7-8 breathing technique: Breathe in for 4, hold for 7, exhale for 8.",
                "Practice grounding: Name 5 things you can see, 4 you can touch, 3 you can hear, 2 you can smell, 1 you can taste.",
                "Progressive muscle relaxation: Tense and release each muscle group starting from your toes."
            ],
            'depression': [
                "Try to maintain a daily routine, even if it's simple.",
                "Spend a few minutes outside or near a window for natural light.",
                "Reach out to one person you trust, even if it's just a text message."
            ],
            'stress': [
                "Break large tasks into smaller, manageable steps.",
                "Practice the 'two-minute rule': If something takes less than 2 minutes, do it now.",
                "Set boundaries and learn to say no to additional commitments when possible."
            ],
            'general': [
                "Regular sleep schedule can significantly impact mental health.",
                "Physical exercise, even a short walk, can boost mood.",
                "Journaling can help process thoughts and emotions."
            ]
        }

        # Crisis keywords that need immediate attention
        self.crisis_keywords = ['suicide', 'kill myself', 'end it all', 'not worth living', 'hurt myself']

    def detect_emotion(self, text: str) -> str:
        """Detect the primary emotion in user input"""
        text_lower = text.lower()
        emotion_scores = {}

        for emotion, keywords in self.emotion_keywords.items():
            score = sum(1 for keyword in keywords if keyword in text_lower)
            if score > 0:
                emotion_scores[emotion] = score

        if emotion_scores:
            return max(emotion_scores, key=emotion_scores.get)
        return 'general'

    def check_crisis(self, text: str) -> bool:
        """Check if user input contains crisis-related keywords"""
        text_lower = text.lower()
        return any(keyword in text_lower for keyword in self.crisis_keywords)

    def get_mood_score(self) -> int:
        """Ask user to rate their mood on a scale of 1-10"""
        try:
            print("\nOn a scale of 1-10, how would you rate your current mood?")
            print("(1 = Very low, 10 = Excellent)")
            score = int(input("Your mood score: "))
            if 1 <= score <= 10:
                self.mood_scores.append(score)
                return score
            else:
                print("Please enter a number between 1 and 10.")
                return self.get_mood_score()
        except ValueError:
            print("Please enter a valid number.")
            return self.get_mood_score()

    def provide_crisis_support(self) -> str:
        """Provide crisis support information"""
        return """
I'm concerned about what you've shared. Your life has value, and there are people who want to help.

🆘 IMMEDIATE HELP:
• National Suicide Prevention Lifeline: 988 (US)
• Crisis Text Line: Text HOME to 741741
• International: befrienders.org

Please reach out to a mental health professional, trusted friend, or family member right now. 
You don't have to go through this alone.

Would you like to talk about what's bringing up these feelings?
"""

    def generate_response(self, user_input: str) -> str:
        """Generate an appropriate response based on user input"""
        # Check for crisis situations first
        if self.check_crisis(user_input):
            return self.provide_crisis_support()

        # Detect emotion and generate response
        emotion = self.detect_emotion(user_input)

        # Get appropriate response
        if emotion in self.responses:
            response = random.choice(self.responses[emotion])
        else:
            response = random.choice(self.responses['general'])

        return response

    def suggest_coping_strategy(self, emotion: str = 'general') -> str:
        """Suggest a coping strategy based on detected emotion"""
        if emotion in self.coping_strategies:
            strategy = random.choice(self.coping_strategies[emotion])
        else:
            strategy = random.choice(self.coping_strategies['general'])

        return f"\n💡 Coping Strategy: {strategy}"

    def mood_check_in(self) -> str:
        """Perform a mood check-in"""
        current_score = self.get_mood_score()

        if current_score <= 3:
            return f"""
Thank you for sharing. A score of {current_score} suggests you're having a really tough time. 
That takes courage to acknowledge. Remember, it's okay to not be okay, and these feelings can change.

{self.suggest_coping_strategy('depression')}

Have you been able to talk to anyone else about how you're feeling?
"""
        elif current_score <= 6:
            return f"""
I hear you. A {current_score} suggests you're going through some challenges right now. 
Your feelings are valid, and I'm here to listen.

{self.suggest_coping_strategy()}

What's been the most difficult part of your day?
"""
        else:
            return f"""
I'm glad to hear you're feeling relatively good with a score of {current_score}! 
It's wonderful when we can recognize positive moments.

What's been going well for you lately?
"""

    def end_session_summary(self) -> str:
        """Provide a session summary"""
        session_duration = datetime.datetime.now() - self.session_start
        minutes = int(session_duration.total_seconds() / 60)

        summary = f"""
📋 Session Summary:
• Duration: {minutes} minutes
• Messages exchanged: {len(self.conversation_history)}
"""

        if self.mood_scores:
            avg_mood = sum(self.mood_scores) / len(self.mood_scores)
            summary += f"• Average mood score: {avg_mood:.1f}/10\n"

        summary += """
🌟 Remember:
• Your feelings are valid
• It's okay to ask for help
• Small steps count
• You're not alone in this journey

Take care of yourself! 💙
"""
        return summary

    def chat(self):
        """Main chat loop"""
        print("🤖 Mental Health Support Chatbot")
        print("=" * 40)
        print("Hello! I'm here to listen and provide support.")
        print("You can talk to me about anything on your mind.")
        print("Type 'mood' for a mood check-in, 'strategy' for coping tips, or 'quit' to end.\n")

        # Get user's name
        self.user_name = input("What would you like me to call you? ").strip()
        if self.user_name:
            print(f"\nNice to meet you, {self.user_name}! How are you feeling today?")
        else:
            print("\nHow are you feeling today?")

        while True:
            user_input = input(f"\n{self.user_name or 'You'}: ").strip()

            if not user_input:
                continue

            if user_input.lower() in ['quit', 'exit', 'bye', 'goodbye']:
                print(f"\nBot: Take care, {self.user_name}! Remember, I'm here whenever you need support.")
                print(self.end_session_summary())
                break
            elif user_input.lower() == 'mood':
                response = self.mood_check_in()
                print(f"\nBot: {response}")
            elif user_input.lower() == 'strategy':
                emotion = 'general'
                if self.conversation_history:
                    # Use the most recent emotion context
                    emotion = self.detect_emotion(self.conversation_history[-1])
                strategy = self.suggest_coping_strategy(emotion)
                print(f"\nBot: Here's a coping strategy for you:{strategy}")
            else:
                # Store conversation
                self.conversation_history.append(user_input)

                # Generate response
                response = self.generate_response(user_input)

                # Add coping strategy suggestion for negative emotions
                emotion = self.detect_emotion(user_input)
                if emotion in ['anxiety', 'depression', 'stress', 'anger']:
                    response += self.suggest_coping_strategy(emotion)

                print(f"\nBot: {response}")


# Run the chatbot
if __name__ == "__main__":
    chatbot = MentalHealthChatbot()
    try:
        chatbot.chat()
    except KeyboardInterrupt:
        print(f"\n\nBot: I understand you need to go. Take care of yourself! 💙")
        if chatbot.user_name:
            print(f"Goodbye, {chatbot.user_name}.")
    except Exception as e:
        print(f"\nBot: I'm sorry, something went wrong. Please remember that if you're in crisis, help is available.")
        print("National Suicide Prevention Lifeline: 988")
