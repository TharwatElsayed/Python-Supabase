from supabase import create_client, Client

# Supabase project credentials
url = ""
key = ""

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

