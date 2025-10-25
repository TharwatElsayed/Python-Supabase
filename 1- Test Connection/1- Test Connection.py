from supabase import create_client, Client

# Supabase project credentials
url = "https://lnkqupiklbgvdmfnyjlj.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imxua3F1cGlrbGJndmRtZm55amxqIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjEzMjg3NzgsImV4cCI6MjA3NjkwNDc3OH0.GJq4fQFmql3pRL9nbHTcjk5JppxsvuDvF-Sli2aO-A4"

# Try creating the client to test connection setup
try:
    supabase: Client = create_client(url, key)
    print("✅ Supabase connection initialized successfully!")
except Exception as e:
    print("❌ Failed to initialize Supabase connection:", e)
