import asyncio
import logging

from dotenv import load_dotenv

from chain import process_text

TEXTO = (
    "La API en FastAPI usa Redis como caché y PostgreSQL para persistencia. "
    "Las consultas tardan el doble por saturación del pool de conexiones "
    "de PostgreSQL. El servicio sigue disponible."
)


async def main() -> None:
    resultado = await process_text(TEXTO)
    print(resultado.model_dump_json(indent=2))


if __name__ == "__main__":
    load_dotenv()
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    asyncio.run(main())
