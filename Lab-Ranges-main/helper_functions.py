import pandas as pd
import openai
from pdf2image import convert_from_path
import pytesseract
from PIL import Image
from keys import openai_api_key 

openai.api_key = openai_api_key

def csv_to_df(csv_file):
    # Load the CSV file into a pandas DataFrame
    df = pd.read_csv(csv_file)
    return df

def pdf_to_image(filename):
    pdf_file = filename + ".pdf"
    image_file = filename + ".png"
    # Convert the PDF to an image
    images = convert_from_path(pdf_file)

    # Save the images
    for i, image in enumerate(images):
        image.save(image_file)

def image_to_text(filename):
    image_file = filename + ".png"
    # Open the image file
    image = Image.open(image_file)
    # Use pytesseract to recognize text from the image
    text = pytesseract.image_to_string(image)
    return text

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
    model=model,
    messages=messages,
    temperature=0,)
    return response.choices[0].message["content"]

def prompt_ai(text):
    prompt = "convert this into a table and give me the .csv code for the table."+ text
    response = get_completion(prompt)
    return response

def text_to_csv(filename,response):
    csv_data = response
    # Specify the file path where you want to save the CSV file
    filename = filename + "_predicted.csv"

    # Open the file in write mode and write the CSV data to it
    with open(filename, "w") as csv_file:
        csv_file.write(csv_data)

def pdf_to_csv(filename):
    pdf_to_image(filename)
    text = image_to_text(filename)
    response = prompt_ai(text)
    text_to_csv(filename,response)

def director(pdf_file):
    pdf_file = pdf_file[:-4]
    pdf_to_csv(pdf_file)
    df = csv_to_df(pdf_file + '_predicted.csv')
    return df