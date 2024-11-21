from playwright.async_api import BrowserContext
import asyncio
from typing import Tuple


def configure_semaphore(limit: int = None):
    global sem
    if limit is None:
        import os
        limit = os.cpu_count() or 4

    sem = asyncio.Semaphore(limit)
    

async def acess_and_get_price(context: BrowserContext, store: str, url: str) -> Tuple[float, float]:
    from .utils_stores import terabyte_price, pichau_price, kabum_price
    
    configure_semaphore()
    
    async with sem:
        page = await context.new_page()
        await page.goto(url,wait_until="domcontentloaded")
        
        if store == "kabum":
            prices = await kabum_price(page, url)
        elif store == "terabyte":
            prices = await terabyte_price(page, url)
        elif store == "pichau":
            prices = await pichau_price(page, url)

        await page.close()
        
        return prices



