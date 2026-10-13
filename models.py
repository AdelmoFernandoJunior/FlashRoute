from sqlalchemy import Boolean, Column, create_engine, Enum, Float, ForeignKey
from sqlalchemy import Integer, String
from sqlalchemy.orm import declarative_base

# cria a conexão com o banco de dados SQLite
db = create_engine('sqlite:///mydatabase.db')

# cria a base de dados para os modelos
Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(50), nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    senha = Column(String(10), nullable=False)
    ativo = Column(Boolean, default=True)
    admin = Column(Boolean, default=False)

    def __init__(self, nome, email, senha, ativo=True, admin=False):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo
        self.admin = admin

class Pedido(Base):
    __tablename__ = 'pedidos'

    STATUS_PEDIDOS = (
        ("Pendente", "Pendente"),
        ("Processando", "Processando"),
        ("Concluído", "Concluído"),
        ("Cancelado", "Cancelado")
    )

    id = Column(Integer, primary_key=True, autoincrement=True)
    status = Column(Enum(*[status[0] for status in STATUS_PEDIDOS]), nullable=False, default="Pendente")
    usuario_id = Column(Integer, ForeignKey('usuarios.id'), nullable=False)
    preco_total = Column(Float, nullable=False)

    def __init__(self, status, usuario_id, preco_total):
        self.status = status
        self.usuario_id = usuario_id
        self.preco_total = preco_total

class itemPedido(Base):
    __tablename__ = 'itens_pedido'

    id = Column(Integer, primary_key=True, autoincrement=True)
    pedido_id = Column(Integer, ForeignKey('pedidos.id'), nullable=False)
    produto = Column(String(50), nullable=False)
    quantidade = Column(Integer, nullable=False)
    preco_unitario = Column(Float, nullable=False)

    def __init__(self, pedido_id, produto, quantidade, preco_unitario):
        self.pedido_id = pedido_id
        self.produto = produto
        self.quantidade = quantidade
        self.preco_unitario = preco_unitario