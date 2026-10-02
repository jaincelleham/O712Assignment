import streamlit as st
from starter import COSTS, TIME_BLOCKS, ZONES, delivery_times


def cost_per_late_order(costs):
  refund = costs["refund"]
  lost_profit = costs["churn_orders"] * costs["margin"]
  return refund + lost_profit


def net_profit(zone, time_block, promise, costs):
  times = delivery_times(zone, time_block, promise, seed = 1)

  orders = len(times)
  profit = orders * costs["margin"]

  late_count = (times > promise).sum()
  late_cost = late_count * cost_per_late_order(costs)

  return profit - late_cost


def best_promise(zone, time_block, promise, costs, seed = 1):
  best_promise = promise[0]
  best_profit = net_profit(zone, time_block, best_promise, costs)

  for p in promise:
    profit = net_profit(zone, time_block, p, costs)
    if profit > best_profit:
      best_promise = p
      best_profit = profit
  return best_promise, round(float(best_profit),2)


possible_promises = list(range(5, 55, 5))

st.title("Rosa's Delivery Promise")
st.write("Choose a zone and time block to find the most profitable promise.")

zone = st.selectbox("Zone", ZONES)
time_block = st.selectbox("Time block", TIME_BLOCKS)

promise, profit = best_promise(
  zone,
  time_block,
  possible_promises,
  COSTS,
  seed = 1,
)

st.metric("Best promise", f"{promise} minutes")
st.metric("Net profit", f"${profit:.2f}")