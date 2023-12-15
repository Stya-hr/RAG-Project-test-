from langchain.text_splitter import RecursiveCharacterTextSplitter
import random


def text_splitter(txt_path: str) -> list[str]:
    # This is a long document we can split up.
    with open(txt_path) as f:
        state_of_the_union = f.read()

    text_splitter = RecursiveCharacterTextSplitter(
        # Set a really small chunk size, just to show.
        chunk_size=64,
        chunk_overlap=8,
        length_function=len,
    )

    texts = text_splitter.create_documents([state_of_the_union])

    return texts

if __name__ == "__main__":
    texts = text_splitter("example.txt")
    random_texts = random.sample(texts, 20)
    print(*random_texts, sep='\n\n')
    print(len(texts))