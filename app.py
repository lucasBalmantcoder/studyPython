import datetime
import os
import click
from flask import Flask, current_app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
import sqlalchemy as sa
from flask_migrate import Migrate, migrate


# Base do SQLAlchemy
class Base(DeclarativeBase):
    pass


# Instância do SQLAlchemy com modelo base
db = SQLAlchemy(model_class=Base)
migrate = Migrate()



# Modelo User
class User(Base):
    __tablename__ = "user"
    
    id: Mapped[int] = mapped_column(sa.Integer, primary_key=True)
    username: Mapped[str] = mapped_column(sa.String(100), unique=True, nullable=False)

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, username={self.username!r})"


# Modelo Post
class Post(Base):
    __tablename__ = "post"
    
    id: Mapped[int] = mapped_column(sa.Integer, primary_key=True)
    title: Mapped[str] = mapped_column(sa.String(100), nullable=False)
    body: Mapped[str] = mapped_column(sa.String(100), nullable=False)
    created: Mapped[datetime.datetime] = mapped_column(
        sa.DateTime, server_default=sa.func.now()
    )
    author_id: Mapped[int] = mapped_column(sa.Integer, sa.ForeignKey("user.id"))

    def __repr__(self) -> str:
        return f"Post(id={self.id!r}, title={self.title!r})"


# Comando CLI para inicializar o banco de dados
@click.command("init-db")
def init_db_command():
    with current_app.app_context():
        db.create_all()
    click.echo("Initialized the database")


# Função para criar e configurar a aplicação
def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    # Configuração padrão
    app.config.from_mapping(
        SECRET_KEY="dev",
        SQLALCHEMY_DATABASE_URI="sqlite:///db.sqlite",
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )

    # Configuração externa (ex: config.py)
    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)

    # Garante que o diretório instance/ existe
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Comandos CLI
    app.cli.add_command(init_db_command)

    # Inicializa o banco de dados
    db.init_app(app)
    migrate.init_app(app, db)  # <- Aqui funciona agora

    # Registro de blueprints (verifique se os arquivos existem)
    from pj_flask.src.controllers.user import app as user
    # from pj_flask.src.controllers import 
    app.register_blueprint(user)
    # app.register_blueprint(post)

    return app
