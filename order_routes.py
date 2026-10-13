from fastapi import APIRouter

order_router = APIRouter()

@order_router.get("/")
async def pedidos():
    """
    Rota padrão de pedidos do nosso sistema.
    """
    return {"message": "Você está na rota de pedidos!"}
