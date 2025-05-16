import os
import base64

def encode_pdf_to_base64(pdf_file_path, output_file_path="encoded_pdf.txt"):
    """
    Reads a PDF file, encodes it to Base64, and writes the Base64 string to a text file.

    Args:
        pdf_file_path (str): The path to the PDF file.
        output_file_path (str, optional): The path to the output text file.
            Defaults to "encoded_pdf.txt".

    Returns:
        str:  The Base64 encoded string.  Also writes this string to a file.
              Returns None on error.
    """
    if not os.path.exists(pdf_file_path):
        print(f"Error: File not found at {pdf_file_path}")
        return None

    try:
        with open(pdf_file_path, "rb") as pdf_file:
            pdf_content = pdf_file.read()
            encoded_string = base64.b64encode(pdf_content).decode("ascii")
    except Exception as e:
        print(f"Error encoding PDF: {e}")
        return None

    try:
        with open(output_file_path, "w") as text_file:
            text_file.write(encoded_string)
        print(f"Base64 encoded string written to {output_file_path}")
    except Exception as e:
        print(f"Error writing to output file: {e}")
        return encoded_string # Return even if writing to file fails.

    return encoded_string

if __name__ == "__main__":
    # Hardcoded paths (replace with your actual paths)
    pdf_path = "C:\\Users\\Administrator\\Documents\\testsdir\\dummytestpdf.pdf"  # Replace with the actual path to your PDF
    output_path = "C:\\Users\\Administrator\\Documents\\testsdir\\testop\\empT_file_dummytextpdfencoded.txt"  # Replace with the path to your empty text file

    encoded_data = encode_pdf_to_base64(pdf_path, output_path)
    if encoded_data:
        print(f"Base64 string is ready. It has been saved to {output_path}")
    else:
        print("An error occurred. Please check the file path and try again.")
