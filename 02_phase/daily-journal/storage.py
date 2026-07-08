import json
import os

FILE = 'data/journalData.json'

def load_entries():
    """Load entries from JSON file"""
    try:
        if os.path.exists(FILE):
            with open(FILE, 'r') as f:
                # Check if file is empty
                content = f.read().strip()
                if not content:
                    print("ℹ️  File is empty. Starting fresh.")
                    return []
                
                # Parse JSON
                entries = json.loads(content)
                print(f"📖 Loaded {len(entries)} entries")
                return entries
        else:
            print("ℹ️  No data file. Starting fresh.")
            return []
            
    except json.JSONDecodeError as e:
        print(f"❌ Corrupted JSON: {e}")
        print("ℹ️  Starting with empty journal.")
        return []
    except Exception as e:
        print(f"❌ Error loading: {e}")
        return []



def save_entries(entries):
    try:
        os.makedirs(os.path.dirname(FILE),exist_ok =True)

        with open(FILE, 'w') as f:
            json.dump(entries , f, indent=4)
        print(f" Saved{ len(entries)}")
        return True
    except Exception as e:
        print(f"Error Saving ", e)
        return False
