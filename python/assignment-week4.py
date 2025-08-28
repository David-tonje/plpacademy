# File Read, Modify & Error Handling Challenge

def main():
    try:
        # Ask user for the input filename
        filename = input("Enter the filename to read: ")

        # Try opening the file
        with open(filename, "r") as infile:
            content = infile.read()
            print("\n📄 Original File Content:\n")
            print(content)

        # Modify the content (example: make everything uppercase)
        modified_content = content.upper()

        # Save to a new file
        output_file = "modified_" + filename
        with open(output_file, "w") as outfile:
            outfile.write(modified_content)

        print(f"\n✅ Modified content has been written to {output_file}")

    except FileNotFoundError:
        print("❌ Error: The file does not exist.")
    except PermissionError:
        print("❌ Error: You don’t have permission to read this file.")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
