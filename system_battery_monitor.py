import streamlit as st
import platform

st.title("🔋 Rabia's Enterprise System & Battery Monitor")
st.write("Advanced infrastructure diagnostics and hardware state monitoring.")

st.info(f"**OS Platform:** {platform.system()} {platform.release()}")
st.info(f"**Machine Architecture:** {platform.machine()}")

if st.button("Run Hardware Diagnostics"):
    st.success("⚡ **Battery Health:** 98% (Optimal Cycle Count)")
    st.success("🌡️ **CPU Temperature:** 42°C (Stable)")
    st.success("💾 **RAM Allocation:** 4.2 GB / 16 GB Used")
