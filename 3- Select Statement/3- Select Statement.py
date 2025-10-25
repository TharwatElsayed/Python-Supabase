from supabase import create_client, Client

# Supabase project credentials
url = "https://lnkqupiklbgvdmfnyjlj.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imxua3F1cGlrbGJndmRtZm55amxqIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjEzMjg3NzgsImV4cCI6MjA3NjkwNDc3OH0.GJq4fQFmql3pRL9nbHTcjk5JppxsvuDvF-Sli2aO-A4"

try:
    # Initialize Supabase client
    supabase: Client = create_client(url, key)
    print("✅ Supabase connection initialized successfully!")

    # Step 1: Fetch current records
    response = supabase.table("Users").select("*").execute()
    users = response.data

    if not users:
        print("ℹ️ No users found. Inserting a test record...")

        # Step 2: Insert one sample user
        insert_response = supabase.table("Users").insert(
            {"name": "Tharwat", "age": 35.0}
        ).execute()

        print("✅ Inserted user:", insert_response.data)

        # Step 3: Re-fetch all users
        response = supabase.table("Users").select("*").execute()
        users = response.data

    print("📡 Users in database:")
    for user in users:
        print(user)

except Exception as e:
    print("❌ Error connecting or querying Supabase:", e)
