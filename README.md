#phish-link-analyzer

## 🛡️ Project Overview
This project is a Python-based security tool designed to automate the initial triage of suspicious emails. It parses `.eml` files to extract metadata (Subject, From, To) and uses Regular Expressions (Regex) to identify all embedded URLs. The tool then queries the **VirusTotal API** to determine if any links have been flagged as malicious by industry vendors.

## 🚀 Features
- **Automated Parsing:** Handles complex multipart EML structures to extract plain-text body content.
- **URL Extraction:** Utilizes Regex patterns to identify hidden or suspicious links.
- **Threat Intelligence Integration:** Connects to VirusTotal for real-time reputation analysis.


## 🛠️ Technical Breakdown
### 1. EML Parsing & Decoding
Initially, I encountered issues where standard `get_payload()` calls failed on multipart emails (common in modern phishing). I implemented a recursive check to ensure the script correctly decodes bytes into readable text regardless of the email's structure.

### 2. URL Identification
Using the `re` module, the script scans the decoded body for URI patterns. By converting findings into a `set()`, I ensured that duplicate links (often found in "Unsubscribe" and "Click Here" buttons) are only scanned once, saving API quota.

### 3. VirusTotal Integration
The script sends the identified URLs to VirusTotal. 
- **Clean:** 0 engines flagged the link.
- **Malicious:** >0 engines flagged the link, triggering a high-priority warning.

## 📊 Results
<img width="536" height="89" alt="image" src="https://github.com/user-attachments/assets/92073fcb-00e8-4de4-9cd4-1cb19d0e5a44" />
*Example output showing a detected phishing link from a verified PhishTank sample.*

## 🔧 Installation & Usage
1. Clone the repo: `git clone https://github.com/YOUR_USERNAME/Project_Name`
2. Install dependencies: `pip install vt-py`
3. Add your VirusTotal API key to the script.
4. Run: `python eml_analyzer.py`
