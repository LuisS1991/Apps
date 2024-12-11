from fastapi import status
from fastapi.responses import FileResponse



async def descargaractualizacion():
    return FileResponse("Releses/releses1.zip",status_code=status.HTTP_200_OK)