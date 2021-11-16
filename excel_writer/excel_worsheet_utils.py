from typing import TypedDict,Literal
from enum import Enum
import pandas as pd

class cell_format(TypedDict, total=False):
    border: int
    left: int
    right: int
    top: int
    bottom: int
    border_color: str
    bold: bool
    num_format: str
    align: Literal[ 'align',	
                    'valign',
                    'rotation',
                    'text_wrap',
                    'reading_order',
                    'text_justlast',
                    'center_across',
                    'indent',
                    'shrink']