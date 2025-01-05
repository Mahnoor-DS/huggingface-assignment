import gradio as gr

# A simple ML model: Addition function
def add_numbers(a, b):
    return a + b

# Gradio Interface
demo = gr.Interface(fn=add_numbers, inputs=["number", "number"], outputs="number")
demo.launch()
