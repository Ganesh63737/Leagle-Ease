# app.py

if st.session_state.get("show_edit"):
    edited_text = st.text_area(
        "Edit Document Below:",
        generated_text,
        height=300
    )
    st.session_state.generated_text = edited_text

# Downloads
st.download_button(
    "Download as .TXT",
    data=generated_text,
    ...
)

st.download_button(
    "Download as .DOCX",
    data=format_docx(...),
    ...
)

st.download_button(
    "Download as .PDF",
    data=format_pdf(...),
    ...
)