from tools import *

def crm_agent(user_input: str):
    user_input = user_input.lower()

    if "edit" in user_input:
        return edit_interaction(1, {"sentiment": "Positive"})

    if "follow" in user_input:
        return suggest_follow_up()

    summary = summarize_interaction(user_input)
    compliance = compliance_check(user_input)

    data = {
        "hcp_name": "Dr Smith",
        "interaction_type": "Meeting",
        "summary": summary,
        "sentiment": "Positive",
        "follow_up": "Call in 2 weeks"
    }

    log_interaction(data)

    return f"{summary}\n{compliance}"
