import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, ConnectionPatch
import numpy as np

def create_smart_agriculture_diagram():
    """Create a visual data flow diagram for the smart agriculture system"""
    
    fig, ax = plt.subplots(1, 1, figsize=(14, 10))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis('off')
    
    # Define colors
    sensor_color = '#4CAF50'  # Green
    gateway_color = '#2196F3'  # Blue
    cloud_color = '#FF9800'   # Orange
    control_color = '#9C27B0'  # Purple
    
    # IoT Sensors Box
    sensors_box = FancyBboxPatch((0.5, 6), 2, 1.5, 
                                boxstyle="round,pad=0.1", 
                                facecolor=sensor_color, 
                                edgecolor='black', 
                                alpha=0.7)
    ax.add_patch(sensors_box)
    ax.text(1.5, 6.75, 'IoT Sensors', ha='center', va='center', fontsize=12, fontweight='bold')
    ax.text(1.5, 6.4, '• Soil Moisture\n• Temperature\n• pH Levels\n• Nutrients', 
            ha='center', va='center', fontsize=9)
    
    # Edge Gateway Box
    gateway_box = FancyBboxPatch((4, 6), 2, 1.5, 
                                boxstyle="round,pad=0.1", 
                                facecolor=gateway_color, 
                                edgecolor='black', 
                                alpha=0.7)
    ax.add_patch(gateway_box)
    ax.text(5, 6.75, 'Edge Gateway', ha='center', va='center', fontsize=12, fontweight='bold')
    ax.text(5, 6.4, '• Data Filtering\n• Local Storage\n• Preprocessing\n• Edge AI', 
            ha='center', va='center', fontsize=9)
    
    # Cloud Platform Box
    cloud_box = FancyBboxPatch((7.5, 6), 2, 1.5, 
                              boxstyle="round,pad=0.1", 
                              facecolor=cloud_color, 
                              edgecolor='black', 
                              alpha=0.7)
    ax.add_patch(cloud_box)
    ax.text(8.5, 6.75, 'Cloud Platform', ha='center', va='center', fontsize=12, fontweight='bold')
    ax.text(8.5, 6.4, '• AI Processing\n• Yield Models\n• Analytics\n• Dashboards', 
            ha='center', va='center', fontsize=9)
    
    # Decision Engine Box
    decision_box = FancyBboxPatch((7.5, 3.5), 2, 1.5, 
                                 boxstyle="round,pad=0.1", 
                                 facecolor=control_color, 
                                 edgecolor='black', 
                                 alpha=0.7)
    ax.add_patch(decision_box)
    ax.text(8.5, 4.25, 'Decision Engine', ha='center', va='center', fontsize=12, fontweight='bold')
    ax.text(8.5, 3.9, '• ML Predictions\n• Optimization\n• Alerts\n• Recommendations', 
            ha='center', va='center', fontsize=9)
    
    # Control Logic Box
    control_box = FancyBboxPatch((4, 3.5), 2, 1.5, 
                                boxstyle="round,pad=0.1", 
                                facecolor=gateway_color, 
                                edgecolor='black', 
                                alpha=0.7)
    ax.add_patch(control_box)
    ax.text(5, 4.25, 'Control Logic', ha='center', va='center', fontsize=12, fontweight='bold')
    ax.text(5, 3.9, '• Rule Engine\n• Safety Checks\n• Manual Override\n• Scheduling', 
            ha='center', va='center', fontsize=9)
    
    # Actuator Systems Box
    actuator_box = FancyBboxPatch((0.5, 3.5), 2, 1.5, 
                                 boxstyle="round,pad=0.1", 
                                 facecolor=sensor_color, 
                                 edgecolor='black', 
                                 alpha=0.7)
    ax.add_patch(actuator_box)
    ax.text(1.5, 4.25, 'Actuator Systems', ha='center', va='center', fontsize=12, fontweight='bold')
    ax.text(1.5, 3.9, '• Irrigation\n• Fertilization\n• Pest Control\n• Climate Control', 
            ha='center', va='center', fontsize=9)
    
    # Data Flow Arrows
    # Sensors to Gateway
    arrow1 = ConnectionPatch((2.5, 6.75), (4, 6.75), "data", "data",
                           arrowstyle="->", shrinkA=5, shrinkB=5, 
                           mutation_scale=20, fc="black", lw=2)
    ax.add_patch(arrow1)
    
    # Gateway to Cloud
    arrow2 = ConnectionPatch((6, 6.75), (7.5, 6.75), "data", "data",
                           arrowstyle="->", shrinkA=5, shrinkB=5, 
                           mutation_scale=20, fc="black", lw=2)
    ax.add_patch(arrow2)
    
    # Cloud to Decision Engine
    arrow3 = ConnectionPatch((8.5, 6), (8.5, 5), "data", "data",
                           arrowstyle="->", shrinkA=5, shrinkB=5, 
                           mutation_scale=20, fc="black", lw=2)
    ax.add_patch(arrow3)
    
    # Decision Engine to Control Logic
    arrow4 = ConnectionPatch((7.5, 4.25), (6, 4.25), "data", "data",
                           arrowstyle="->", shrinkA=5, shrinkB=5, 
                           mutation_scale=20, fc="black", lw=2)
    ax.add_patch(arrow4)
    
    # Control Logic to Actuators
    arrow5 = ConnectionPatch((4, 4.25), (2.5, 4.25), "data", "data",
                           arrowstyle="->", shrinkA=5, shrinkB=5, 
                           mutation_scale=20, fc="black", lw=2)
    ax.add_patch(arrow5)
    
    # Feedback loop from Actuators to Sensors
    arrow6 = ConnectionPatch((1.5, 5), (1.5, 6), "data", "data",
                           arrowstyle="->", shrinkA=5, shrinkB=5, 
                           mutation_scale=20, fc="gray", lw=1.5, linestyle='--')
    ax.add_patch(arrow6)
    
    # Add data flow labels
    ax.text(3.25, 7, 'Sensor Data\n(15min intervals)', ha='center', va='bottom', fontsize=8, 
            bbox=dict(boxstyle="round,pad=0.3", facecolor='white', alpha=0.8))
    ax.text(6.75, 7, 'Processed Data\n(Real-time)', ha='center', va='bottom', fontsize=8,
            bbox=dict(boxstyle="round,pad=0.3", facecolor='white', alpha=0.8))
    ax.text(9, 5.5, 'AI Insights\n(Predictions)', ha='left', va='center', fontsize=8,
            bbox=dict(boxstyle="round,pad=0.3", facecolor='white', alpha=0.8))
    ax.text(6.75, 4.5, 'Control\nCommands', ha='center', va='bottom', fontsize=8,
            bbox=dict(boxstyle="round,pad=0.3", facecolor='white', alpha=0.8))
    ax.text(3.25, 4.5, 'Automated\nActions', ha='center', va='bottom', fontsize=8,
            bbox=dict(boxstyle="round,pad=0.3", facecolor='white', alpha=0.8))
    ax.text(0.8, 5.5, 'Environmental\nFeedback', ha='center', va='center', fontsize=8,
            bbox=dict(boxstyle="round,pad=0.3", facecolor='lightgray', alpha=0.8))
    
    # Add title
    ax.text(5, 7.8, 'Smart Agriculture System - Data Flow Architecture', 
            ha='center', va='center', fontsize=16, fontweight='bold')
    
    # Add legend
    legend_elements = [
        patches.Patch(color=sensor_color, alpha=0.7, label='Field Devices'),
        patches.Patch(color=gateway_color, alpha=0.7, label='Processing Units'),
        patches.Patch(color=cloud_color, alpha=0.7, label='Cloud Services'),
        patches.Patch(color=control_color, alpha=0.7, label='AI/ML Components')
    ]
    ax.legend(handles=legend_elements, loc='lower center', ncol=4, 
              bbox_to_anchor=(0.5, 0.02), fontsize=10)
    
    # Add performance metrics box
    metrics_box = FancyBboxPatch((0.5, 1), 9, 1.5, 
                                boxstyle="round,pad=0.1", 
                                facecolor='lightblue', 
                                edgecolor='black', 
                                alpha=0.3)
    ax.add_patch(metrics_box)
    ax.text(5, 2, 'System Performance Metrics', ha='center', va='center', 
            fontsize=12, fontweight='bold')
    ax.text(2.5, 1.5, '• Data Latency: <5 seconds\n• Prediction Accuracy: >90%\n• System Uptime: 99.5%', 
            ha='left', va='center', fontsize=10)
    ax.text(7.5, 1.5, '• Sensor Coverage: 50+ per hectare\n• Processing Capacity: 1M data points/day\n• Response Time: <30 seconds', 
            ha='left', va='center', fontsize=10)
    
    plt.tight_layout()
    plt.savefig('smart_agriculture_dataflow.png', dpi=300, bbox_inches='tight')
    plt.show()

if __name__ == "__main__":
    create_smart_agriculture_diagram()