import os
import re

# Function to create directories if they don't exist
def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Created directory: {path}")

# Function to sanitize folder and file names to be cross-platform compatible
def sanitize_name(name):
    # Convert to lowercase
    name = name.lower()
    # Replace spaces with underscores and allow dots between numbers and words, but remove other non-alphanumeric characters
    name = re.sub(r'[^a-zA-Z0-9._]', '', name).strip().replace(' ', '_')
    return name

# Function to create a Logseq page with dummy content
def create_logseq_page(page_dir, page_name, content):
    page_path = os.path.join(page_dir, f"{sanitize_name(page_name)}.md")
    with open(page_path, 'w') as page:
        # Add title and favorite tag to ensure the page shows up in the sidebar favorites
        page.write(f"#+TITLE: {page_name}\n#+FAVORITES: {page_name}\n\n")
        page.write(content)
    print(f"Created Logseq page: {page_path}")
    return page_name

# Function to create a logseq config.edn file with the favorites section
def create_logseq_config(logseq_dir, favorites):
    config_path = os.path.join(logseq_dir, "config.edn")
    with open(config_path, 'w') as config_file:
        config_file.write("{:meta/version 1\n\n")
        config_file.write(" ;; Favorites to list on the left sidebar\n")
        config_file.write(f" :favorites {favorites}\n")
        config_file.write("\n ;; Additional Logseq configurations can go here\n}\n")
    print(f"Created Logseq config file: {config_path}")

# Function to create the Daily Agenda template for each company
def create_daily_agenda_template(company_name):
    template = f"""
[[Daily Agenda]]
    
- **What are the top 3 most important tasks for {company_name} today?**
    - Task 1
    - Task 2
    - Task 3
- **How are you feeling today?**
    - I feel great!
- **What are you motivated to work on?**
    - Work on my startup application
- **Wins**
    - Time to myself
- **Losses**
    - Not very productive
- **Rate your performance out of 10**
    - 6
- **Journal**
    - Random thoughts of the day
"""
    return template

# List of company names
companies = ["snapsuite", "phd solutions", "dwain unfinished", "firmhub", "dwainbrowne", "downtown dwainbrowne"]

# Logseq page structure with dummy content for companies, obligations, resources, and the new programming section
logseq_structure = {
    "companies": {
        "planning": "## Strategic Goals\n\n- Goal 1: Increase market share by 15%\n- Goal 2: Launch new product line\n\n## Business Plans\n\n- Plan 1: Expand to new markets\n- Plan 2: Improve customer retention",
        "sales": "## Leads\n\n- Lead 1: Company A\n- Lead 2: Company B\n\n## Sales Reports\n\n- Report 1: Q1 2024\n- Report 2: Q2 2024",
        "marketing": "## Campaigns\n\n- Campaign 1: Social Media Blitz\n- Campaign 2: Email Marketing Push\n\n## Branding\n\n- Branding guidelines\n- Logo redesign ideas",
        "operations": "## Processes\n\n- Process 1: Order fulfillment\n- Process 2: Inventory management\n\n## Quality Control\n\n- QC Checklist\n- Defect rate analysis",
        "human_resources": "## Recruitment\n\n- Job postings\n- Interview schedules\n\n## Training Certifications\n\n- Certification 1: Safety training\n- Certification 2: Management skills",
        "legal": "## Compliance\n\n- Compliance checklists\n- Regulatory updates\n\n## Contracts\n\n- Contract 1: Vendor agreement\n- Contract 2: Client NDA",
        "it_infrastructure": "## Systems Management\n\n- System 1: CRM maintenance\n- System 2: Network monitoring\n\n## Security\n\n- Security protocols\n- Data breach response plan",
        "finance": "## Budgeting\n\n- Budget 1: Operational budget\n- Budget 2: Marketing budget\n\n## Financial Reports\n\n- Report 1: Annual financials\n- Report 2: Quarterly earnings",
        "programming": "## Code Snippets\n\n- Useful code snippets\n\n## Project Ideas\n\n- New programming projects"
    },
    "obligations": {
        "personal": {
            "health": "## Health - Medical\n\n- Medical history\n- Appointments\n\n## Insurance\n\n- Policy details\n- Claims history",
            "finance": "## Financials\n\n- Budget tracking\n- Expense reports\n\n## Taxes\n\n- Tax filings\n- Receipts",
            "identity": "## Drivers License\n\n- Expiry dates\n- Renewal reminders\n\n## Passport\n\n- Passport number\n- Renewal dates",
            "family": "## Events\n\n- Birthdays\n- Anniversaries\n\n## Archive\n\n- Family photos\n- Important documents",
            "legal": "## Infractions\n\n- Traffic tickets\n- Legal consultations\n\n## Rental Application\n\n- Rental agreements\n- Application status",
            "employment": "## Contracts\n\n- Employment contracts\n- Contractor agreements\n\n## Pay Stubs\n\n- Monthly salary breakdown\n- Tax deductions",
            "planning": "## Business Planning\n\n- Business goals\n- SWOT analysis\n\n## Personal Planning\n\n- Personal goals\n- Daily to-dos",
            "travel": "## Upcoming Trips\n\n- Itinerary\n- Packing lists\n\n## Travel Documents\n\n- Passports\n- Visa details",
            "photos_videos": "## Family Photos\n\n- 2024 vacation\n- Holiday gatherings\n\n## Archived Media\n\n- Old family photos\n- Historical records",
            "miscellaneous": "## Business\n\n- Business notes\n- Meeting agendas\n\n## Branding\n\n- Logos\n- Brand guidelines"
        },
        "people": {
            "friend_1": "## Notes\n\n- Birthday reminders\n- Gift ideas\n\n## Photos\n\n- Party photos\n- Shared memories",
            "friend_2": "## Notes\n\n- Catch-up topics\n- Mutual interests\n\n## Photos\n\n- Trip to the beach\n- Hiking memories",
            "colleagues": "## Notes\n\n- Project updates\n- Task delegation\n\n## Documents\n\n- Meeting minutes\n- Project proposals",
            "acquaintances": "## Notes\n\n- Networking topics\n- Common connections"
        },
        "family": {
            "family_1": "## Notes\n\n- Family reunion notes\n- Shared responsibilities\n\n## Photos\n\n- Family photos\n- Holiday gatherings",
            "family_2": "## Notes\n\n- Event planning\n- Daily updates\n\n## Documents\n\n- Birth certificates\n- Legal documents"
        }
    },
    "resources": {
        "audio_notes": "## Random Thoughts\n\n- Ideas for new projects\n- Reflection on the day\n\n## Meeting Notes\n\n- Notes from team meeting\n- Action items",
        "brainstorming": "## Business Ideas\n\n- New product concepts\n- Market expansion strategies\n\n## Personal Projects\n\n- Home improvement ideas\n- Hobby projects",
        "bookmarks": "## Business Productivity\n\n- Articles on time management\n- Tools for efficiency\n\n## Design Inspiration\n\n- Website designs\n- Branding concepts",
        "books": {
            "non_fiction": "## Business Leadership\n\n- Book 1: Principles by Ray Dalio\n- Book 2: The Lean Startup\n\n## Personal Development\n\n- Book 1: Atomic Habits\n- Book 2: Deep Work",
            "fiction": "## Novels\n\n- Novel 1: 1984 by George Orwell\n- Novel 2: Brave New World\n\n## Short Stories\n\n- Story 1: The Lottery\n- Story 2: A Good Man is Hard to Find"
        },
        "design_notes": "## UX Design\n\n- Wireframes for project X\n- User flows for onboarding\n\n## Interior Design\n\n- Living room layout\n- Color palette options",
        "miscellaneous_ideas": "## Random Thoughts\n\n- Ideas for future\n- Personal reflections\n\n## Quotes Inspiration\n\n- Quote 1: 'The only limit to our realization of tomorrow is our doubts of today.'\n- Quote 2: 'Success is not final, failure is not fatal: It is the courage to continue that counts.'"
    },
    "records": {
        "family": "## Family History\n\n- Genealogy research\n- Family tree\n\n## Important Documents\n\n- Birth certificates\n- Marriage licenses",
        "business": "## Business Transactions\n\n- Invoice records\n- Payment history\n\n## Contracts\n\n- Contract 1: Vendor\n- Contract 2: Client",
        "old_records": "## Archived Documents\n\n- Old tax filings\n- Historical agreements"
    }
}

# Create the Logseq folder structure, pages, and config files
def create_logseq_structure(root_path, companies, structure):
    core_notes_dir = os.path.join(root_path, "C.O.R.E_notes")
    create_directory(core_notes_dir)
    
    # Create company folders and their corresponding pages
    companies_dir = os.path.join(core_notes_dir, "companies")
    create_directory(companies_dir)
    
    for company in companies:
        company_dir = os.path.join(companies_dir, sanitize_name(company))
        create_directory(company_dir)
        print(f"Creating Logseq structure for company: {company}")
        
        favorites = []
        for page_name, content in structure["companies"].items():
            favorites.append(f"\"{page_name}\"")
            create_logseq_page(company_dir, page_name, content)
        
        # Create the daily agenda template for the company
        daily_agenda_content = create_daily_agenda_template(company)
        create_logseq_page(company_dir, "Daily Agenda", daily_agenda_content)
        favorites.append("\"Daily Agenda\"")
        
        # Create the logseq folder and config.edn file with favorites
        logseq_dir = os.path.join(company_dir, "logseq")
        create_directory(logseq_dir)
        create_logseq_config(logseq_dir, f"[{', '.join(favorites)}]")

    # Create Obligations, Resources, and Records folders and their corresponding pages
    for section, sub_structure in structure.items():
        if section != "companies":
            section_dir = os.path.join(core_notes_dir, sanitize_name(section))
            create_directory(section_dir)
            for sub_page, content in sub_structure.items():
                if isinstance(content, dict):
                    sub_section_dir = os.path.join(section_dir, sanitize_name(sub_page))
                    create_directory(sub_section_dir)
                    favorites = []
                    for sub_sub_page, sub_content in content.items():
                        favorites.append(f"\"{sub_sub_page}\"")
                        create_logseq_page(sub_section_dir, sub_sub_page, sub_content)
                    
                    # Create the logseq folder and config.edn file with favorites
                    logseq_dir = os.path.join(sub_section_dir, "logseq")
                    create_directory(logseq_dir)
                    create_logseq_config(logseq_dir, f"[{', '.join(favorites)}]")
                else:
                    create_logseq_page(section_dir, sub_page, content)

# Main function to generate the Logseq structure for each company
def main(root_path):
    print("Starting Logseq folder and page creation...")
    create_logseq_structure(root_path, companies, logseq_structure)
    print("Logseq structure creation completed.")

# Run the script
if __name__ == "__main__":
    # Specify the root path where the C.O.R.E_notes folder should be created
    root_path = r"C:\Users\DwainBrowne\OneDrive - SnapSuite\__new"  # Change this to your desired path
    main(root_path)
