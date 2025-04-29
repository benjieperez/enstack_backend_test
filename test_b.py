# Create a simple application that rewrites the json data structure using Section A to Section B. Please note that Section A nodes are sorted in no particular order. 
# The "subordinate" node must be removed when no child exists (see markcorderoi and richard)

import json

def transform_data(section_a):
    # Create a dictionary to map each person to their manager
    manager_map = {}
    # Create a set of all login names to identify top-level managers
    all_logins = set()
    # Create a set of all subordinates to identify who has no manager
    all_subordinates = set()
    
    for item in section_a:
        # Handle items with "login_name" (some have trailing space in the example)
        login_key = "login_name" if "login_name" in item else "login_name"
        login_name = item[login_key].strip()
        manager_name = item["manager_name"].strip()
        
        manager_map[login_name] = manager_name
        all_logins.add(login_name)
        all_subordinates.add(manager_name)
    
    # Find top-level managers (those who aren't subordinates to anyone)
    top_managers = all_subordinates - all_logins
    
    # Build the hierarchy recursively
    def build_hierarchy(name):
        node = {"name": name}
        subordinates = [k for k, v in manager_map.items() if v == name]
        
        if subordinates:
            node["subordinate"] = [build_hierarchy(sub) for sub in subordinates]
        
        return node
    
    # Create the final structure
    section_b = [build_hierarchy(manager) for manager in sorted(top_managers)]
    return section_b

# Example usage
section_a = [
    {"manager_name": "nssi", "login_name": "nishanthi"},
    {"manager_name": "mbarcelona", "login_name ": "nssi"},
    {"manager_name": "nishanthi", "login_name": "markcorderoi"},
    {"manager_name": "mbarcelona", "login_name ": "richard"},
    {"manager_name": "letecia", "login_name ": "rudy"}
]

section_b = transform_data(section_a)
print(json.dumps(section_b, indent=4))