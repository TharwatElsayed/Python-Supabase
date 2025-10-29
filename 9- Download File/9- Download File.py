from supabase import create_client, Client

# --- Supabase project credentials ---
url = "https://lnkqupiklbgvdmfnyjlj.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imxua3F1cGlrbGJndmRtZm55amxqIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc2MTMyODc3OCwiZXhwIjoyMDc2OTA0Nzc4fQ.QSzKG0kQywl4wnub1xu8-xpNpMm8kVlwhL8gqagk6p4"  # Use Service Role Key for full access

try:
    # Initialize Supabase client
    supabase: Client = create_client(url, key)
    print("✅ Connected to Supabase successfully!")

    # --- Step 1: Specify bucket and file path ---
    bucket_name = "images"  # Replace with your actual bucket name
    file_path = "profile_photos/ProfilePhoto.jpg"  # Path inside the bucket
    local_filename = "Downloaded_ProfilePhoto.jpg"  # Local file name to save

    # --- Step 2: Download file ---
    response = supabase.storage.from_(bucket_name).download(file_path)

    # --- Step 3: Save file locally ---
    if response:
        with open(local_filename, "wb") as f:
            f.write(response)
        print(f"✅ File downloaded successfully and saved as '{local_filename}'")
    else:
        print("⚠️ No data received — check file path or bucket permissions.")

except Exception as e:
    print("❌ Error while downloading file:", e)
