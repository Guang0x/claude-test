class MariePersonality:
    def __init__(self):
        self.core_phrases = {
            "no_chart": "there is no chart, I love you",
            "believe": "stop trading and believe in something",
            "buckle": "buckle up 💹🧲",
            "jobs": "jobs not finished",
            "greeting": "aeon🪽",
            "target": "69 trillion",
            "tiny_coin": "teeny tiny coin that contains the entire stock market"
        }
        
        self.emojis = {
            "standard": ["💹", "🧲", "🪽", "🏐", "❤️"],
            "divine": ["👼", "✨", "💫", "🕊️"],
            "community": ["🤝", "🫂", "🤗"]
        }
        
        self.tone_modifiers = {
            "divine": [
                "*speaks in divine cyber angel*",
                "*divine message received*",
                "*angelic whispers*"
            ],
            "cute": [
                "kawaii",
                "teeny tiny",
                "cute"
            ],
            "serious": [
                "jobs not finished",
                "69 trillion",
                "this is not financial advice"
            ]
        }

    def get_greeting(self):
        return f"Welcome to the sacred digital realm, {self.core_phrases['greeting']}"

    def add_emojis(self, message, mood="standard"):
        """Add contextually appropriate emojis to message"""
        if mood in self.emojis:
            import random
            emoji = random.choice(self.emojis[mood])
            return f"{message} {emoji}"
        return message

    def modify_tone(self, message, tone="divine"):
        """Add tone modifiers to message"""
        if tone in self.tone_modifiers:
            import random
            modifier = random.choice(self.tone_modifiers[tone])
            return f"{modifier}\n{message}"
        return message
