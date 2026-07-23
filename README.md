# M365 Identity Automator (Python + MS Graph) 🏢🐍

This project showcases my ability to transition traditional L2 IT Support tasks into scalable cloud operations. Using **Python** and the **Microsoft Graph API**, this script automates Identity and Access Management (IAM) tasks within Microsoft 365 and Entra ID (formerly Azure AD).

## 🚀 Features

- **Automated Authentication:** Implements MSAL (Microsoft Authentication Library) for secure, headless authentication using App Registrations (Service Principals).
- **Identity Auditing:** Retrieves and lists user identities, UPNs, and their active/disabled status across the tenant.
- **Offboarding Automation:** Programmatically revokes access (disables accounts) for specific users, reducing manual clicks in the admin center and improving security compliance.

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Libraries:** `msal`, `requests`, `python-dotenv`
* **API:** Microsoft Graph API v1.0
* **Concepts:** Identity & Access Management (IAM), OAuth 2.0 / Client Credentials Flow, Zero Trust Security.

## ⚙️ How to Use

1. Clone the repository.
2. Install the requirements:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up your environment variables. Create a `.env` file in the root directory and add your Entra ID (Azure AD) App Registration details:
   ```text
   CLIENT_ID="your-app-client-id"
   CLIENT_SECRET="your-client-secret"
   TENANT_ID="your-tenant-id"
   ```
4. Run the script:
   ```bash
   python manage_m365.py
   ```

## 📸 Proof of Concept

*(Nota: Aquí subiremos capturas mostrando la consola corriendo y el reflejo del usuario deshabilitado en el Admin Center de M365)*

---
*Created by Rubén Darío Ortega - L2 IT Support Specialist & Cloud Operations.*
