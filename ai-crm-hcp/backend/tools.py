from db import SessionLocal
from models import Interaction

# ✅ 1. LOG INTERACTION
def log_interaction(data):
    db = SessionLocal()

    obj = Interaction(
        doctor_name=data["doctor_name"],
        summary=data["summary"],
        next_action=", ".join(data["next_action"])  # ✅ convert list → string
    )

    db.add(obj)
    db.commit()
    db.refresh(obj)

    return {
        "id": obj.id,
        "doctor_name": obj.doctor_name
    }


# ✅ 2. EDIT INTERACTION
def edit_interaction(data):
    db = SessionLocal()

    obj = db.query(Interaction).get(data["id"])

    if not obj:
        return {"error": "Not found"}

    obj.summary = data["summary"]

    # ✅ handle list update
    if "next_action" in data:
        obj.next_action = ", ".join(data["next_action"])

    db.commit()

    return {"message": "Updated"}


# ✅ 3. GET INTERACTIONS
def get_interactions(_):
    db = SessionLocal()

    data = db.query(Interaction).all()

    return [
        {
            "id": i.id,
            "doctor": i.doctor_name,
            "summary": i.summary,
            "next_action": i.next_action.split(", ")  # ✅ string → list
        }
        for i in data
    ]


# ✅ 4. SUMMARIZE (LLM)
def summarize_interaction(llm, notes):
    return llm.invoke(
        f"Summarize this medical interaction clearly: {notes}"
    ).content


# ✅ 5. SUGGEST NEXT ACTION (RULE-BASED)
def suggest_next_action(summary):
    actions = []

    # Always include
    actions.append("Schedule a follow-up meeting")
    actions.append("Share clinical data and product resources")

    text = summary.lower()

    # Better matching (covers more cases)
    if "interest" in text or "interested" in text:
        actions.append("Provide drug samples")
        actions.append("Discuss patient use cases")

    return actions

