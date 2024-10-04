# Proyek-AnalisisData

# Set-up Enviroment Anaconda
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt

# Set-up requirements.txt
pip freeze > requirements.txt

# Streamlit Run App
streamlit run dashboard/dashboard.py
