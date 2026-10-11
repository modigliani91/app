import streamlit as st

st.set_page_config(page_title="Text File Reader", page_icon="📄")

st.title("📄 Text File Reader")
st.write("Upload a `.txt` file to view its contents.")

uploaded_file = st.file_uploader("Choose a text file", type=["txt"])

if uploaded_file is not None:
    # Decode bytes to text, replacing any characters that can't be decoded
    text = uploaded_file.read().decode("utf-8", errors="replace")

    st.subheader(f"File: {uploaded_file.name}")

    # Basic statistics
    lines = text.splitlines()
    words = text.split()
    col1, col2, col3 = st.columns(3)
    col1.metric("Lines", len(lines))
    col2.metric("Words", len(words))
    col3.metric("Characters", len(text))

    # Optional search within the file
    query = st.text_input("Search for a word or phrase (optional)")
    if query:
        matches = [(i + 1, line) for i, line in enumerate(lines) if query.lower() in line.lower()]
        st.write(f"Found **{len(matches)}** matching line(s).")
        for line_no, line in matches:
            st.text(f"{line_no}: {line}")

    # Full contents
    st.subheader("Contents")
    st.text_area("File contents", text, height=400)

    # Let the user download the text back
    st.download_button(
        label="Download file",
        data=text,
        file_name=uploaded_file.name,
        mime="text/plain",
    )
else:
    st.info("Waiting for a file to be uploaded.")
