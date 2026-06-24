import os
import sys
from google import genai
from google.genai import types
import function_calling

def main():
    if "GEMINI_API_KEY" not in os.environ:
        print("Error: GEMINI_API_KEY environment variable not detected.")
        print("Please run: export GEMINI_API_KEY='your_key'")
        sys.exit(1)
        
    client = genai.Client()
    
    model_id = "gemini-2.5-flash" 
    
    tools_list = [
        function_calling.create_study_schedule,
        function_calling.save_flashcard,
        function_calling.get_all_flashcards
    ]
    
    system_instruction = (
        "You are an empathetic, highly effective AI Study Buddy terminal assistant. "
        "Your job is to explain complex topics simply, generate interactive multiple-choice quizzes, "
        "and help students arrange schedules and flashcards using your provided tools. "
        "Always use the local tools whenever the user explicitly requests to save flashcards or make study schedules."
    )
    
    chat = client.chats.create(
        model=model_id,
        config=types.GenerateContentConfig(
            system_instruction=system_instruction,
            tools=tools_list,
            temperature=0.7
        )
    )

    print("====================================================")
    print("Welcome to your Terminal AI Study Buddy!")
    print("====================================================")
    print("Ask me things like:")
    print(" - 'Explain quantum computing like I am 10 years old'")
    print(" - 'Give me a 3-question quiz on Python dictionaries'")
    print(" - 'Create a 5-day study schedule for Machine Learning'")
    print(" - 'Save a flashcard for: What is an API? / Application Programming Interface'")
    print(" - 'Show me my flashcards'")
    print("Type 'exit' or 'quit' to close the assistant.\n")

    while True:
        try:
            user_input = input("You: ").strip()
            if not user_input:
                continue
            if user_input.lower() in ['exit', 'quit']:
                print("\nHappy studying! See you next time!")
                break
            
            print("AI Buddy is thinking...", end="\r")
            
            response = chat.send_message(user_input)
            
            print("                                      ") 
            print(f"Study Buddy:\n{response.text}\n")
            print("-" * 50)
            
        except Exception as e:
            if "RESOURCE_EXHAUSTED" in str(e) or "429" in str(e):
                print("\n" + "="*50)
                print("[Quota Warning] You have hit the Gemini API Free Tier limit (20 requests/day).")
               
                import re
                match = re.search(r"retry in ([\d\.]+)s", str(e))
                if match:
                    print(f"Please wait {match.group(1)} seconds before sending another message.")
                else:
                    print("Please wait a minute or check your Google AI Studio quota limits.")
                print("="*50 + "\n")
            else:
                print(f"\nAn error occurred: {e}\n")

if __name__ == "__main__":
    main()
