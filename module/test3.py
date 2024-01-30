from typing import Any

from pydantic import BaseModel
from unstructured.partition.pdf import partition_pdf

raw_pdf_elements = partition_pdf(
    filename="statement_of_changes.pdf",
    extract_images_in_pdf=False,
    infer_table_structure=True,
    chunking_strategy="by_title",
    max_characters=4000,
    new_after_n_chars=3800,
    combine_text_under_n_chars=2000,
    image_output_dir_path=".",
)
