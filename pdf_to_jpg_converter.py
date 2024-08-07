import os
from pdf2image import convert_from_path
import tkinter as tk
from tkinter import filedialog, messagebox

def convert_pdf_to_jpg(pdf_path, output_folder):
    pages = convert_from_path(pdf_path)
    pdf_filename = os.path.splitext(os.path.basename(pdf_path))[0]
    
    for i, page in enumerate(pages):
        jpg_filename = f"{pdf_filename}_page_{i+1}.jpg"
        page.save(os.path.join(output_folder, jpg_filename), "JPEG")
    
    print(f"Converted {pdf_filename}")

def batch_convert_pdfs():
    input_folder = filedialog.askdirectory(title="선택 PDF 파일이 있는 폴더")
    if not input_folder:
        return
    
    output_folder = filedialog.askdirectory(title="JPG 파일을 저장할 폴더 선택")
    if not output_folder:
        return
    
    pdf_files = [f for f in os.listdir(input_folder) if f.lower().endswith('.pdf')]
    
    if not pdf_files:
        messagebox.showinfo("알림", "선택한 폴더에 PDF 파일이 없습니다.")
        return
    
    for pdf_file in pdf_files:
        pdf_path = os.path.join(input_folder, pdf_file)
        convert_pdf_to_jpg(pdf_path, output_folder)
    
    messagebox.showinfo("완료", f"{len(pdf_files)}개의 PDF 파일 변환이 완료되었습니다.")

# GUI 설정
root = tk.Tk()
root.title("PDF to JPG Batch Converter")
root.geometry("300x100")

convert_button = tk.Button(root, text="PDF 폴더 선택 및 변환 시작", command=batch_convert_pdfs)
convert_button.pack(pady=20)

root.mainloop()