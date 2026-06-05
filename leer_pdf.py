import PyPDF2

#abrir archivo PDF
with open('C:/Users/Sergio/Documents/PDFS/Matriz Catedra Constituyente.pdf', 'rb') as f:

    pdf_reader = PyPDF2.PdfReader(f)
    num_pages = len(pdf_reader.pages)

    print(f'Número de páginas: {num_pages} \n')

    for i,pagina in enumerate(pdf_reader.pages):
        texto = pagina.extract_text()
        print(f'Página {i+1}:\n{texto}\n')