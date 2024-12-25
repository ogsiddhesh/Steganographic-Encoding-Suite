# Steganographic-Encoding-Suite
Steganographic-Encoding-Suite explores the application of steganography for secure communication, data integrity verification, and digital watermarking within image files. 

Steganographic-Encoding-Suite provides a secure method for embedding sensitive data within digital images. This tool leverages LSB steganography to conceal information, offering a discreet communication channel for various applications.

# Steganographic-Encoding-Suite

A Python tool for image steganography using Least Significant Bit (LSB) encoding. This tool allows you to hide text messages within image files.

## Description

This tool implements LSB steganography to embed text data within the least significant bits of an image's pixel values. This makes the hidden message virtually undetectable to the human eye.

## Features

*   Encodes text messages into PNG and other image formats.
*   Decodes hidden messages from encoded images.
*   Uses NumPy for efficient pixel manipulation.
*   Error handling for file operations and message length.
*   Simple command-line interface.

## Installation

1.  Clone the repository:
    ```bash
    git clone [https://github.com/ogsiddhesh/Steganographic-Encoding-Suite.git](https://github.com/ogsiddhesh/Steganographic-Encoding-Suite.git)
    ```
2.  Navigate to the project directory:
    ```bash
    cd Steganographic-Encoding-Suite
    ```
3.  Create a virtual environment (recommended):
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate  # Linux/macOS
    .venv\Scripts\activate      # Windows
    ```
4.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

```bash
python Steganographic-Encoding-Suite.py  
