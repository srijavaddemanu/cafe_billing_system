import streamlit as st

#title
st.title("Cafe Billing System")

#menu 
menu = {
    "Coffee" : 180,
    "Burger" : 200,
    "French Fries" : 130,
    "Pizza" : 250,
    "Cool Drink" : 120,
}

st.subheader("Select items")
total = 0
bill = []
#input quantities
for item,price in menu.items():
    qty = st.number_input(f"{item} - {price}",min_value=0,step = 1,key=item)
    if qty>0:
        item_total = qty * price
        total += item_total
        bill.append((item,qty,item_total))

#gst calculation
gst = total * 0.05
final_total = total + gst

# bill receipt
st.header("Bill receipt")

for item, qty, item_total in bill:
    st.write(f"{item} x {qty} : {item_total}")
    
st.write(f"sub_total : {total}")
st.write(f"GST 5% : {gst}")
st.success(f"Final Total : {final_total}")


