# blockchain_streamlit.py
import streamlit as st
from blockchain import Blockchain

# Initialize blockchain
blockchain = Blockchain()

st.title("💸 Blockchain Donation Tracker")
st.write("Record donations securely on a blockchain ledger.")

# Donation form
with st.form("donation_form"):
    donor_id = st.text_input("Donor ID")
    donor_name = st.text_input("Donor Name")
    amount = st.number_input("Donation Amount", min_value=1)
    organization = st.text_input("Organization Name")
    submitted = st.form_submit_button("Donate")

    if submitted:
        blockchain.new_donation(donor_id, donor_name, amount, organization)
        block = blockchain.new_block(proof=12345)
        st.success(f"✅ Donation recorded in block #{block['index']}")

# Display blockchain
if st.checkbox("Show full blockchain"):
    for block in blockchain.chain:
        st.write(f"### Block {block['index']}")
        st.write(block)
        st.write("---")
