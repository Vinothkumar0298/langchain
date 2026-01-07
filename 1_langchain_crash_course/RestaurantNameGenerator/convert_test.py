from typing import TypedDict, Dict


class converter(TypedDict):
    total_amount: Dict[str,float]
    portfolio_amount: float
    to_inr_amount: float
    """
    dist_value = {'total_amount':total_amount,
                  'portfolio_amount':portfolio_amount,
                  'to_inr_amount':to_inr_amount}
              """


def handle_portfolio(holder: converter) -> converter:
    holder['portfolio_amount'] = sum(holder['total_amount'].values()) * int(1.08)


    return holder


def handle_inr_convert(holder: converter) -> converter:
    holder['to_inr_amount'] = holder['portfolio_amount'] * 89.0
    return holder
