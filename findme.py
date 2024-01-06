import subprocess

def steghide_extract(input_image, passphrase):
    try:
        # Construct the steghide extract command
        command = [
            'steghide',
            'extract',
            '-sf', input_image,  # Input image
 	    '-xf', output_file,  # Output extracted file
            '-p', passphrase     # Passphrase (if applicable)
        ]

        # Run the steghide extract command
        subprocess.run(command, check=True)

        print("Extraction completed successfully.")
    except subprocess.CalledProcessError as e:
        print("Error:", e)
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    # Replace these with your file path and passphrase (if applicable)
    input_image = "/home/sysadmin/Pictures/islands/goofball/bingbong.jpg"
    output_file = "/home/sysadmin/Pictures/islands/goofball/secretmessage.py"
    passphrase = "apple"  # Leave empty if not encrypted

    steghide_extract(input_image, passphrase)
print("Hint 3: We've made great memories and weve imagined amazing things; but at the end of it all we must say fin. Hes made mosty of cotton candy and some dreams the start of his name rhymes with ring.")
