#!/usr/bin/env bash
# Domino launch script for the Streamlit text-file reader (app.py).
# Domino apps must listen on 0.0.0.0:8888.
#
# CORS and XSRF protection are turned off because Domino serves the app
# through its own reverse proxy. With them on, file uploads
# (st.file_uploader) often fail with a 403 error.

streamlit run app.py \
  --server.port=8888 \
  --server.address=0.0.0.0 \
  --server.headless=true \
  --server.enableCORS=false \
  --server.enableXsrfProtection=false
