from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "category" (
    "id" UUID NOT NULL  PRIMARY KEY,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "name" VARCHAR(100) NOT NULL
);
        CREATE TABLE IF NOT EXISTS "category_issue" (
    "issue_id" UUID NOT NULL REFERENCES "issue" ("id") ON DELETE CASCADE,
    "category_id" UUID NOT NULL REFERENCES "category" ("id") ON DELETE CASCADE
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "category_issue";
        DROP TABLE IF EXISTS "category";"""
