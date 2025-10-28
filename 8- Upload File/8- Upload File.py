from supabase import create_client, Client
import os

# --- Supabase project credentials ---
url = "https://lnkqupiklbgvdmfnyjlj.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imxua3F1cGlrbGJndmRtZm55amxqIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc2MTMyODc3OCwiZXhwIjoyMDc2OTA0Nzc4fQ.QSzKG0kQywl4wnub1xu8-xpNpMm8kVlwhL8gqagk6p4"

try:
    # Initialize Supabase client
    supabase: Client = create_client(url, key)
    print("✅ Connected to Supabase successfully!")

    # --- Step 1: Select bucket and file ---
    bucket_name = "images"  # Change to your actual bucket name
    file_path = "ProfilePhoto.jpg"  # Local file path

    if not os.path.exists(file_path):
        print(f"❌ File not found: {file_path}")
        exit()

    # --- Step 2: Read file bytes ---
    with open(file_path, "rb") as f:
        file_bytes = f.read()

    # --- Step 3: Upload file ---
    response = supabase.storage.from_(bucket_name).upload(
        path=f"profile_photos/{os.path.basename(file_path)}",
        file=file_bytes,
        file_options={"content-type": "image/jpeg"}
    )

    print("📤 Upload Response:", response)

    # --- Step 4: Generate a public URL for the uploaded image ---
    public_url = supabase.storage.from_(bucket_name).get_public_url(
        f"profile_photos/{os.path.basename(file_path)}"
    )

    print("✅ File uploaded successfully!")
    print("🌐 Public URL:", public_url)

except Exception as e:
    print("❌ Error while uploading file:", e)
