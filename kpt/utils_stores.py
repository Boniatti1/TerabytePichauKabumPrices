import json
from playwright.async_api import Page
from typing import Tuple

# Kabum Features


async def kabum_price(page: Page, url) -> Tuple[float, float]:
    """
    Acess the site and get the price for the product
    Args:
        page (Page): Playwright Page object used to interact with the site
        url (str): URL for the product page
    Returns:
        tuple: A tuple containing two floats or None values:
            - clean_pix (float): The price for paying upfront
            - clean_card (float): The price for paying in installments
    """
    
    script = await page.query_selector('#__NEXT_DATA__')
    script_content = await script.text_content()
    data = json.loads(script_content)
    kabum_prices = data["props"]["pageProps"]["initialZustandState"]["descriptionProduct"]["priceDetails"]
    
    clean_pix = float(kabum_prices["price"])
    clean_card = float(kabum_prices["discountPrice"])
    
    return (clean_pix,clean_card)


# Terabyte Features


async def terabyte_price(page: Page, url: str) -> Tuple[float, float]:
    """
    Acess the site and get the price for the product
    Args:
        page (Page): Playwright Page object used to interact with the site
        url (str): URL for the product page
    Returns:
        tuple: A tuple containing two floats or None values:
            - clean_pix (float): The price for paying upfront
            - clean_card (float): The price for paying in installments
    """

    # There are three elements with the id valVista. Therefore, there was a need to use the CSS selector
    element_pix = await page.query_selector('#valVista')
    price_pix = await element_pix.text_content()

    element_card = await page.query_selector('p.val-parc:nth-child(1) > span:nth-child(1)')
    price_card = await element_card.text_content()
    
    clean_pix = float(price_pix.replace('R$', '').replace('.', '').replace(',', '.').strip())
    clean_card = float(price_card.replace('R$', '').replace('.', '').replace(',', '.').strip())
    
    return (clean_pix, clean_card)



# Pichau Features


async def pichau_price(page: Page, url) -> Tuple[float, float]:
    """
    Acess the site and get the price for the product
    Args:
        page (Page): Playwright Page object used to interact with the site
        url (str): URL for the product page
    Returns:
        tuple: A tuple containing two floats or None values:
            - clean_pix (float): The price for paying upfront
            - clean_card (float): The price for paying in installments
    """
    
    script = await page.query_selector('#__NEXT_DATA__')
    script_content = await script.text_content()
    data = json.loads(script_content)
    pichau_prices = data["props"]["pageProps"]["pageData"]["content"]['pichau_prices']
    
    clean_pix = float(pichau_prices["avista"])
    clean_card = float(pichau_prices["final_price"])
    
    return (clean_pix,clean_card)