import pandas as pd
import plotly.graph_objects as go

# Assuming you have loaded your DataFrame as df
df = pd.read_csv('data/list.csv', header=None, names=['Component', 'PR Number', 'Title', 'MergedAt'])

# Prepare the data
df['MergedAt'] = pd.to_datetime(df['MergedAt'])
df['MonthYear'] = df['MergedAt'].dt.to_period('M')

# Count the PRs
pr_counts = df.groupby(['MonthYear', 'Component']).size().unstack(fill_value=0)

# Create a stacked bar chart
fig = go.Figure()

for component in pr_counts.columns:
    fig.add_trace(go.Bar(
        x=pr_counts.index.astype(str),  # Convert to string to avoid issues with datetime on x-axis
        y=pr_counts[component],
        name=component
    ))

# Update layout for a stacked bar chart
fig.update_layout(
    barmode='stack',
    title='Monthly PR Activity by Component',
    xaxis_title='Month-Year',
    yaxis_title='Number of PRs Merged',
    legend_title='Component',
    hovermode="x"
)

fig.show()

# To save the figure as an HTML file which supports interactivity
fig.write_html("interactive_pr_timeline_stacked_bars.html")
