
import os
import requests
import msal
from dotenv import load_dotenv

# Load environment variables from a .env file (DO NOT share your .env file!)
load_dotenv()

CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
TENANT_ID = os.getenv('TENANT_ID')
AUTHORITY = f"https://login.microsoftonline.com/{TENANT_ID}"
GRAPH_ENDPOINT = 'https://graph.microsoft.com/v1.0'

class M365Manager:
    def __init__(self):
        """Initializes MSAL app and acquires an access token."""
        self.app = msal.ConfidentialClientApplication(
            CLIENT_ID, authority=AUTHORITY, client_credential=CLIENT_SECRET
        )
        self.token = self._get_access_token()
        self.headers = {'Authorization': f'Bearer {self.token}', 'Content-Type': 'application/json'}

    def _get_access_token(self):
        """Authenticates with Microsoft Graph API using Client Credentials."""
        scopes = ["https://graph.microsoft.com/.default"]
        result = self.app.acquire_token_silent(scopes, account=None)
        if not result:
            print("🔑 Acquiring new token from Microsoft...")
            result = self.app.acquire_token_for_client(scopes=scopes)
        
        if "access_token" in result:
            return result["access_token"]
        else:
            raise Exception(f"❌ Failed to get token: {result.get('error_description')}")

    def list_users(self):
        """Retrieves and lists all users in the M365 Tenant."""
        print("\n📊 Current M365 Users:")
        response = requests.get(f'{GRAPH_ENDPOINT}/users?$select=displayName,userPrincipalName,accountEnabled', headers=self.headers)
        
        if response.status_code == 200:
            users = response.json().get('value', [])
            for user in users:
                status = "🟢 Active" if user['accountEnabled'] else "🔴 Disabled"
                print(f" - {user['displayName']} | {user['userPrincipalName']} | Status: {status}")
        else:
            print(f"❌ Error fetching users: {response.text}")

    def disable_user(self, user_principal_name):
        """Disables a user account (e.g., during offboarding)."""
        print(f"\n🔒 Disabling account for: {user_principal_name}...")
        data = {"accountEnabled": False}
        response = requests.patch(f'{GRAPH_ENDPOINT}/users/{user_principal_name}', headers=self.headers, json=data)
        
        if response.status_code == 204:
            print("✅ User account successfully disabled.")
        else:
            print(f"❌ Error disabling user: {response.text}")

if __name__ == "__main__":
    try:
        manager = M365Manager()
        
        # 1. List all users in the tenant
        manager.list_users()
        
        # 2. Example: Disable a specific user (Uncomment and change email to test)
        # manager.disable_user("former.employee@yourdomain.com")
        
    except Exception as e:
        print(e)
