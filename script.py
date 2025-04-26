import subprocess

# List of your necessary python files to run
files_to_run = [
    "store_index.py",  # generate vectorstore/index
]

for file in files_to_run:
    print(f"\n🔵 Running {file}...")
    try:
        subprocess.run(["python", file], check=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ Error occurred while running {file}: {e}")
        break
else:
    # If no errors in the above scripts, start the Flask app
    print("\n🚀 Starting Flask app (app.py)...")
    subprocess.run(["python", "app.py"])
