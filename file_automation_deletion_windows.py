import os

source_dir = "INSERT FILE PATH"
for i in range(10):
    files = os.listdir(source_dir)

    for file in files:
        source_file_path = os.path.join(source_dir, file)
        os.remove(source_file_path)

        print(f"Iteration {i+1}: Files deleted from windows file explorer.")

    print("All iterations completed.")