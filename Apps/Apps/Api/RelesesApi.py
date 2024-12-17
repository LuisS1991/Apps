from fastapi import status
from fastapi.responses import FileResponse


async def tst():
    return {"respuesta" :{"valor1:" :  "1050", "valor2:" :  "3205"}}

async def descargaractualizacion():
    return FileResponse("Releses/releses1.zip",status_code=status.HTTP_200_OK)