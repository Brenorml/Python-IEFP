from fastapi import FastAPI
from data import nomes
 
app = FastAPI() 
 
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/teste")
async def pag2():
    return {"message": "pagina teste"}

@app.get("/pedido/{pedido_id}")
async def pag2(pedido_id: int):...

@app.get("/pedido/")
async def pedidos():
    msg = []
    for i in range(len(nomes)):
        msg.append({f"nome {i}": nomes[i]})

    return msg

@app.get("/pedido2/")
async def pedidos2(slot: int = 0, max: int = 10):
    msg = []
    for i in range(slot, max):
        msg.append({f"nome {i}": nomes[i]})

    return msg


