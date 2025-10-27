from supabase import create_client, Client

# Supabase project credentials
url = "https://lnkqupiklbgvdmfnyjlj.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imxua3F1cGlrbGJndmRtZm55amxqIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjEzMjg3NzgsImV4cCI6MjA3NjkwNDc3OH0.GJq4fQFmql3pRL9nbHTcjk5JppxsvuDvF-Sli2aO-A4"

try:
    # Initialize Supabase client
    supabase: Client = create_client(url, key)
    print("✅ Connected to Supabase successfully!")

    # --- Step 1: Get record ID from user ---
    record_id_input = input("Enter ID of the record to delete: ")

    # Validate ID
    try:
        record_id = int(record_id_input)
    except ValueError:
        print("❌ Invalid ID. Please enter a valid integer.")
        exit()

    # --- Step 2: Delete record ---
    response = (
        supabase.table("Users")
        .delete()
        .eq("id", record_id)
        .execute()
    )

    # --- Step 3: Check response ---
    if response.data:
        print("✅ Record deleted successfully!")
        print("Deleted record data:", response.data)
    else:
        print("⚠️ No record found with the given ID or insufficient permissions.")

except Exception as e:
    print("❌ Error while deleting record:", e)
