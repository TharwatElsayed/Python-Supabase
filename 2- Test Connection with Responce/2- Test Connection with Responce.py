from supabase import create_client, Client

# Supabase project credentials
url = "https://lnkqupiklbgvdmfnyjlj.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imxua3F1cGlrbGJndmRtZm55amxqIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjEzMjg3NzgsImV4cCI6MjA3NjkwNDc3OH0.GJq4fQFmql3pRL9nbHTcjk5JppxsvuDvF-Sli2aO-A4"

try:
    # Initialize client
    supabase: Client = create_client(url, key)
    print("✅ Supabase connection initialized successfully!")

    # Make a simple API request to confirm connectivity
    # We'll fetch from the system schema 'pg_meta' which lists tables in your project
    response = supabase.rpc('version').execute()
    print("📡 Supabase response received!")
    print("Response data:", response.data)

except Exception as e:
    print("❌ Failed to connect or fetch response:", e)
