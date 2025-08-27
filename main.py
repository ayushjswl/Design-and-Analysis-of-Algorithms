import streamlit as st
import numpy as np
import pandas as pd
import io
from algorithm.algos import bubble_sort, insertion_sort, merge_sort, selection_sort, sample_size
from algorithm.algo_doc import document, description
from PDF import generate_pdf
import matplotlib.pyplot as p


st.set_page_config(page_title="AlgoLab")

# Google Search Console verification
st.markdown("""
    <meta name="google-site-verification" content="YOUR_VERIFICATION_CODE_HERE" />
""", unsafe_allow_html=True)

st.markdown("""
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-Q9W5J332GX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-Q9W5J332GX');
</script>
            """, unsafe_allow_html=True)

st.title("Algorithm Lab")
sort_functions = {
    "Bubble Sort": bubble_sort,
    "Insertion Sort": insertion_sort,
    "Merge Sort": merge_sort,
    "Selection Sort": selection_sort,
    "Comparison": "Comparison",
    "Other": "Others",
}


algo =  st.selectbox("Select Algorithms", list(sort_functions.keys()))

if algo=='Other':
    input = st.text_area("Source Code", height=300)
    if input :
        st.button("Run")

elif algo=="Comparison":
    
    all_algos = ["Bubble Sort", "Insertion Sort", "Merge Sort","Selection Sort"]
    algorithms = st.multiselect("Algorithms", all_algos, default=all_algos[0])
    st.write(f"Comparison between {algorithms}")

    if 'list' not in st.session_state:
        st.session_state.list = []

    tab3, tab4 = st.tabs(["Single Array", "Multiple Arrays"])
    with tab3:
        size = st.number_input("Enter Array Size", min_value=1, max_value=30, value=10,)
        if st.button("Generate", key="_comparrison"):
            st.session_state.list = sample_size(size)
            
        st.code(st.session_state.list, language="python", line_numbers=True, wrap_lines=True, height="content", width="stretch")
        if st.button("Run Code", key="run_code_comparrison"):
            temp = st.session_state.list.copy()
            z=[]
            for function_name in algorithms:
                z.append(sort_functions[function_name](temp[0])[0])
            
            data = {
                "Algorithms": algorithms,
                "Time": z,
            }

            df = pd.DataFrame(data).set_index('Algorithms')
            st.bar_chart(df, x_label="Seconds", horizontal=True,)
            #st.write("Sorted Array")
            #st.code(z[2][1], language="python", line_numbers=True, wrap_lines=True, height="content", width="stretch")


    with tab4:

        samples = st.slider("Max Array size", 1, 1000, 100)
        step = st.number_input("Enter intervals", min_value=1, max_value=samples, value=10,)

        if st.button("Run"):

            #code logic 
            x, y1, y2, y3, y4 = [], [], [], [], []

            list = sample_size(*range(step,samples+1,step))

            for i in list:
                x.append(len(i))
                y1.append(bubble_sort(i[:])[0])
                y2.append(insertion_sort(i[:])[0])
                y3.append(merge_sort(i[:])[0])
                y4.append(selection_sort(i[:])[0])
            
            fig, plt = p.subplots()
            plt.plot(x, y1, marker='o', linestyle='-', label = "Bubble Sort")
            plt.plot(x, y2, marker='o', linestyle='-', label = "Insertion Sort")
            plt.plot(x, y3, marker='o', linestyle='-', label = "Merge Sort")
            plt.plot(x, y4, marker='o', linestyle='-', label = "Selection Sort")
            plt.autoscale(tight=True)
            plt.set_xlabel('Array Size')
            plt.set_ylabel('Time Taken dt')
            plt.set_title('Simple Line Graph')
            plt.legend()
            plt.grid(True)

            data = {
            "Array Size": x,
            "Bubble Sort": y1,
            "Insertion Sort": y2,
            "Merge Sort": y3,
            "Selection Sort": y4,
            }

            df = pd.DataFrame(data, columns=["Array Size"] + algorithms)

            tab1, tab2, tab3 = st.tabs(["Chart", "Dataframe", "Matplot Chart"])
            with tab1:
                st.line_chart(df.set_index("Array Size"), height=250)
            with tab2:
                st.dataframe(df, height=250, use_container_width=True)
            with tab3:
                st.pyplot(fig, clear_figure=True, use_container_width=True)

else:
    detail_data ={
        "Attributes" : description["Attributes"],
        "Description" : description[algo]
    }
    detail_df = pd.DataFrame(detail_data)
    tab1, tab2 = st.tabs(["Source Code", "Details"])
    with tab1:
        body = document[algo]
        st.code(body, language="python", line_numbers=True, wrap_lines=True, height="content", width="stretch")
    with tab2:
        st.dataframe(detail_df, height=250, use_container_width=True)
    

    #flag1, flag2 = False, False
    if 'list' not in st.session_state:
        st.session_state.list = []
    tab3, tab4 = st.tabs(["Single Array", "Multiple Arrays"])
    with tab3:
        size = st.number_input("Enter Array Size", min_value=1, max_value=30, value=10,)
        if st.button("Generate"):
            st.session_state.list = sample_size(size)
        st.code(st.session_state.list, language="python", line_numbers=True, wrap_lines=True, height="content", width="stretch")
            
        if st.button("Run Code", key="run_button_flag1"):
            temp = st.session_state.list.copy()
            z = sort_functions[algo](temp[0])
            df = pd.DataFrame(
                {"Time Taken":[z[0]], 
                }
            )
            
            st.bar_chart(df, y_label=algo, x_label="Seconds", horizontal=True,)
            st.write("Sorted Array")
            st.code(z[1], language="python", line_numbers=True, wrap_lines=True, height="content", width="stretch")


    with tab4:
        samples = st.slider("Max Array size", 1, 1000, 100)
        step = st.number_input("Enter intervals", min_value=1, max_value=samples, value=10,)
        if st.button("Run", key="run_button_flag2"):
            list = sample_size(*range(step,samples+1,step))

            #code logic 
            x, y= [], []
            for i in list:
                x.append(len(i))
                y.append(sort_functions[algo](i[:])[0])
            
            fig, plt = p.subplots()
            plt.plot(x, y, marker='o', linestyle='-', label = {algo})
            plt.autoscale(tight=True)
            plt.set_xlabel('Array Size')
            plt.set_ylabel('Time Taken dt')
            plt.set_title(f'{algo} Line Graph')
            plt.legend()
            plt.grid(True)

            data = {
            "Array Size": x,
            "Time (ms)": y,
            }

            df = pd.DataFrame(data)

            tab1, tab2, tab3 = st.tabs(["Chart", "Dataframe", "Matplot Chart"])
            tab1.line_chart(df.set_index("Array Size"), height=250)
            tab2.dataframe(df, height=250, use_container_width=True)
            tab3.pyplot(fig, clear_figure=None, use_container_width=True)

            #Saving matplotlib graph to buffer
            img_buffer = io.BytesIO()
            fig.savefig(img_buffer, format='png', bbox_inches='tight')
            img_buffer.seek(0)

            get_pdf = generate_pdf.create_pdf_report(algo, detail_df, df, body, img_buffer)
            
            st.download_button(
            label="Report",
            data=bytes(get_pdf),
            file_name=f"{algo} report.pdf",
            type="primary",
            icon=":material/download:",
            mime="application/pdf",
            )