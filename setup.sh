mkdir -p ~/.streamlit
echo "[server]
headless = true
port = $PORT
enableCORS = false

[theme]
primaryColor='#f63366'
backgroundColor='#0e1117'
secondaryBackgroundColor='#31333F'
textColor='#fafafa'
font='sans serif'
" > ~/.streamlit/config.toml
