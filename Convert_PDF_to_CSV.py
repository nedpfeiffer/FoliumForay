import PyPDF2

def pdf_to_text(file_path, output_file_path):
    # Open the PDF file
    with open(file_path, 'rb') as file:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfReader(file)
        
        # Initialize an empty string for the text
        text = ''

        # Loop through each page in the PDF
        for page in pdf_reader.pages:
            # Extract text from the page and add it to the text string
            text += page.extract_text() + '\n'

    # Save the text to a file
    with open(output_file_path, 'w') as output_file:
        output_file.write(text)

    print(f'Text extracted and saved to {output_file_path}')

# Example usage
pdf_file_path = 'data.pdf'
output_file_path = 'data.txt'
pdf_to_text(pdf_file_path, output_file_path)
