from supabase import create_client, Client

# --- Supabase project credentials ---
url = "https://lnkqupiklbgvdmfnyjlj.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imxua3F1cGlrbGJndmRtZm55amxqIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc2MTMyODc3OCwiZXhwIjoyMDc2OTA0Nzc4fQ.QSzKG0kQywl4wnub1xu8-xpNpMm8kVlwhL8gqagk6p4"  # Use your Service Role Key for delete permissions

try:
    # Initialize Supabase client
    supabase: Client = create_client(url, key)
    print("✅ Connected to Supabase successfully!")

    # --- Step 1: Specify bucket and file to delete ---
    bucket_name = "images"  # Replace with your actual bucket name
    file_path = "profile_photos/ProfilePhoto.jpg"  # Path inside the bucket

    # --- Step 2: Delete file ---
    response = supabase.storage.from_(bucket_name).remove([file_path])

    # --- Step 3: Show result ---
    if isinstance(response, list) and response:
        print(f"✅ File '{file_path}' deleted successfully from '{bucket_name}' bucket!")
    else:
        print(f"⚠️ File '{file_path}' may not exist or could not be deleted.")
        print("Response:", response)

except Exception as e:
    print("❌ Error while deleting file:", e)
