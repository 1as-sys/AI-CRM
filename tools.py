from models import Interaction
from database import SessionLocal

db = SessionLocal()

def log_interaction(data):
    interaction = Interaction(**data)
    db.add(interaction)
    db.commit()
    return "Interaction logged successfully"

def edit_interaction(id, updates):
    interaction = db.query(Interaction).get(id)
    for k, v in updates.items():
        setattr(interaction, k, v)
    db.commit()
    return "Interaction updated"

def summarize_interaction(text):
    return f"Summary: {text[:100]}..."

def suggest_follow_up():
    return "Suggested follow-up: Schedule meeting in 2 weeks"

def compliance_check(text):
    if "guarantee" in text.lower():
        return "Compliance Risk Detected"
    return "Compliant"
