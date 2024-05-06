import streamlit as st


def discovery(show: bool = True) -> None:
    """
    Discovery component. Display the LLM discovery step.
    """

    with st.status("Discovery", expanded=st.session_state["show_discovery"]):
        if st.session_state["discovery_ran"] == False:
            st.session_state["discovery"].run()
            st.session_state["discovery_summary"] = st.session_state["discovery"].discovery
        st.write(st.session_state["discovery_summary"])
        st.session_state["discovery_ran"] = True
        st.session_state["show_initial_data_model"] = True
