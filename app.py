import streamlit as st
from datetime import datetime
import os
import warnings
import streamlit.components.v1 as components
import time
import random

from src.crews.agent_prompt.src.agent_prompt.crew import AgentPromptEnhancementCrew
from src.crews.long_prompt.src.long_prompt.crew import LongPromptCrew
from src.crews.short_prompt.src.short_prompt.crew import ShortPromptCrew

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# Function to run crew operations (unchanged)
def run_crew(crew_type, inputs):
    if crew_type == "agent":
        AgentPromptEnhancementCrew().crew().kickoff(inputs=inputs)
        return "enhanced_prompt.md"
    elif crew_type == "short":
        ShortPromptCrew().crew().kickoff(inputs=inputs)
        return "short_prompt.md"
    elif crew_type == "long":
        LongPromptCrew().crew().kickoff(inputs=inputs)
        return "long_prompt.md"
    else:
        raise ValueError("Invalid crew type.")

# Define theme colors
PRIMARY_COLOR = "#6200EA"  # Deep purple
SECONDARY_COLOR = "#03DAC6"  # Teal
BG_COLOR = "#121212"  # Very dark gray
CARD_BG = "#1E1E1E"  # Dark gray
TEXT_COLOR = "#FFFFFF"  # White
ACCENT_COLOR = "#FF9100"  # Amber

# Custom CSS with futuristic tech theme
def apply_tech_theme():
    st.markdown(f"""
    <style>
        /* Main app styling */
        .stApp {{
            background: {BG_COLOR};
            background-image: 
                radial-gradient(circle at 10% 20%, rgba(98, 0, 234, 0.03) 0%, transparent 20%),
                radial-gradient(circle at 90% 80%, rgba(3, 218, 198, 0.03) 0%, transparent 20%),
                linear-gradient(135deg, {BG_COLOR} 0%, #0a0a14 100%);
            color: {TEXT_COLOR};
        }}
        
        /* Sidebar styling */
        .css-1d391kg {{
            background-color: rgba(30, 30, 30, 0.9);
            border-right: 1px solid rgba(255, 255, 255, 0.1);
        }}
        
        /* Header styling */
        .tech-header {{
            background: linear-gradient(90deg, {PRIMARY_COLOR}99 0%, {PRIMARY_COLOR}22 100%);
            border-left: 4px solid {SECONDARY_COLOR};
            padding: 2rem;
            border-radius: 0.5rem;
            margin-bottom: 2rem;
            position: relative;
            overflow: hidden;
        }}
        
        .tech-header::before {{
            content: "";
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 2px;
            background: linear-gradient(90deg, transparent, {SECONDARY_COLOR}, transparent);
            animation: scan-line 3s linear infinite;
        }}
        
        @keyframes scan-line {{
            0% {{
                transform: translateX(-100%);
            }}
            100% {{
                transform: translateX(100%);
            }}
        }}
        
        .tech-header h1 {{
            font-family: 'Courier New', monospace;
            font-weight: 700;
            color: white;
            margin-bottom: 0.5rem;
            font-size: 2.5rem;
            letter-spacing: -1px;
        }}
        
        .tech-header p {{
            color: rgba(255, 255, 255, 0.8);
            font-size: 1rem;
            max-width: 600px;
        }}
        
        /* Card styling with tech vibe */
        .tech-card {{
            background: {CARD_BG};
            border-radius: 0.5rem;
            padding: 1.5rem;
            margin-bottom: 1.5rem;
            border: 1px solid rgba(255, 255, 255, 0.1);
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.25);
            position: relative;
            overflow: hidden;
        }}
        
        .tech-card::after {{
            content: "";
            position: absolute;
            bottom: 0;
            left: 0;
            right: 0;
            height: 2px;
            background: linear-gradient(90deg, transparent, {PRIMARY_COLOR}, {SECONDARY_COLOR}, transparent);
        }}
        
        /* Glowing effect for active elements */
        .glow-effect {{
            box-shadow: 0 0 15px {PRIMARY_COLOR}66;
            transition: box-shadow 0.3s ease;
        }}
        
        /* Form styling */
        .form-header {{
            color: {SECONDARY_COLOR};
            font-weight: 600;
            margin-bottom: 1rem;
            border-bottom: 1px solid rgba(255, 255, 255, 0.1);
            padding-bottom: 0.5rem;
            font-family: 'Courier New', monospace;
            letter-spacing: 1px;
        }}
        
        /* Input styling */
        .stTextInput>div>div>input {{
            background-color: rgba(30, 30, 30, 0.9);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 4px;
            color: white;
        }}
        
        .stTextArea>div>div>textarea {{
            background-color: rgba(30, 30, 30, 0.9);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 4px;
            color: white;
        }}
        
        /* Button styling */
        .stButton>button {{
            background: linear-gradient(90deg, {PRIMARY_COLOR} 0%, {SECONDARY_COLOR} 100%);
            color: white;
            border: none;
            padding: 0.6rem 1.2rem;
            font-weight: 600;
            border-radius: 4px;
            font-family: 'Courier New', monospace;
            letter-spacing: 1px;
            text-transform: uppercase;
            transition: all 0.3s;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
        }}
        
        .stButton>button:hover {{
            transform: translateY(-2px);
            box-shadow: 0 6px 15px rgba(0, 0, 0, 0.4);
        }}
        
        /* Crew Type Badge */
        .crew-badge {{
            display: inline-block;
            padding: 0.5rem 1rem;
            border-radius: 2rem;
            margin-right: 0.5rem;
            font-weight: 600;
            font-size: 0.85rem;
            position: relative;
            overflow: hidden;
            background: rgba(30, 30, 30, 0.9);
            border: 1px solid;
            letter-spacing: 1px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.3);
        }}
        
        .crew-agent {{
            border-color: #FF9100;
            color: #FF9100;
        }}
        
        .crew-short {{
            border-color: #00B0FF;
            color: #00B0FF;
        }}
        
        .crew-long {{
            border-color: #00E676;
            color: #00E676;
        }}
        
        /* Terminal effect for code output */
        .terminal-output {{
            background-color: #0d0d0d;
            color: #00ff00;
            font-family: 'Courier New', monospace;
            padding: 1rem;
            border-radius: 4px;
            border: 1px solid #333333;
            white-space: pre-wrap;
            position: relative;
            overflow: hidden;
        }}
        
        .terminal-output::before {{
            content: "> Prompt Engineering Studio Output";
            display: block;
            color: #cccccc;
            margin-bottom: 10px;
            border-bottom: 1px solid #333333;
            padding-bottom: 5px;
        }}
        
        /* Success message styling */
        .success-message {{
            background: linear-gradient(90deg, rgba(0, 200, 83, 0.1) 0%, rgba(0, 200, 83, 0.02) 100%);
            border-left: 4px solid #00C853;
            color: #00C853;
            padding: 1rem;
            border-radius: 0.25rem;
            margin: 1rem 0;
        }}
        
        /* Error message styling */
        .error-message {{
            background: linear-gradient(90deg, rgba(255, 23, 68, 0.1) 0%, rgba(255, 23, 68, 0.02) 100%);
            border-left: 4px solid #FF1744;
            color: #FF1744;
            padding: 1rem;
            border-radius: 0.25rem;
            margin: 1rem 0;
        }}
        
        /* Footer styling */
        .tech-footer {{
            text-align: center;
            margin-top: 2rem;
            padding-top: 1rem;
            border-top: 1px solid rgba(255, 255, 255, 0.1);
            color: rgba(255, 255, 255, 0.6);
            font-size: 0.85rem;
            font-family: 'Courier New', monospace;
        }}
        
        /* Typing effect */
        .typing-effect {{
            overflow: hidden;
            border-right: 2px solid {SECONDARY_COLOR};
            white-space: nowrap;
            margin: 0 auto;
            animation: typing 3.5s steps(40, end), blink-caret 0.75s step-end infinite;
        }}
        
        @keyframes typing {{
            from {{ width: 0 }}
            to {{ width: 100% }}
        }}
        
        @keyframes blink-caret {{
            from, to {{ border-color: transparent }}
            50% {{ border-color: {SECONDARY_COLOR} }}
        }}
        
        /* Loading animation */
        .loading-container {{
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
            padding: 2rem;
        }}
        
        .loading-brain {{
            font-size: 3rem;
            margin-bottom: 1rem;
            animation: pulse 1.5s infinite;
        }}
        
        @keyframes pulse {{
            0% {{ opacity: 1; transform: scale(1); }}
            50% {{ opacity: 0.6; transform: scale(0.95); }}
            100% {{ opacity: 1; transform: scale(1); }}
        }}
        
        .loading-text {{
            font-family: 'Courier New', monospace;
            color: {SECONDARY_COLOR};
            margin-top: 1rem;
        }}
        
        .loading-bar {{
            width: 100%;
            height: 4px;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 2px;
            margin: 1rem 0;
            position: relative;
            overflow: hidden;
        }}
        
        .loading-bar::after {{
            content: "";
            position: absolute;
            top: 0;
            left: 0;
            height: 100%;
            width: 30%;
            background: linear-gradient(90deg, {PRIMARY_COLOR}, {SECONDARY_COLOR});
            animation: loading-progress 2s infinite;
            border-radius: 2px;
        }}
        
        @keyframes loading-progress {{
            0% {{ left: -30%; }}
            100% {{ left: 100%; }}
        }}
        
        /* Tab styling */
        .stTabs [data-baseweb="tab-list"] {{
            gap: 10px;
            background-color: rgba(30, 30, 30, 0.9);
            border-radius: 4px;
            padding: 0.5rem;
        }}
        
        .stTabs [data-baseweb="tab"] {{
            padding: 0.5rem 1rem;
            color: white;
            border-radius: 4px;
        }}
        
        .stTabs [aria-selected="true"] {{
            background: linear-gradient(90deg, {PRIMARY_COLOR}80 0%, {PRIMARY_COLOR}40 100%);
            border-left: 2px solid {SECONDARY_COLOR};
        }}
        
        /* Selectbox styling */
        div[data-baseweb="select"] > div {{
            background-color: rgba(30, 30, 30, 0.9);
            border: 1px solid rgba(255, 255, 255, 0.1);
        }}
        
        div[data-baseweb="popover"] div {{
            background-color: rgba(30, 30, 30, 0.95);
            border: 1px solid rgba(255, 255, 255, 0.1);
        }}
        
        div[data-baseweb="select"] {{
            color: white;
        }}
        
        /* Stats boxes */
        .stats-container {{
            display: flex;
            gap: 10px;
            margin-bottom: 1rem;
        }}
        
        .stats-box {{
            background: rgba(30, 30, 30, 0.9);
            border-radius: 4px;
            padding: 0.8rem;
            flex: 1;
            border: 1px solid rgba(255, 255, 255, 0.1);
            text-align: center;
            position: relative;
            overflow: hidden;
        }}
        
        .stats-box::after {{
            content: "";
            position: absolute;
            bottom: 0;
            left: 0;
            right: 0;
            height: 2px;
        }}
        
        .stats-box.agent::after {{
            background: #FF9100;
        }}
        
        .stats-box.short::after {{
            background: #00B0FF;
        }}
        
        .stats-box.long::after {{
            background: #00E676;
        }}
        
        .stats-number {{
            font-size: 1.8rem;
            font-weight: bold;
            margin-bottom: 0.2rem;
        }}
        
        .stats-label {{
            font-size: 0.75rem;
            opacity: 0.8;
            text-transform: uppercase;
            letter-spacing: 1px;
        }}
        
        /* Processing step indicators */
        .processing-steps {{
            margin: 1.5rem 0;
        }}
        
        .step {{
            display: flex;
            align-items: center;
            margin-bottom: 0.5rem;
        }}
        
        .step-number {{
            background: rgba(30, 30, 30, 0.9);
            border: 1px solid rgba(255, 255, 255, 0.1);
            width: 25px;
            height: 25px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-right: 10px;
            font-size: 0.8rem;
        }}
        
        .step-text {{
            font-size: 0.9rem;
        }}
        
        .step.completed .step-number {{
            background: {SECONDARY_COLOR};
            color: #000;
            border: none;
        }}
        
        .step.active .step-number {{
            border-color: {SECONDARY_COLOR};
            color: {SECONDARY_COLOR};
        }}
    </style>
    """, unsafe_allow_html=True)

# Futuristic header with animation
def tech_header():
    st.markdown(f"""
    <div class="tech-header">
        <h1>PROMPT ENGINEERING NEXUS</h1>
        <p>Harness AI-powered prompt optimization with advanced processing techniques</p>
    </div>
    """, unsafe_allow_html=True)

# Processing animation with steps
def processing_animation():
    st.markdown("""
    <div class="loading-container">
        <div class="loading-brain">🧠</div>
        <div class="loading-bar"></div>
        <div class="loading-text">PROCESSING IN PROGRESS</div>
    </div>
    """, unsafe_allow_html=True)
    
# Show crew type badge
def show_crew_badge(crew_type):
    badge_icons = {
        "agent": "🤖",
        "short": "⚡",
        "long": "🔬"
    }
    
    badge_titles = {
        "agent": "FOR AGENT",
        "short": "PRECISION PROMPT",
        "long": "DEEP SYNTHESIS"
    }

 

# Tech style footer
def tech_footer():
    current_year = datetime.now().year
    st.markdown(f"""
    <div class="tech-footer">
        <p>PROMPT ENGINEERING NEXUS | v2.5.7 | © {current_year}</p>
    </div>
    """, unsafe_allow_html=True)

# Main app
def main():
    st.set_page_config(
        page_title="Prompt Engineering Nexus",
        page_icon="🧠",
        layout="wide",
        initial_sidebar_state="collapsed"
    )
    
    # Apply futuristic tech theme
    apply_tech_theme()
    
    # Display tech header
    tech_header()
    
    # Create three columns for better spacing
    left_col, main_col, right_col = st.columns([1, 10, 1])
    
    with main_col:
        # Create two columns for layout
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.markdown('<div class="tech-card">', unsafe_allow_html=True)
            st.markdown('<h2 class="form-header">CONFIGURATION</h2>', unsafe_allow_html=True)
            
            crew_type = st.selectbox(
                "Select Processing Type",
                ["agent", "short", "long"],
                format_func=lambda x: {
                    "agent": "🤖 Agents' Prompt Enhancer",
                    "short": "⚡ Precision Prompt Synthesizer",
                    "long": "🔬 Deep Context Processor"
                }[x]
            )
            

            
            st.markdown('</div>', unsafe_allow_html=True)
        
        with col2:
            st.markdown('<div class="tech-card">', unsafe_allow_html=True)
            st.markdown('<h2 class="form-header">INPUT PARAMETERS</h2>', unsafe_allow_html=True)
            
            with st.form("input_form"):
                if crew_type == "agent":
                    original_prompt = st.text_area("Original Prompt Matrix", height=200, 
                                                  placeholder="Enter the prompt you want to enhance with our neural network...")
                    inputs = {
                        "original_prompt": original_prompt,
                        "current_year": str(datetime.now().year),
                    }
                    
                elif crew_type == "short":
                    prompt_task = st.text_input("Core Directive", 
                                               placeholder="Define the primary objective for this prompt...")
                    prompt_requirements = st.text_area("Parameter Constraints", 
                                                     placeholder="Specify the required parameters and constraints...")
                    output_format = st.text_area("Output Schema", 
                                               placeholder="Define the expected output structure and format...")
                    additional_instructions = st.text_area("Auxiliary Directives", 
                                                         placeholder="Any supplementary instructions or guidelines...")
                    
                    inputs = {
                        "prompt_task": prompt_task,
                        "prompt_requirements": prompt_requirements,
                        "output_format": output_format,
                        "additional_instructions": additional_instructions,
                        "current_year": str(datetime.now().year),
                    }
                    
                elif crew_type == "long":
                    prompt_task = st.text_input("Primary Objective", 
                                              placeholder="Define the comprehensive task for this prompt...")
                    prompt_requirements = st.text_area("Detailed Parameters", 
                                                     placeholder="List all requirements, constraints, and conditions...")
                    output_format = st.text_area("Response Architecture", 
                                               placeholder="Describe the complete output structure and format...")
                    
                    inputs = {
                        "prompt_task": prompt_task,
                        "prompt_requirements": prompt_requirements,
                        "output_format": output_format,
                        "current_year": str(datetime.now().year),
                    }
                
                st.markdown("""
                <div style="display: flex; justify-content: flex-end; margin-top: 1.5rem;">
                </div>
                """, unsafe_allow_html=True)
                
                submitted = st.form_submit_button("PROCESS")
            
            st.markdown('</div>', unsafe_allow_html=True)
        
        # Process submission
        if submitted:
            try:
                # Show processing animation
                processing_animation()
                
                # Run the selected crew (original logic)
                md_path = run_crew(crew_type, inputs)
                
                if os.path.exists(md_path):
                    with open(md_path, "r", encoding="utf-8") as f:
                        result = f.read()
                    
                    st.markdown('<div class="tech-card">', unsafe_allow_html=True)
                    st.markdown('<h2 class="form-header">RESULTS</h2>', unsafe_allow_html=True)
                    
                    # Create tabs for different views of the output
                    tab1, tab2, tab3 = st.tabs(["🔮 PREVIEW", "📟 RAW CODE", "💾 EXPORT"])
                    
                    with tab1:
                        st.markdown(result)
                    
                    with tab2:
                        st.markdown('<div class="terminal-output">', unsafe_allow_html=True)
                        st.code(result, language="markdown")
                        st.markdown('</div>', unsafe_allow_html=True)
                    
                    with tab3:
                        col1, col2 = st.columns(2)
                        
                        with col1:
                            st.download_button(
                                label="📥 DOWNLOAD MARKDOWN",
                                data=result,
                                file_name=os.path.basename(md_path),
                                mime="text/markdown"
                            )
                        
                        with col2:
                            st.download_button(
                                label="📤 EXPORT AS TXT",
                                data=result,
                                file_name=os.path.splitext(os.path.basename(md_path))[0] + ".txt",
                                mime="text/plain"
                            )
                    
                    st.markdown('</div>', unsafe_allow_html=True)
                    
                    # Show success message
                    st.markdown("""
                    <div class="success-message">
                        <h3>✅ PROCESSING COMPLETE</h3>
                        <p>Your optimized prompt has been successfully synthesized.</p>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    
                    st.markdown('</div>', unsafe_allow_html=True)
                    
                else:
                    st.markdown("""
                    <div class="error-message">
                        <h3>⚠️ SYNTHESIS ERROR</h3>
                        <p>Output file not found. Processing was interrupted.</p>
                    </div>
                    """, unsafe_allow_html=True)
                    
            except Exception as e:
                st.markdown(f"""
                <div class="error-message">
                    <h3>🚨 CRITICAL ERROR</h3>
                    <p>System encountered an exception: {e}</p>
                    <p>Please recalibrate your parameters and try again.</p>
                </div>
                """, unsafe_allow_html=True)
    
    # Add footer
    tech_footer()

if __name__ == "__main__":
    main()