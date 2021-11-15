from pyracing import client as pyracing
import os
import asyncio
import dotenv

dotenv.load_dotenv()

class IracingIndexer:
    def __init__(self):
        self.pyracing = self.init_pyracing()

    async def index_iracing(self):
        all_series = await self.pyracing.current_seasons(series_id=True)
        print('hello')

    def init_pyracing(self):
        return pyracing.Client(
            os.getenv("IRACING_USERNAME"),
            os.getenv("IRACING_PASSWORD")
        )


if __name__ == '__main__':
    indexer = IracingIndexer()
    asyncio.run(indexer.index_iracing())
