from supabase import create_client, Client

# Supabase project credentials
url = ""
key = ""

# Try creating the client to test connection setup
try:
    supabase: Client = create_client(url, key)
    print("✅ Supabase connection initialized successfully!")
except Exception as e:
    print("❌ Failed to initialize Supabase connection:", e)

