import base64
from email.mime import base

from fastapi.responses import JSONResponse 
from converter import base64_para_pdf
from fastapi import FastAPI, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/uploadfile")
async def create_upload_file(arquivo: UploadFile):
    try:
        bytesArquivo = arquivo.file.read()
        base64_arquivo = base64.b64encode(bytesArquivo)

        sucesso, mensagem = base64_para_pdf(base64_arquivo, 'arquivo.pdf')

        if sucesso:
            # Aqui você pode fazer o processamento desejado com o conteúdo do arquivo (file_content)
            return JSONResponse(content={"message": "Arquivo recebido com sucesso"}, status_code=200)
        else:
            raise HTTPException(status_code=400, detail=mensagem)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/retornartexto")
def ler_texto():
    return "Retorna a mensagem para o front."
