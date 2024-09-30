from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#CONEXAO
e = create_engine("sqlite:///base_tarefas.db", echo=True)

#SESSAO
session = sessionmaker(bind=e)


#SELECT
def ler_user(modelo):
    with session() as s:
        rows = s.query(modelo).all()

        for row in rows:
            print(row.dict())


#TASK
# 1) INSERIR 2 task para um usuario
# 2) Apresente as informações da tarefa com o uso do s.query(Task).all()

def inserir_tasks(tasks):
    with session() as s:
        for task in tasks:
            s.add(task)
        s.commit()


def mostrar_tasks(model):
    with session() as s:
        rows = s.query(model).all()

        for row in rows:
            print(row.dict())


def get_userid(name_in):
    with session() as s:
        user = s.query(User).filter_by(name = name_in).first()
        return user.id