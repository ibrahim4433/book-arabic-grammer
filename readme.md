# **📘 Modern Arabic Grammar Book using Web-to-Print process**

A modern, high-quality Arabic Grammar book project built with **HTML**, **CSS Paged Media**, and **Python**. This repository acts as a "Book Engine" that compiles individual HTML chapters into a single, print-ready PDF using WeasyPrint.

Target Audience: Middle School Students.  
Language: Modern Standard Arabic (MSA) with full Diacritics (Tashkeel).

## **🚀 Quick Start**

### **Prerequisites**

* Python 3.10 or higher  
* GTK3 libraries (Required for WeasyPrint)

### **Installation**

1. Clone the repository:  
   git clone \[https://github.com/ibrahim4433/book-arabic-grammer.git](https://github.com/ibrahim4433/book-arabic-grammer.git)  
   cd arabic-grammar-book

2. Install Python dependencies:  
   pip install \-r requirements.txt

### **Building the Book**

To generate the PDF, run the build script:

python build.py

The final PDF will be generated at: output/book.pdf

## **📂 Project Structure**

* **/pages**: Contains the source content. Each chapter is a separate .html file (e.g., 01\_intro.html).  
* **/styles**: Contains the CSS files. main.css controls the global layout and A4 dimensions.  
* **/assets**: Stores images and fonts.  
* **build.py**: The Python automation script that merges pages and renders the PDF.

## **✍️ Contribution Guidelines**

**Adding a New Chapter:**

1. Create a new file in /pages/ following the naming convention: XX\_topic\_name.html.  
2. Ensure the file starts with:  
   \<\!DOCTYPE html\>  
   \<html lang="ar" dir="rtl"\>

3. Link the stylesheet:  
   \<link rel="stylesheet" href="../styles/main.css"\>

4. Write your content using the approved semantic HTML tags (\<article\>, \<h1\>, .grammar-box).

**Design Rules:**

* **No Inline Styles:** Use classes defined in CODING\_STANDARDS.md.  
* **A4 Layout:** Do not change the global @page settings in main.css.  
* **Diacritics:** All Arabic text must include full Tashkeel.

## **🛠️ Technical Documentation**

For detailed technical constraints and architecture, please refer to:

* [TECH\_STACK.md](https://github.com/ibrahim4433/book-arabic-grammer/blob/main/TECH_STACK.md) \- Frameworks and strict constraints.  
* [ARCHITECTURE.md](https://github.com/ibrahim4433/book-arabic-grammer/blob/main/ARCHITECTURE.md) \- File structure and build logic.  
* [CODING\_STANDARDS.md](https://github.com/ibrahim4433/book-arabic-grammer/blob/main/CODING_STANDARDS.md) \- HTML/CSS rules and snippets.
