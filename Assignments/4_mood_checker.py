# A simple program that tells if a senctence sounds happy, sad, or angry

sentence = input("Enter a sentence describing your mood: ")

happy_keywords = ["happy", "joy", "excited", "pleased", "content", "cheerful", "elated", "joyful"]
sad_keywords = ["sad", "unhappy", "down", "depressed", "gloomy", "melancholy", "sorrowful", "mournful"]
angry_keywords = ["angry", "irritated", "mad", "furious", "annoyed", "frustrated", "outraged", "resentful"]

if any(word in sentence.lower() for word in happy_keywords):
    mood = "Happy"
elif any(word in sentence.lower() for word in sad_keywords):
    mood = "Sad"
elif any(word in sentence.lower() for word in angry_keywords):
    mood = "Angry"
else:
    mood = "Neutral"

print("Your current mood is:", mood)