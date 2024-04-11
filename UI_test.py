import streamlit as st
from streamlit_extras.stylable_container import stylable_container

with stylable_container(
        key="green_button",
        css_styles="""
        button {
            background-color: green;
            color: white;
            border-radius: 20px;
        }
        """,
):
    st.button("Green button")

st.button("Normal button")

with stylable_container(
        key="container_with_border",
        css_styles="""
        {
            border: 1px solid rgba(49, 51, 63, 0.2);
            border-radius: 0.5rem;
            padding: calc(1em - 1px)
        }
        """,
):
    st.markdown("This is a container with a border.")

st.info(
    """
    Need a feature that's not on here?
    [Let us know by opening a GitHub issue!](https://github.com/streamlit/streamlit/issues)
    """,
    icon="👾",
)

st.caption('This is a string that explains something above.')
st.caption('A caption with _italics_ :blue[colors] and emojis :sunglasses:')