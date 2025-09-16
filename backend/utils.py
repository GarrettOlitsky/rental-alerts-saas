import hashlib
import csv
import os

# -----------------------------
# Password hashing
# -----------------------------
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def verify_password(password, hashed):
    return hash_password(password) == hashed

# -----------------------------
# Save scraped listings to CSV
# -----------------------------
def save_listings_csv(listings, filename="data/results.csv"):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=["title", "price", "link", "date_posted"])
        writer.writeheader()
        for listing in listings:
            writer.writerow(listing)

# -----------------------------
# Example placeholder for email notifications
# -----------------------------
def send_email(to_email, subject, body):
    # Placeholder function, integrate with SendGrid / Mailgun later
    print(f"Sending email to {to_email} with subject '{subject}'")
