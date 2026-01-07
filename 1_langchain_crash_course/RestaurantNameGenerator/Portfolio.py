from typing import TypedDict, Dict

from langchain_core.tools import tool


class Portfolio(TypedDict):
    invested_amount: Dict[str, float]
    current_value_of_your_investment: Dict[str, float]

    total_profit_amount: float = 0
    total_loss_amount: float = 0
    tax_amount: float = 0
    total_profit_or_loss: float = 0
    total_current_asset_values: float = 0
    total_invested_amount: float = 0
    messages: list = []


def get_total_invested_amount(state: Portfolio) -> Portfolio:
    """calculate the total amount of the investments"""
    state['total_invested_amount'] = sum(state['invested_amount'].values())

    return state


def get_total_profit_or_loss_amount(state: Portfolio) -> Portfolio:
    """calculate the profit or loss of the investments"""

    for (invest_info, val) in state['current_value_of_your_investment'].items():

        if state['current_value_of_your_investment'][invest_info] >= state['invested_amount'][invest_info]:
            state['total_profit_amount'] += state['current_value_of_your_investment'][invest_info] - \
                                            state['invested_amount'][invest_info]
        else:
            state['total_loss_amount'] += state['invested_amount'][invest_info] - \
                                          state['current_value_of_your_investment'][
                                              invest_info]

    state['total_profit_or_loss'] = state['total_profit_amount'] - state['total_loss_amount']
    return state


def get_tax_amount(state: Portfolio) -> Portfolio:
    """get the tax amount based on the total profit amount is made with investment"""
    tax_amount = 0.0
    if state['total_profit_or_loss'] <= 1000:
        tax_amount = 0.0

    elif state['total_profit_or_loss'] >= 1000 & int(state['total_profit_or_loss']) <= 10000:
        tax_amount = state['total_profit_or_loss'] * 0.10
    elif state['total_profit_or_loss'] >= 10000 & int(state['total_profit_or_loss']) <= 100000:
        tax_amount = state['total_profit_or_loss'] * 0.20
    else:
        tax_amount = state['total_profit_or_loss'] * 0.30

    state['tax_amount'] = tax_amount
    return state
