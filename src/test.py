from typing import Dict, Any

import re

# pattern = r'\[C(\d+):([a-f0-9]{64}):([^\]]+)\]'
pattern = r'\[(C\d+):([a-f0-9]{64}):([^\]]+)\]'
IGM_DELIMITERS: Dict[str, str] = {
    "START": "[",
    "END": "]",
    "SEP": ":"
}
start, sep, end = IGM_DELIMITERS['START'], IGM_DELIMITERS['SEP'], IGM_DELIMITERS['END']
escaped_end = re.escape(end)
# pattern = rf'\{start}(\w+)\{sep}([a-f0-9]{64})\{sep}([^{escaped_end}]+)\{end}'
        
text = """
One of the earliest recorded forms of cryptographic schemes was hieroglyphic substitution ciphers, employed by the ancient Egyptians [C1:bde5367d315989513314bc1faacd300d79f68e87c439dd7898a7cacee0b859d9:#post-12113 > div:nth-of-type(3) > p:nth-of-type(3)].
--- SSR_START ---
[
  {
    "SHI": "bde5367d315989513314bc1faacd300d79f68e87c439dd7898a7cacee0b859d9",
    "Type": "Web Article",
    "Canonical_URI": "https://nhsjs.com/2024/the-evolution-of-cryptography-and-a-contextual-analysis-of-the-major-modern-schemes/",
    "Location_Type": "CSS_Selector",
    "Loc_Selector": "#post-12113 > div:nth-of-type(3) > p:nth-of-type(3)"
  }
]
--- SSR_END ---
"""
 
for match in re.finditer(pattern, text, re.IGNORECASE):
    print(match.groups())
