# TerabytePichauKabumPrices
A Python script to fetch product prices from Brazilian online stores: Terabyte, Pichau, and Kabum.
Um script escrito em Python para procurar preços das lojas: Terabyte, Pichau e Kabum

## Instalação

1. Instale as dependências:

   pip install playwright

2. Instale o Firefox para o Playwright:

   playwright install firefox
   
Isso configura o ambiente necessário para rodar o script.


## Exemplo

```python
from kpt.price_scraper import process_sites
from pprint import pprint

sites = [
    ("kabum", 
     "https://www.kabum.com.br/produto/581685/placa-de-video-rtx-4060-infinity-2-palit-nvidia-geforce-8gb-gddr6-"
     "dlss-ray-tracing-g-sync-ne64060019p1-1070l"), 
    ("pichau", 
     "https://www.pichau.com.br/placa-de-video-msi-geforce-rtx-4060-ventus-2x-oc-8gb-gddr6-128-bit-white-"
     "912-v516-030"),  
    ("terabyte", 
     "https://www.terabyteshop.com.br/produto/25236/placa-de-video-gigabyte-nvidia-geforce-rtx-4060-eagle-"
     "oc-8gb-gddr6-dlss-ray-tracing-gv-n4060eagle-oc-8gd"),  
    ("kabum", 
     "https://www.kabum.com.br/produto/469132/placa-de-video-rtx-4060-ventus-2x-black-oc-msi-nvidia-geforce-"
     "8gb-gddr6-dlss-ray-tracing"),   
    ("pichau", 
     "https://www.pichau.com.br/placa-de-video-pny-geforce-rtx-4060-ti-verto-dual-fan-oc-8gb-gddr6-128-bit-"
     "vcg4060t8dfxpb1-o"),  
    ("terabyte", 
     "https://www.terabyteshop.com.br/produto/25235/placa-de-video-gigabyte-nvidia-geforce-rtx-4060-windforce-"
     "oc-8gbgddr6-dlss-ray-tracing-gv-n4060wf2oc-8gd"),  
    ("kabum", 
     "https://www.kabum.com.br/produto/461395/placa-de-video-rtx-4060-ti-ventus-3x-8g-oc-msi-nvidia-geforce-"
     "8-gbd6-dlss-ray-tracing"), 
    ("pichau", 
     "https://www.pichau.com.br/placa-de-video-gigabyte-geforce-rtx-4060-aero-oc-8gb-gddr6-128-bit-"
     "gv-n4060aero-oc-8gd"),  
    ("terabyte", 
     "https://www.terabyteshop.com.br/produto/25153/placa-de-video-gigabyte-nvidia-geforce-rtx-4060-ti-aero-"
     "oc-8gb-gddr6-dlss-ray-tracing-gv-n406taero-oc-8gd")
]

results = process_sites(sites)

pprint(results)
```


### Resultado

``` 
[(2299.9, 2705.76),
 (2325.57, 1999.99),
 (2899.99, 3411.75),
 (2159.9, 2541.06),
 (3117.64, 2649.99),
 (2299.99, 2705.87),
 (2999.9, 3529.29)]
```

## Problemas conhecidos
- O gerenciamento de erros causados for falta de estoque, por exemplo, não está totalmente implementado. Farei isso futuramente.

## Licença
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Agradecimentos
Obrigado ao Playwright pela incrível biblioteca de automação
