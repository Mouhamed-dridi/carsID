import easyocr
from translate import Translator
from PIL import Image

def extract_text(image_path):
    """Extracts text from the image."""
    reader = easyocr.Reader(['en', 'ar'])  # Initialize with languages you expect in the image
    result = reader.readtext(image_path, detail=0)
    return ' '.join(result)

def translate_text(text, target_language='en'):
    """Translates text into the target language."""
    translator = Translator(to_lang=target_language)
    translation = translator.translate(text)
    return translation

def main():
    image_path = '/home/myadmin/cars/tun2.jpg'
    
    # Extract text from the image
    extracted_text = extract_text(image_path)
    print("Extracted text:", extracted_text)
    
    # Translate the extracted text
    translated_text = translate_text(extracted_text, 'en')
    print("Translated text:", translated_text)

if __name__ == '__main__':
    main()
