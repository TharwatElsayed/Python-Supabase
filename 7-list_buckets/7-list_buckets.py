from supabase import create_client, Client

# --- Supabase project credentials ---
url = ""
key = ""

try:
    # Initialize Supabase client
    supabase: Client = create_client(url, key)
    print("✅ Connected to Supabase successfully!")

    # --- Step 1: List all buckets ---
    buckets = supabase.storage.list_buckets()

    # --- Step 2: Display bucket info ---
    if buckets:
        print("📦 Available Buckets:")
        for bucket in buckets:
            print(f" - Name: {bucket.name}, Public: {bucket.public}")
    else:
        print("⚠️ No buckets found in this Supabase project.")

except Exception as e:

    print("❌ Error while listing buckets:", e)
