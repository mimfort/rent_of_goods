import asyncio
from logging.config import fileConfig

from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import AsyncConnection
from alembic import context

from app.categories.models import Category
from app.database import Base
from app.users.models import User
from app.goods.models import Good
from app.categories.models import Category
from app.rentals.models import Rental
# Загружаем конфигурацию Alembic
config = context.config

# Настройка логирования
fileConfig(config.config_file_name)

# Указываем метаданные
target_metadata = Base.metadata
print(Base.metadata.tables.keys())

def run_migrations_offline():
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


async def run_migrations_online():
    """Run migrations in 'online' mode."""
    connectable = create_async_engine(
        config.get_main_option("sqlalchemy.url"),
        poolclass=None,  # NullPool можно использовать, если не требуется пул соединений
    )

    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)


def do_run_migrations(connection: AsyncConnection):
    """Выполнение миграций в синхронном режиме."""
    context.configure(
        connection=connection,
        target_metadata=target_metadata,
    )

    with context.begin_transaction():
        context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    asyncio.run(run_migrations_online())
