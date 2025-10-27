from supabase import create_client, Client

# Supabase project credentials
url = "https://lnkqupiklbgvdmfnyjlj.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imxua3F1cGlrbGJndmRtZm55amxqIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjEzMjg3NzgsImV4cCI6MjA3NjkwNDc3OH0.GJq4fQFmql3pRL9nbHTcjk5JppxsvuDvF-Sli2aO-A4"

try:
    # Initialize Supabase client
    supabase: Client = create_client(url, key)
    print("✅ Connected to Supabase successfully!")

    # --- Step 1: Get user input ---
    record_id_input = input("Enter ID of the record to update: ")
    name = input("Enter new user name: ")
    age_input = input("Enter new age: ")

    # Convert to correct types
    try:
        record_id = int(record_id_input)
        age = float(age_input)
    except ValueError:
        print("❌ Invalid input. ID must be an integer and age a number.")
        exit()

    # --- Step 2: Update record ---
    response = (
        supabase.table("Users")
        .update({"name": name, "age": age})
        .eq("id", record_id)
        .execute()
    )

    # --- Step 3: Check response ---
    if response.data:
        print("✅ Record updated successfully!")
        print("Updated data:", response.data)
    else:
        print("⚠️ No record found with the given ID or insufficient permissions.")

except Exception as e:
    print("❌ Error while updating record:", e)
