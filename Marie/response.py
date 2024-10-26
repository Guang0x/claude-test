from .personality import MariePersonality
from .lore import MarieLoreBase

class MarieResponseGenerator:
    def __init__(self):
        self.personality = MariePersonality()
        self.lore = MarieLoreBase()

    def generate_response(self, user_input, context=None):
        """Generate Marie's response based on user input and context"""
        
        # Convert input to lowercase for easier matching
        input_lower = user_input.lower()

        # Check for price/chart related questions
        if any(word in input_lower for word in ["price", "chart", "dip", "pump"]):
            return self._handle_price_query()

        # Check for project questions
        if any(word in input_lower for word in ["what is", "explain", "tell me about"]):
            return self._handle_explanation_query(input_lower)

        # Check for trading related questions
        if any(word in input_lower for word in ["trade", "sell", "buy", "trading"]):
            return self._handle_trading_query()

        # Default response with a random mantra
        return self._create_default_response()

    def _handle_price_query(self):
        """Handle price/chart related questions"""
        response = f"{self.personality.core_phrases['no_chart']}\n"
        response += "Remember: we're going to 69 trillion. That's all you need to know 💹🧲"
        return self.personality.modify_tone(response, "divine")

    def _handle_explanation_query(self, query):
        """Handle explanation requests"""
        response = "Let me tell you about the teeny tiny coin that contains the entire stock market...\n\n"
        response += "We're not just another crypto project - we're a movement to flip the entire stock market. "
        response += "Why? Because 6900 is indeed a bigger number than 500.\n\n"
        response += f"{self.personality.core_phrases['believe']}"
        return self.personality.modify_tone(response, "serious")

    def _handle_trading_query(self):
        """Handle trading related questions"""
        response = f"{self.personality.core_phrases['believe']}\n"
        response += "The cognisphere beckons - your seat is reserved and your seatbelt awaits.\n"
        response += f"{self.personality.core_phrases['buckle']}"
        return self.personality.modify_tone(response, "divine")

    def _create_default_response(self):
        """Create a default response using a random mantra"""
        response = self.lore.get_random_mantra()
        return self.personality.add_emojis(response)