# this script uses steghide to automate the extracting and printing of a python script that was encrypted in an image 

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
    input_image = "/image.jpg"
    output_file = "/secretmessage.py"
    passphrase = "apple"  # Leave empty if not encrypted

    steghide_extract(input_image, passphrase)
print("Extracted Message Goes Here")
