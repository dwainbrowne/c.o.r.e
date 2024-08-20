import os
import re
from datetime import datetime

# Function to create directories if they don't exist
def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Created directory: {path}")

# Function to sanitize folder names to be cross-platform compatible
def sanitize_name(name):
    # Convert to lowercase
    name = name.lower()
    # Replace spaces with underscores and allow dots between numbers and words, but remove other non-alphanumeric characters
    name = re.sub(r'[^a-zA-Z0-9._]', '', name).strip().replace(' ', '_')
    return name

# Function to create sample meeting files
def create_sample_meeting_files(meetings_dir):
    sample_files = [
        "2024-08-20-strategy-session.md",
        "2024-08-25-product-roadmap.md",
        "2024-09-01-market-analysis.md"
    ]
    for file_name in sample_files:
        file_path = os.path.join(meetings_dir, file_name)
        with open(file_path, 'w') as file:
            file.write(f"# {file_name.replace('.md', '').replace('-', ' ').title()}\n\n")
            file.write("Meeting notes go here...\n")
        print(f"Created sample file: {file_path}")

# List of company names
companies = ["snapsuite", "phd solutions", "dwain unfinished", "firmhub", "dwainbrowne", "downtown dwainbrowne"]

# Base folder structure with numbered and ordered sections
base_structure = {
    "1.companies": {
        "1.planning": {
            "strategic_goals": [],
            "business_plans": [],
            "market_research": [],
            "product_roadmaps": [],
            "meetings": []  # Adding the meetings folder here
        },
        "2.sales": ["leads", "client_communications", "contracts", "sales_reports"],
        "3.marketing": ["campaigns", "content_strategy", "branding", "social_media"],
        "4.operations": ["processes", "project_management", "logistics", "quality_control"],
        "5.human_resources": ["recruitment", "employee_records", "payroll", "training_certifications"],
        "6.legal": ["compliance", "contracts", "intellectual_property", "legal_disputes"],
        "7.it_infrastructure": ["systems_management", "security", "software_tools", "network_management"],
        "8.finance": ["budgeting", "accounting", "financial_reports", "tax_documents"],
        "9.clients": {
            "notes": [],
            "photos": [],
            "documents": []
        }
    },
    "2.obligations": {
        "personal": {
            "health": ["health_medical", "fertility_clinic", "ohip", "insurance"],
            "finance": ["financials", "receipts", "taxes", "social_insurance"],
            "identity": ["drivers_license", "permanent_resident", "passport", "certificates"],
            "family": ["events", "church", "school", "archive"],
            "legal": ["infractions", "rental_application", "car", "archive"],
            "employment": ["contracts", "pay_stubs", "performance_reviews", "training_certifications"],
            "planning": ["business_planning", "personal_planning", "strategic_goals", "checklists_to_dos"],
            "travel": ["upcoming_trips", "past_trips", "itineraries", "travel_documents"],
            "photos_videos": ["family_photos", "event_photos", "personal_videos", "archived_media"],
            "miscellaneous": ["business", "branding", "instructions", "signature", "scan"],
        },
        "people": {
            "friend_1": ["notes", "photos", "documents"],
            "friend_2": ["notes", "photos", "documents"],
            "colleagues": ["notes", "photos", "documents"],
            "acquaintances": ["notes", "photos", "documents"],
        },
        "family": {
            "family_1": ["notes", "photos", "documents"],
            "family_2": ["notes", "photos", "documents"],
            "extended_family": ["notes", "photos", "documents"],
        },
    },
    "3.resources": {
        "audio_notes": ["random_thoughts", "meeting_notes", "ideas"],
        "brainstorming": ["business_ideas", "personal_projects", "creative_concepts"],
        "bookmarks": ["business_productivity", "design_inspiration", "learning_tutorials", "personal_interests"],
        "books": {
            "non_fiction": ["business_leadership", "personal_development", "finance_investing"],
            "fiction": ["novels", "short_stories", "essays"],
        },
        "design_notes": {
            "ux_design": ["wireframes", "user_flows", "ui_inspiration"],
            "interior_design": ["room_layouts", "color_palettes", "furniture_ideas"],
        },
        "miscellaneous_ideas": ["random_thoughts", "quotes_inspiration", "miscellaneous_resources"],
    },
    "4.records": ["family", "business", "old_records"],
}

# Create the folder structure
def create_folder_structure(base_dir, structure):
    if isinstance(structure, dict):
        for folder, subfolders in structure.items():
            folder_path = os.path.join(base_dir, sanitize_name(folder))
            create_directory(folder_path)
            create_folder_structure(folder_path, subfolders)
            if "meetings" in folder:  # Check if we are in the meetings folder
                create_sample_meeting_files(folder_path)  # Create sample meeting files
    elif isinstance(structure, list):
        for subfolder in structure:
            create_directory(os.path.join(base_dir, sanitize_name(subfolder)))

# Main function to generate the folder structure for each company
def main(root_path):
    core_dir = os.path.join(root_path, "C.O.R.E.")
    
    # Create the base "C.O.R.E." directory
    create_directory(core_dir)
    print("Starting folder structure creation...")
    
    # Iterate through the companies and create their respective folder structures
    for company in companies:
        company_dir = os.path.join(core_dir, "1.companies", sanitize_name(company))
        print(f"Creating structure for company: {company}")
        create_folder_structure(company_dir, base_structure["1.companies"])
    
    # Create other top-level folders like "Obligations", "Resources", and "Records"
    for section, sub_structure in base_structure.items():
        if section != "1.companies":
            print(f"Creating structure for section: {section}")
            create_folder_structure(os.path.join(core_dir, sanitize_name(section)), sub_structure)

    print("Folder structure creation completed.")

# Run the script
if __name__ == "__main__":
    # Specify the root path where the C.O.R.E. folder should be created
    root_path = r"C:\Users\DwainBrowne\OneDrive - SnapSuite\__new"  # Change this to your desired path
    main(root_path)
