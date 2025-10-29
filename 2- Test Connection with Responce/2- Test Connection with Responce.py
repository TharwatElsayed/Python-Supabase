from supabase import create_client, Client

# Supabase project credentials
url = ""
key = ""

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

