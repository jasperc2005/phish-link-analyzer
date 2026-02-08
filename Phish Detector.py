import email
from email import policy
import re
import vt


FILE_PATH = r'C:\Users\jaspe\Downloads\Order submitted REF#38493.eml'
VT_API_KEY = '29aca87fdd0d530fbe3f2a0dad4f336e9efe983c02dd3cbcd3a2c5efd8487341'


with open(FILE_PATH, 'rb') as f:
    msg = email.message_from_binary_file(f, policy=policy.default)

print(f"Subject: {msg['subject']}")

body_part = msg.get_body(preferencelist=('plain', 'html'))
body_text = body_part.get_content()


links = re.findall(r'(https?://[^\s<>"]+)', body_text)
unique_links = set(links)


if unique_links:
    with vt.Client(VT_API_KEY) as client:
        for link in unique_links:
            print(f"\nScanning: {link}")
            try:
                url_id = vt.url_id(link)
                url_obj = client.get_object(f"/urls/{url_id}")
                
                stats = url_obj.last_analysis_stats
                malicious = stats['malicious']
                
                if malicious > 0:
                    print(f"❌ DANGER: {malicious} engines flagged this as malicious!")
                else:
                    print("✅ Clean: No engines flagged this link.")
            except Exception as e:
                print(f"Could not scan {link}: {e}")
else:
    print("No links found in the email body.")