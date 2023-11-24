from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "issue" ADD "author_id" UUID NOT NULL;
        ALTER TABLE "issue" ADD CONSTRAINT "fk_issue_user_39da43b0" FOREIGN KEY ("author_id") REFERENCES "user" ("id") ON DELETE CASCADE;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "issue" DROP CONSTRAINT "fk_issue_user_39da43b0";
        ALTER TABLE "issue" DROP COLUMN "author_id";"""
