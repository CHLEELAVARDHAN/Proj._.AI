import json

def load_skills_jobs():
    try:
        with open("data/skills_jobs.json") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def get_companies_for_skill(skill):
    data = load_skills_jobs()
    skill = skill.lower()  # case-insensitive match

    for key in data:
        if key.lower() == skill:
            return data[key]['Companies']  # list of dicts with name & package
    return []
