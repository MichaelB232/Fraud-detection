import sys

from sqlalchemy import text

from app.db.session import engine


def main() -> None:
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT version();"))
            version = result.scalar()
            print("✅ Database connection successful.")
            print(f"   Postgres version: {version}")
    except Exception as e:
        print("❌ Database connection failed.")
        print(f"   Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
