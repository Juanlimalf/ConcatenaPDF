import os
import PyPDF2 as pdf
from glob import glob


def concatenaPdf(caminho):
    os.chdir(caminho)

    arquivos = glob('*.pdf')
    destino = r'concatenado\concatenado.pdf'

    if not os.path.exists('concatenado'):
        os.makedirs(r'.\concatenado')
        print('Diretório de destino criado\nProsseguindo...')
    else:
        print('Diretório de destino já existente\nProsseguindo...')
    try:
        pdfWriter = pdf.PdfFileWriter()

        for j in range(0, len(arquivos)):
            pdfDoc = open(arquivos[j], 'rb')

            pdfReader = pdf.PdfFileReader(pdfDoc)

            for k in range(0, pdfReader.numPages):
                pagina = pdfReader.getPage(k)
                pdfWriter.addPage(pagina)

            pdfResultado = open(destino, 'ab')
            pdfWriter.write(pdfResultado)
            
            pdfDoc.close()
            pdfResultado.close()
    except Exception as exc:
        print('Administrador: verificar existência de exceções')
        return str(exc)

    print(f'Arquivo gerado em:\n{os.getcwd()}\{destino}')
    return f'Arquivo gerado em:\n{os.getcwd()}\{destino}'

def main():
 
    caminho = input('coloque o caminho do arquivo: ')
    response = concatenaPdf(caminho)
    print("Processo Finalizado")

main()