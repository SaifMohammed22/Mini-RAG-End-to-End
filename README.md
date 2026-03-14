# Mini-RAG End-to-End App

This is a minimal end-to-end implementation of a Retrieval-Augmented Generation (RAG) system for question answering. The application leverages a vector database for document retrieval and a language model for generating answers based on the retrieved documents.

## Requirements

- Python 3.10 or higher
- fastapi
- uvicorn

## Installation

### Install the required packages

1. Clone the repository:
   ```bash
    git clone https://github.com/SaifMohammed22/Mini-RAG-End-to-End.git
    cd Mini-RAG-End-to-End
    ```
3. Create and activate a virtual environment (optional but recommended) with Miniconda:
    ```bash
    conda create -n mini-rag-env python=3.10 -y
    conda activate mini-rag-env
    ```
2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

### Set up environment variables
1. Create a `.env` file in the root directory of the project.
2. Copy the contents of `.env.example` into your `.env` file using this command:
    ```bash
    cp .env.example .env
    ```
3. Replace the placeholder values with your actual API keys and configurations.