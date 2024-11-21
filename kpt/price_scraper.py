import asyncio
from typing import Iterable, TypedDict

class Teste(TypedDict):
    url: str
    
    

        
async def _process_sites(product_list: Iterable):
    from playwright.async_api import async_playwright
    from .utils import configure_semaphore, acess_and_get_price
    
    store_block_rules = {
                    "pichau": ["fetch", "script", "manifest", "image", "font", "stylesheet", "media"],
                    "kabum": ["image", "font", "stylesheet", "script", "media", "manifest", "xhr", "fetch"],
                    "terabyte": ["manifest", "script", "stylesheet", "fetch", "preflight","image", "xhr","font"],
                    }
    
    
    async with async_playwright() as p:
        browser = await p.firefox.launch(headless=False)
        tasks = []
        results = []
        
        for product in product_list:
            context = await browser.new_context()
            await context.route("**/*", lambda route: route.abort() if route.request.resource_type in store_block_rules[product[0]] else route.continue_())
            tasks.append(acess_and_get_price(context, *product))

        results = await asyncio.gather(*tasks)
        
        await browser.close()

        return results


def process_sites(product_list: Iterable):
    return asyncio.run(_process_sites(product_list))


