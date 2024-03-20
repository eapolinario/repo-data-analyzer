import pandas as pd
import plotly.express as px

# Load the data
df = pd.read_csv('data/list.csv', header=None, names=['Component', 'PR Number', 'Title', 'MergedAt'])

# Convert 'MergedAt' to datetime and extract year-month for grouping
df['MergedAt'] = pd.to_datetime(df['MergedAt'])
df['YearMonth'] = df['MergedAt'].dt.to_period('M')

# Count the number of PRs per component per month
pr_counts = df.groupby(['YearMonth', 'Component']).size().reset_index(name='Counts')

# Create a pivot table for plotting, with YearMonth as index and components as columns
pivot_pr_counts = pr_counts.pivot(index='YearMonth', columns='Component', values='Counts').fillna(0)

# Reset index to convert YearMonth from PeriodIndex to DateTimeIndex for plotting
pivot_pr_counts.reset_index(inplace=True)

# Convert the pivot table back to a "long-form" dataframe
long_pr_counts = pd.melt(pivot_pr_counts, id_vars=['YearMonth'], var_name='Component', value_name='Counts')

# Convert YearMonth back to datetime for plotting
long_pr_counts['YearMonth'] = long_pr_counts['YearMonth'].dt.to_timestamp()

# Plot using Plotly Express
fig = px.line(long_pr_counts, x='YearMonth', y='Counts', color='Component', markers=True,
              labels={'Counts': 'Number of PRs Merged', 'YearMonth': 'Month'},
              title='Monthly PR Activity by Component')

fig.update_traces(mode='lines+markers', hoverinfo='text+name', line=dict(shape='linear'))
fig.update_layout(hovermode='closest')

# Show the figure
fig.show()

# To save the figure as an HTML file which supports interactivity
fig.write_html("interactive_pr_timeline.html")
