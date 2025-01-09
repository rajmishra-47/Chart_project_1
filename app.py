import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd 


options=[]

uploaded_file = st.file_uploader("Choose a   .xlsx file to start analysis",type=["xlsx", "xls"])

if uploaded_file:
    file=pd.read_excel(uploaded_file)
    Names=file.columns

    optionsX = st.multiselect(
    "Selcet values for X ",Names
    )
    
    optionsY = st.multiselect(
    "Selcet values for Y ",Names
    )

  
    if st.button("Plot"):
        if optionsX and optionsY:
            fig, ax = plt.subplots()
            for x_col in optionsX:
                for y_col in optionsY:
                    ax.bar(file[x_col], file[y_col], label=f"{x_col} vs {y_col}")

       
            ax.set_xlabel("X-axis")
            ax.set_ylabel("Y-axis")
            ax.legend()
            ax.grid(True)

            st.success("Here it is")
            st.pyplot(fig)
        else:
            st.warning("Please select both X and Y values to plot.")
    