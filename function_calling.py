import json
from datetime import datetime, timedelta

study_schedules = {}
flashcards_deck = []

def create_study_schedule(topic: str, days: int) -> str:
    schedule = {}
    start_date = datetime.now()
    for day in range(1, days + 1):
        target_date = (start_date + timedelta(days=day-1)).strftime("%Y-%m-%d")
        schedule[f"Day {day} ({target_date})"] = f"Focus heavily on mastering '{topic}' fundamentals, review notes, and complete practice set part {day}."
    
    study_schedules[topic] = schedule
    return json.dumps({
        "status": "Success", 
        "message": f"Generated a {days}-day plan for {topic}", 
        "schedule": schedule
    }, indent=2)

def save_flashcard(question: str, answer: str) -> str:
    card = {"id": len(flashcards_deck) + 1, "question": question, "answer": answer}
    flashcards_deck.append(card)
    return json.dumps({"status": "Saved", "card_id": card["id"]})

def get_all_flashcards() -> str:
    if not flashcards_deck:
        return json.dumps({"message": "No flashcards found. Generate some first!"})
    return json.dumps({"flashcards": flashcards_deck}, indent=2)
