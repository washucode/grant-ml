import os
import pandas as pd
from extraction.extract_from_pdf import extract_text_from_pdf
from extraction.extract_from_docx import extract_text_from_docx
from extraction.section_parser import parse_proposal

def extract_proposal_to_row(file_path):
    ext = os.path.splitext(file_path)[1].lower()

    if ext == ".pdf":
        raw_text = extract_text_from_pdf(file_path)
    elif ext == ".docx":
        raw_text = extract_text_from_docx(file_path)
    else:
        raise ValueError("File must be PDF or DOCX")

    sections = parse_proposal(raw_text)

    # Placeholder numeric fields (can later extract programmatically)
    numeric_defaults = {
        "past_grants_total": 0,
        "annual_budget": 0,
        "total_revenue": 0,
        "annual_budget_last_year": 0,
        "cash_reserves": 0,
        "monthly_operating_expenses": 0,
        "years_active": 0,
    }

    return {**sections, **numeric_defaults}
