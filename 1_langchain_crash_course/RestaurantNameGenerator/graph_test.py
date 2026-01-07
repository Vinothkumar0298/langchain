from langgraph.graph import StateGraph,START,END
#from convert_test import handle_inr_convert,handle_portfolio,converter
from RestaurantNameGenerator.Portfolio import Portfolio, get_total_invested_amount, get_total_profit_or_loss_amount, \
    get_tax_amount

state = StateGraph(Portfolio)
#state.add_node('handle_portfolio',handle_portfolio)
#state.add_node('handle_inr_convert',handle_inr_convert)

#state.add_edge(START,'handle_portfolio')
#state.add_edge('handle_portfolio','handle_inr_convert')
#state.add_edge('handle_portfolio',END)

state.add_node('get_total_invested_amount',get_total_invested_amount)
state.add_node('get_total_profit_or_loss_amount',get_total_profit_or_loss_amount)
state.add_node('get_tax_amount',get_tax_amount)

state.add_edge(START,'get_total_invested_amount')
state.add_edge('get_total_invested_amount','get_total_profit_or_loss_amount')
state.add_edge('get_total_profit_or_loss_amount','get_tax_amount')

gr = state.compile()

print(gr.invoke({'invested_amount': {"A":float(1000.0),"B":float(1200.0)},"current_value_of_your_investment":{"A":1200.0,"B":800.0}}))



