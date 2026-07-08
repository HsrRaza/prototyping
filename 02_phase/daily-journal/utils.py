from journal  import JournalEntry
from storage import save_entries ,load_entries



def add_to_dic():
    title = input("Title : ")
    content = input("Content : ")


    new_entry_object = JournalEntry(title , content)

    new_entry_dict =new_entry_object.to_dict()

    current_entries = load_entries()

    current_entries.append(new_entry_dict)

    save_entries(current_entries)

    print("Entry Saved successfully ")


def read_entries():
    entries = load_entries()
    if not entries:
         print("No data found") 
    else:
         for entry in entries:
             print(f"[{entry['created_at']}] {entry['title']}: {entry['content']}")