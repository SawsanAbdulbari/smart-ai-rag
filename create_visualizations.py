"""
Strategy Comparison Visualization
This script creates visual comparisons of different prompting strategies.
"""

import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px

def create_strategy_comparison_chart():
    """Create a comprehensive comparison of prompting strategies."""
    
    # Data for comparison
    strategies = ['Standard', 'Few-Shot', 'Chain-of-Thought', 'Combined']
    
    metrics = {
        'Response Quality': [70, 82, 85, 91],
        'Consistency': [65, 88, 80, 92],
        'Reasoning Depth': [60, 70, 95, 93],
        'User Satisfaction': [70, 80, 85, 95],
        'Confidence': [72, 85, 88, 93]
    }
    
    # Create subplots
    fig = make_subplots(
        rows=2, cols=2,
        subplot_titles=('Overall Performance', 'Confidence Levels', 
                       'Strategy Effectiveness', 'Feature Comparison'),
        specs=[[{'type': 'bar'}, {'type': 'scatter'}],
               [{'type': 'scatter', 'rowspan': 1, 'colspan': 2}, None]]
    )
    
    # 1. Bar chart - Overall Performance
    for metric, values in metrics.items():
        fig.add_trace(
            go.Bar(name=metric, x=strategies, y=values),
            row=1, col=1
        )
    
    # 2. Line chart - Confidence Progression
    fig.add_trace(
        go.Scatter(
            x=strategies, 
            y=metrics['Confidence'],
            mode='lines+markers',
            name='Confidence Score',
            line=dict(color='#FF6B6B', width=3),
            marker=dict(size=10)
        ),
        row=1, col=2
    )
    
    # 3. Radar chart - Strategy Effectiveness
    categories = list(metrics.keys())
    
    fig.add_trace(
        go.Scatterpolar(
            r=metrics['Response Quality'],
            theta=categories,
            fill='toself',
            name='Standard',
            line_color='#4ECDC4'
        ),
        row=2, col=1
    )
    
    fig.add_trace(
        go.Scatterpolar(
            r=[metrics[cat][3] for cat in categories],  # Combined strategy
            theta=categories,
            fill='toself',
            name='Combined',
            line_color='#FF6B6B'
        ),
        row=2, col=1
    )
    
    # Update layout
    fig.update_layout(
        title_text="Prompting Strategy Comparison Analysis",
        title_font_size=24,
        showlegend=True,
        height=800,
        width=1200
    )
    
    # Update axes
    fig.update_xaxes(title_text="Strategy", row=1, col=1)
    fig.update_yaxes(title_text="Score (%)", row=1, col=1)
    fig.update_xaxes(title_text="Strategy", row=1, col=2)
    fig.update_yaxes(title_text="Confidence (%)", row=1, col=2)
    
    # Update polar
    fig.update_polars(radialaxis_range=[0, 100], row=2, col=1)
    
    return fig

def create_response_time_comparison():
    """Create response time comparison across strategies."""
    
    strategies = ['Standard', 'Few-Shot', 'Chain-of-Thought', 'Self-Consistency', 'Combined']
    response_times = [1.2, 1.5, 2.1, 3.8, 4.5]  # seconds
    quality_scores = [70, 82, 85, 90, 93]
    
    fig = go.Figure()
    
    # Create scatter plot with bubble size representing quality
    fig.add_trace(go.Scatter(
        x=response_times,
        y=quality_scores,
        mode='markers+text',
        marker=dict(
            size=[30, 40, 45, 50, 60],
            color=quality_scores,
            colorscale='Viridis',
            showscale=True,
            colorbar=dict(title="Quality Score")
        ),
        text=strategies,
        textposition="top center"
    ))
    
    fig.update_layout(
        title="Response Time vs Quality Trade-off",
        xaxis_title="Response Time (seconds)",
        yaxis_title="Quality Score (%)",
        showlegend=False,
        height=500,
        width=800
    )
    
    # Add optimal zone
    fig.add_shape(
        type="rect",
        x0=1.5, y0=80,
        x1=3.0, y1=90,
        line=dict(color="green", width=2, dash="dash"),
        fillcolor="lightgreen",
        opacity=0.2
    )
    
    fig.add_annotation(
        x=2.25, y=85,
        text="Optimal Zone",
        showarrow=False,
        font=dict(color="green", size=12)
    )
    
    return fig

def create_role_strategy_heatmap():
    """Create heatmap showing effectiveness of each strategy per role."""
    
    import numpy as np
    
    roles = ['Teacher', 'Expert Reviewer', 'Legal Advisor', 'Technical Writer', 'Friendly Assistant']
    strategies = ['Standard', 'Few-Shot', 'Chain-of-Thought', 'Combined']
    
    # Effectiveness scores (0-100)
    effectiveness = np.array([
        [75, 85, 80, 92],  # Teacher
        [70, 80, 90, 95],  # Expert Reviewer
        [65, 88, 85, 93],  # Legal Advisor
        [72, 82, 88, 94],  # Technical Writer
        [80, 85, 75, 90]   # Friendly Assistant
    ])
    
    fig = go.Figure(data=go.Heatmap(
        z=effectiveness,
        x=strategies,
        y=roles,
        colorscale='RdYlBu',
        text=effectiveness,
        texttemplate="%{text}%",
        textfont={"size": 14}
    ))
    
    fig.update_layout(
        title="Role-Strategy Effectiveness Matrix",
        xaxis_title="Strategy",
        yaxis_title="Role",
        height=500,
        width=700
    )
    
    return fig

if __name__ == "__main__":
    # Generate and save visualizations
    print("Creating strategy comparison visualizations...")
    
    # Create comparison chart
    fig1 = create_strategy_comparison_chart()
    fig1.write_html("strategy_comparison.html")
    fig1.write_image("strategy_comparison.png", width=1200, height=800)
    
    # Create time-quality trade-off
    fig2 = create_response_time_comparison()
    fig2.write_html("time_quality_tradeoff.html")
    fig2.write_image("time_quality_tradeoff.png")
    
    # Create role-strategy heatmap
    fig3 = create_role_strategy_heatmap()
    fig3.write_html("role_strategy_heatmap.html")
    fig3.write_image("role_strategy_heatmap.png")
    
    print("Visualizations saved!")
    print("- strategy_comparison.html/png")
    print("- time_quality_tradeoff.html/png")
    print("- role_strategy_heatmap.html/png")