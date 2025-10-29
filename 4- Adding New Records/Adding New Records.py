from supabase import create_client, Client

# Supabase project credentials
url = ""
key = ""

try:
    # Initialize Supabase client
    supabase: Client = create_client(url, key)
    print("✅ Connected to Supabase successfully!")

    # --- Step 1: Get user input ---
    name = input("Enter user name: ")
    age_input = input("Enter age: ")

    # Convert to float safely
    try:
        age = float(age_input)
    except ValueError:
        print("❌ Invalid age value. Please enter a number.")
        exit()

    # --- Step 2: Insert new record ---
    response = supabase.table("Users").insert(
        {"name": name, "age": age}
    ).execute()

    # --- Step 3: Check response ---
    if response.data:
        print("✅ Record added successfully!")
        print("Inserted data:", response.data)
    else:
        print("⚠️ No data returned. Check RLS or permissions in Supabase.")

except Exception as e:
    print("❌ Error while inserting record:", e)

