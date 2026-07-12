import json
from pathlib import Path

STATE_FILE = Path("data/state.json")


def load_state():
    if not STATE_FILE.exists():
        return {
            "processed": []
        }
    
    try:
        return json.loads(
            STATE_FILE.read_text()
        )
    
    except json.JSONDecodeError:
        return {
            "processed": []
        }
    

def save_state(state):
    STATE_FILE.write_text(
        json.dumps(
            state,
            indent=4
        )
    )


def is_processed(uid, state):
    return uid in state["processed"]


def mark_processed(uid, state):
    state["processed"].append(uid)