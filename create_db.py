from app.db.database import engine, metadata
from app.models import movie_model  

def main():
    print("🔧 Criando o banco de dados e as tabelas...")
    metadata.create_all(bind=engine)
    print("✅ Banco criado com sucesso!")

if __name__ == "__main__":
    main()
