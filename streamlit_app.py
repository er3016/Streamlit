import streamlit as st
import matplotlib.pyplot as plt
import os
#from projects import combined_mdi, mdi, dpi, vx, ek

def main():
    plt.rcParams["figure.figsize"] = (10,4)

    st.title("SonoVx")

    st.sidebar.title("Menu")
    if 'task' not in st.session_state:
        st.session_state.task = 'Preprocessing'
    if st.sidebar.button("Preprocessing"):
        st.session_state.task = 'Preprocessing'
    if st.sidebar.button("Models"):
        st.session_state.task = "Models"
    if st.sidebar.button("Evaluation"):
        st.session_state.task = "Evaluation"
    
    task = st.session_state.task

    if task == "Preprocessing":
        st.header("Data Preprocessing")
        st.subheader("Load audio files")
        
        # Select dataset
        st.write(os.getcwd())
        if os.path.isdir("Dataset"):
            st.write("true")
            subfolders = [f.name for f in os.scandir("Dataset") if f.is_dir()]
        else:
            st.write("false")
            subfolders = []
        st.selectbox("Dataset", subfolders)

    elif task == "Models":
        st.header("Models")
    
    elif task == "Evaluation":
        st.header("Evaluation")

if __name__ == "__main__":
    main()