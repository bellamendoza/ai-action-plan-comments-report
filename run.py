import panel as pn
import plotly.graph_objs as go
import numpy as np
import pandas as pd
from datetime import datetime

pn.extension()

# Sample data
np.random.seed(0)
line_data = pd.DataFrame({
    'x': np.arange(1, 101),
    'y': np.random.randn(100).cumsum()
})

# Plots
def create_line_plot():
    fig = go.Figure(data=[
        go.Scatter(x=line_data['x'], y=line_data['y'], mode='lines', name='Random Walk')
    ])
    fig.update_layout(title='Random Cumulative Sum', xaxis_title='X-axis', yaxis_title='Y-axis')
    return pn.pane.Plotly(fig, width=800)

def create_bar_chart():
    bar_data = pd.DataFrame({
        'categories': ['Category A', 'Category B', 'Category C', 'Category D', 'Category E'],
        'values': np.random.randint(10, 100, 5)
    })
    fig = go.Figure(data=[
        go.Bar(x=bar_data['categories'], y=bar_data['values'])
    ])
    fig.update_layout(title='Category Distribution', xaxis_title='Categories', yaxis_title='Values')
    return pn.pane.Plotly(fig, width=800)

# Text sections
def create_text(text):
    return pn.pane.Markdown(text, width=800)

def create_title_section():
    title_html = f"""
    <div style="text-align: center;">
        <h1>📊 Data Analysis Report</h1>
        <p><strong>Author:</strong> Your Name</p>
        <p><strong>Date:</strong> {datetime.now().strftime('%B %d, %Y')}</p>
    </div>
    """
    return pn.pane.HTML(title_html, width=800)

# Assemble the report
def create_report():
    center_content = pn.Column(
        create_title_section(),
        create_line_plot(),
        create_text("""
        ## Insights

        The first plot shows a random cumulative sum of data points. 
        This simulates a basic random walk process used in modeling and simulation.
        """),
        create_bar_chart(),
        create_text("""
        ## Further Analysis

        The second plot displays a simple bar chart of values by category.
        This is a useful tool for comparing quantities across discrete groups.
        """),
        width=800
    )
    
    # Add HSpacers to center it in the full-width Row
    return pn.Row(
        pn.layout.HSpacer(),
        center_content,
        pn.layout.HSpacer(),
        sizing_mode='stretch_width'
    )

# Show the centered report
create_report().show()
