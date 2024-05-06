import streamlit as st


def iterate_model(show: bool = False) -> None:
    """
    Produces an updated model.
    """
    print("internal show: ", show)
    iteration = st.session_state["model_iteration"]
    with st.status(f"Data Model V{iteration}", expanded=show):

        if st.session_state["run_iterate_model"]:
            print(f"running iterate {iteration}...")
            st.session_state["modeler"].iterate_model(
                iterations=1, user_corrections=st.session_state["user_corrections"]
            )
            st.session_state["run_iterate_model"] = False

        st.json(st.session_state["modeler"].current_model, expanded=False)
        st.graphviz_chart(
            st.session_state["modeler"].current_model.visualize(),
            use_container_width=True,
        )
