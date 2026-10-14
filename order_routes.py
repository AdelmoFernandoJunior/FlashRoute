from fastapi import APIRouter, Depends, HTTPException
from dependecies import pegar_sessao
from schemas import PedidoSchema
from sqlalchemy.orm import Session
from models import Pedido

order_router = APIRouter()

@order_router.get("/")
async def pedidos():
    """
    Rota padrão de pedidos do nosso sistema.
    """
    return {"message": "Você está na rota de pedidos!"}

@order_router.post("/pedidos")
async def criar_pedido(pedido_schema: PedidoSchema, session = Depends(pegar_sessao)):
    novo_pedido = Pedido(
        status="Pendente",
        usuario_id=pedido_schema.usuario,
        preco_total=0,
    )
    session.add(novo_pedido)
    session.commit()
    return {"message": f"Pedido criado com sucesso. ID do pedido: {novo_pedido.id}"}

@order_router.get("/{pedido_id}")
async def verificar_pedido(pedido_id: int, session = Depends(pegar_sessao)):
    pedido = session.query(Pedido).filter_by(id=pedido_id).first()
    if pedido is None:
        raise HTTPException(status_code=404, detail="Pedido não encontrado.")

    return {
        "id": pedido.id,
        "status": pedido.status,
        "usuario_id": pedido.usuario_id,
        "preco_total": pedido.preco_total,
    }