import json
from utils import pdf  # Updated import path

def save_progress(user_id, progress_data, filename="user_progress.json"):
    """Save user progress to a JSON file."""
    try:
        with open(filename, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}

    data[user_id] = progress_data
    with open(filename, "w") as f:
        json.dump(data, f)

def load_progress(user_id, filename="user_progress.json"):
    """Load user progress from a JSON file."""
    try:
        with open(filename, "r") as f:
            data = json.load(f)
            return data.get(user_id, {})
    except FileNotFoundError:
        return {}

def generate_progress_pdf(user_id, filename="progress_report.pdf"):
    """Generate a PDF report of user progress."""
    # Load the user's progress data
    progress_data = load_progress(user_id)
    
    # Format the content for the PDF
    title = f"Progress Report for User {user_id}"
    content = "Curriculum Progress Summary:\n\n"
    for module, status in progress_data.items():
        content += f"Module: {module}\nStatus: {status}\n\n"
    
    # Generate PDF using the pdf_report module
    pdf.create_pdf_report(title, content, filename)
    print(f"Progress report generated: {filename}")
