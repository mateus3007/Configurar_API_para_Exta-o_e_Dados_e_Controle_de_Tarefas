from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from crud.crud import add_user, add_task, get_tasks_by_user

# Conectar com o banco de dados SQLite
engine = create_engine('sqlite:///base_tarefas.db')
Session = sessionmaker(bind=engine)
session = Session()

# Adicionar um novo usuário
user = add_user(session, "Mateus de Araujo", "mateus@example.com")

# Adicionar uma nova tarefa para o usuário
task = add_task(session, "Terminar o projeto de gerenciamento de tarefas", "Alta", "Em andamento", user.id)

# Buscar todas as tarefas do usuário
tasks = get_tasks_by_user(session, user.id)
for t in tasks:
    print(t.task, t.priority, t.status)
