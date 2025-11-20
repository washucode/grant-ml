import re

SECTIONS = {
    "org_background": ["background", "organizational background", "about the organization"],
    "project_description": ["project description", "the project", "project summary"],
    "track_record": ["track record", "experience", "past performance"],
    "mission_statement": ["mission", "vision", "mandate"],
}

def extract_section(text, keywords):
    pattern = "|".join([fr"(?i){kw}" for kw in keywords])
    matches = list(re.finditer(pattern, text))
    
    if not matches:
        return ""

    start = matches[0].start()
    
    # find next section heading
    other_keywords = "|".join([fr"(?i){kw}" for k, v in SECTIONS.items() for kw in v])
    all_matches = list(re.finditer(other_keywords, text))

    next_sec_positions = [m.start() for m in all_matches if m.start() > start]

    end = next_sec_positions[0] if next_sec_positions else len(text)
    
    return text[start:end].strip()

def parse_proposal(text):
    parsed = {}
    for key, keywords in SECTIONS.items():
        parsed[key] = extract_section(text, keywords)
    return parsed
