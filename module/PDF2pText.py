import pdfplumber
from PIL.Image import Image
from tqdm import tqdm
from cnocr import CnOcr
import csv


def plain_text(ocr_list: list) -> str:
    """
    Convert OCR list to plain text
    param ocr_list: OCR list
    return: plain text
    """
    text = ""
    for line in ocr_list[1:]:
        text += line['text']
    return text


def pdf_to_image_sequence(file_path: str) -> list[Image]:
    """
    Convert PDF to a sequence of images using pdfplumber
    param file_path: PDF file path
    return: List of Image objects
    """
    images = []
    with pdfplumber.open(file_path) as pdf:
        for page in tqdm(pdf.pages, desc="PDF to Image"):
            image = page.to_image(resolution=150)
            images.append(image)
    return images


def image_sequence_to_text(file_path: str) -> list[str]:
    """
    Convert a sequence of images to text using CnOCR
    param file_path: PDF file path
    return: text_list
    """
    images = pdf_to_image_sequence(file_path)
    ocr = CnOcr()
    text_list = []
    for image in tqdm(images, desc="Image to Text"):
        text_list.append(ocr.ocr(image))
    return text_list


if __name__ == "__main__":
    # Example
    images = pdf_to_image_sequence("document/ImageProcessing.pdf")
    ocr = CnOcr(rec_model_name='densenet_lite_136-fc',
                det_model_name='db_shufflenet_v2_small', det_more_configs={'rotated_bbox': False})
    text = ""
    context_images = images[1:17]+images[20:58]+images[62:119]+images[124:190]+images[402:437]+images[433:507]
    for image in tqdm(context_images, desc="Image to Text"):
        res = ocr.ocr(image.original)  # Convert PageImage to PIL image
        text += plain_text(res)
    with open("example.txt", "w") as file:
        file.write(text)
    # text_list = image_sequence_to_text("document/ImageProcessing.pdf")
    print(text)
    images[30].save("example.png")   # Save first page as PNG
