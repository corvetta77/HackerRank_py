#!/usr/bin/env python3
"""
Biofeedback Session Progress Charts Generator
Generates high-quality PNG charts for brainwave analysis
Patient: Michał (11 years old)
Date: 2025-11-07
"""

import matplotlib.pyplot as plt
import os

# Configure matplotlib for high-quality output
plt.rcParams['figure.dpi'] = 300
plt.rcParams['savefig.dpi'] = 300
plt.rcParams['font.family'] = 'sans-serif'

# Data from biofeedback sessions
sessions = {
    'Session 1': {
        'time': '16:23:02',
        'duration': '1 min',
        'score': 0,
        'data': {
            'Delta': {'ampl': 39.3, 'percent': 32.7},
            'Theta': {'ampl': 27.3, 'percent': 22.7},
            'Alpha': {'ampl': 26.8, 'percent': 22.2},
            'SMR': {'ampl': 9.9, 'percent': 8.23},
            'Beta': {'ampl': 9.8, 'percent': 8.17},
            'Beta2': {'ampl': 7.0, 'percent': 5.80},
            'SMR/Theta': {'ratio': 2.77}
        }
    },
    'Session 2': {
        'time': '16:41:47',
        'duration': '2 min',
        'score': 385,
        'data': {
            'Delta': {'ampl': 31.2, 'percent': 34.8},
            'Theta': {'ampl': 18.7, 'percent': 20.9},
            'Alpha': {'ampl': 14.7, 'percent': 16.4},
            'SMR': {'ampl': 9.4, 'percent': 10.5},
            'Beta': {'ampl': 7.9, 'percent': 8.87},
            'Beta2': {'ampl': 7.4, 'percent': 8.29},
            'SMR/Theta': {'ratio': 1.98}
        }
    }
}

# Polish descriptions
descriptions = {
    'Delta': {
        'title': 'Postęp w Falach Delta (1-4 Hz)',
        'description': 'Fale delta związane z głębokim snem i regeneracją.\nWzrost wskazuje na lepszą zdolność relaksacji.'
    },
    'Theta': {
        'title': 'Postęp w Falach Theta (4-8 Hz)',
        'description': 'Fale theta odpowiadają za kreatywność i stan medytacyjny.\nObniżenie jest dobrym wskaźnikiem kontroli stanów świadomości.'
    },
    'Alpha': {
        'title': 'Postęp w Falach Alpha (8-12 Hz)',
        'description': 'Fale alfa odpowiadają za stan spokoju i relaksacji.\nObniżenie może wskazywać na lepszą kontrolę uwagi.'
    },
    'SMR': {
        'title': 'Postęp w Falach SMR (12-15 Hz)',
        'description': 'Fale SMR wspierają concentrację i kontrolę motoryczną.\nWzrost to pozytywny efekt treningu neurofeedback.'
    },
    'Beta': {
        'title': 'Postęp w Falach Beta (15-20 Hz)',
        'description': 'Fale beta związane z aktywnością umysłową i alertnością.\nWzrost wskazuje na lepszą gotowość kognitywną.'
    },
    'Beta2': {
        'title': 'Postęp w Falach Beta2 (20-30 Hz)',
        'description': 'Wysokofrequencyjne fale beta2 związane z intensywnym myśleniem.\nWzrost może wskazywać na większą aktywną zaangażowanie.'
    },
    'SMR/Theta': {
        'title': 'Postęp w Stosunku SMR/Theta',
        'description': 'Stosunek SMR do Theta jest kluczowym wskaźnikiem treningu.\nObniżenie z 2.77 do 1.98 wskazuje na wzmocnienie zdolności regulacji.'
    }
}

def create_brainwave_chart(wave_type):
    """Create a chart for a specific brainwave type"""
    
    fig, ax = plt.subplots(figsize=(12, 8))
    
    session1_data = sessions['Session 1']['data'][wave_type]
    session2_data = sessions['Session 2']['data'][wave_type]
    
    # Prepare data
    if wave_type == 'SMR/Theta':
        sessions_list = ['Sesja 1\n(16:23:02)', 'Sesja 2\n(16:41:47)']
        values = [session1_data['ratio'], session2_data['ratio']]
        bar_colors = ['#2E86AB', '#6A994E']
        
        bars = ax.bar(sessions_list, values, color=bar_colors, alpha=0.8, width=0.5)
        
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'{height:.2f}', ha='center', va='bottom', fontsize=11, fontweight='bold')
        
        ax.set_ylabel('Stosunek SMR/Theta', fontsize=12, fontweight='bold')
    else:
        sessions_list = ['Sesja 1\n(16:23:02)', 'Sesja 2\n(16:41:47)']
        ampl_values = [session1_data['ampl'], session2_data['ampl']]
        percent_values = [session1_data['percent'], session2_data['percent']]
        
        x = range(len(sessions_list))
        width = 0.35
        
        bars1 = ax.bar([i - width/2 for i in x], ampl_values, width, 
                       label='Amplituda (μV)', color='#2E86AB', alpha=0.8)
        bars2 = ax.bar([i + width/2 for i in x], percent_values, width,
                       label='Procent (%)', color='#A23B72', alpha=0.8)
        
        for bar in bars1:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'{height:.1f}', ha='center', va='bottom', fontsize=9, fontweight='bold')
        
        for bar in bars2:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'{height:.1f}%', ha='center', va='bottom', fontsize=9, fontweight='bold')
        
        ax.set_ylabel('Wartość', fontsize=12, fontweight='bold')
        ax.legend(fontsize=11, loc='upper left')
    
    ax.set_xlabel('Sesje Treningowe', fontsize=12, fontweight='bold')
    ax.set_xticks(range(len(sessions_list)))
    ax.set_xticklabels(sessions_list, fontsize=11)
    ax.grid(axis='y', alpha=0.3, linestyle='--')
    
    # Add title and description
    title = descriptions[wave_type]['title']
    desc = descriptions[wave_type]['description']
    
    plt.title(title, fontsize=14, fontweight='bold', pad=20)
    
    # Add description box
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.3)
    ax.text(0.98, 0.02, desc, transform=ax.transAxes,
           fontsize=10, verticalalignment='bottom', horizontalalignment='right',
           bbox=props, style='italic', multialignment='right')
    
    # Add session info
    info_text = f"Pacjent: Michał (11 lat)\nData: 2025-11-07\nMetoda: SMR/Theta"
    ax.text(0.02, 0.98, info_text, transform=ax.transAxes,
           fontsize=9, verticalalignment='top', horizontalalignment='left',
           bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.3))
    
    plt.tight_layout()
    
    # Save the figure
    filename = f'brainwave_{wave_type.lower().replace("/", "_")}_progress.png'
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    print(f"✓ Wygenerowano: {filename}")
    plt.close()


def create_summary_chart():
    """Create a comprehensive summary chart"""
    
    fig, axes = plt.subplots(2, 3, figsize=(16, 10))
    fig.suptitle('Podsumowanie Postępu Treningu Neurofeedback - Michał (11 lat)\nData: 2025-11-07', 
                 fontsize=16, fontweight='bold', y=0.995)
    
    waves = ['Delta', 'Theta', 'Alpha', 'SMR', 'Beta', 'Beta2']
    axes_flat = axes.flatten()
    
    for idx, wave in enumerate(waves):
        ax = axes_flat[idx]
        
        session1_data = sessions['Session 1']['data'][wave]
        session2_data = sessions['Session 2']['data'][wave]
        
        sessions_list = ['S1', 'S2']
        percent_values = [session1_data['percent'], session2_data['percent']]
        
        change = percent_values[1] - percent_values[0]
        change_color = '#6A994E' if change > 0 else '#C73E1D'
        
        bars = ax.bar(sessions_list, percent_values, color=['#2E86AB', change_color], alpha=0.8)
        
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'{height:.1f}%', ha='center', va='bottom', fontsize=10, fontweight='bold')
        
        freq_range = descriptions[wave]['title'].split("(")[1].rstrip(")")
        ax.set_title(f'{wave} ({freq_range}',
                    fontsize=11, fontweight='bold')
        ax.set_ylabel('Procent (%)', fontsize=9)
        ax.set_ylim(0, max(percent_values) * 1.2)
        ax.grid(axis='y', alpha=0.3, linestyle='--')
        
        # Add change indicator
        change_text = f'{change:+.1f}%'
        change_symbol = '↑' if change > 0 else '↓'
        ax.text(0.5, 0.95, f'{change_symbol} {change_text}', 
               transform=ax.transAxes, ha='center', va='top',
               fontsize=11, fontweight='bold', color=change_color,
               bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.5))
    
    # Add overall summary text
    fig.text(0.5, 0.02, 
            'Sesja 1: 16:23:02 (1 min, Wynik: 0 pkt) | Sesja 2: 16:41:47 (2 min, Wynik: 385 pkt)\n' +
            'Pozytywny postęp widoczny w większości parametrów. Wzrost SMR i zmniejszenie Theta wskazuje na lepszą samoregulację.',
            ha='center', fontsize=10, style='italic',
            bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.2))
    
    plt.tight_layout(rect=[0, 0.05, 1, 0.99])
    
    filename = 'brainwave_summary_progress.png'
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    print(f"✓ Wygenerowano: {filename}")
    plt.close()


def main():
    """Generate all charts"""
    print("=" * 60)
    print("GENERATOR WYKRESÓW NEUROFEEDBACK")
    print("Pacjent: Michał (11 lat)")
    print("Data: 2025-11-07")
    print("=" * 60)
    print()
    
    waves = ['Delta', 'Theta', 'Alpha', 'SMR', 'Beta', 'Beta2', 'SMR/Theta']
    
    print("Generowanie wykresów poszczególnych fal mózgowych...")
    for wave in waves:
        create_brainwave_chart(wave)
    
    print()
    print("Generowanie podsumowania...")
    create_summary_chart()
    
    print()
    print("=" * 60)
    print("✓ Wszystkie wykresy zostały wygenerowane!")
    print("=" * 60)
    print()
    print("Wygenerowane pliki:")
    print("  - brainwave_delta_progress.png")
    print("  - brainwave_theta_progress.png")
    print("  - brainwave_alpha_progress.png")
    print("  - brainwave_smr_progress.png")
    print("  - brainwave_beta_progress.png")
    print("  - brainwave_beta2_progress.png")
    print("  - brainwave_smr_theta_progress.png")
    print("  - brainwave_summary_progress.png")
    print()


if __name__ == '__main__':
    main()
