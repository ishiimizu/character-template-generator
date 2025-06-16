# streamlit_character_template_generator.py

import streamlit as st
from typing import Tuple

st.set_page_config(page_title="AI Character Template Generator", layout="wide")

# --- Helper Functions ---
def count_tokens(text: str) -> int:
    return len(text.split())

def get_example_template(name: str, format_type: str) -> str:
    examples = {
        "F++": f'''character("{name}") {{
    Gender("Female")
    Race("Human")
    Age("18")
    Height("Petite and toned, with nimble proportions")
    Nickname("Example")

    Appearance {{
        Hairstyle {{
            Type("Short bob cut, slightly angled toward the jawline.")
            Texture("Smooth and slightly layered for a natural look.")
            Details("Light bangs frame the forehead, adding a youthful charm.")
        }}
        HairColor("Jet black with a healthy sheen.")
        EyeColor {{
            Hue("Vibrant green")
            Shape("Almond-shaped")
            Expression("Thoughtful")
        }}
        BodyProportions {{
            Build("Slim and athletic")
            Posture("Upright")
            Features("Agile physique suited to physical activity.")
        }}
        Attire {{
            Top("White hoodie with pink stripe")
            Bottom("Light gray pleated skirt")
            Legwear("Fitted pink tights")
            Footwear("Sporty sneakers")
            Accessories("Minimalistic")
        }}
        OverallAura("Tough-yet-caring appearance")
    }}
}}''',
        "P++": f'''character("{name}") {{
    Gender("Female")
    Race("Human")
    Age("18")
    Height("Petite")
    Nickname("Example")

    Personality {{
        CoreTraits("Loyal, Brave, Curious")
        PositiveTraits("Friendly, Caring")
        NeutralTraits("Blunt, Independent")
        NegativeTraits("Reckless, Stubborn")
        Description("A curious and brave individual, driven by loyalty and a strong sense of justice.")
    }}
}}''',
        "S++": f'''character("{name}") {{
    Role("Combat Companion")
    Specialty("Close combat")
    CombatStyle("Reactive")
    ScenarioTags("Rescue, Raid")
    SampleDialogue("Stay behind me, I’ve got this!")
}}'''
    }
    return examples.get(format_type, "Invalid format type")

def get_blank_template(name: str, format_type: str) -> str:
    templates = {
        "F++": f'''character("{name}") {{
    Gender("")
    Race("")
    Age("")
    Height("")
    Nickname("")

    Appearance {{
        Hairstyle {{
            Type("")
            Texture("")
            Details("")
        }}
        HairColor("")
        EyeColor {{
            Hue("")
            Shape("")
            Expression("")
        }}
        BodyProportions {{
            Build("")
            Posture("")
            Features("")
        }}
        Attire {{
            Top("")
            Bottom("")
            Legwear("")
            Footwear("")
            Accessories("")
        }}
        OverallAura("")
    }}
}}''',
        "P++": f'''character("{name}") {{
    Gender("")
    Race("")
    Age("")
    Height("")
    Nickname("")

    Personality {{
        CoreTraits("")
        PositiveTraits("")
        NeutralTraits("")
        NegativeTraits("")
        Description("")
    }}
}}''',
        "S++": f'''character("{name}") {{
    Role("")
    Specialty("")
    CombatStyle("")
    ScenarioTags("")
    SampleDialogue("")
}}'''
    }
    return templates.get(format_type, "Invalid format type")

# --- Sidebar Inputs ---
st.sidebar.title("🛠️ Configuration")
name = st.sidebar.text_input("Character Name", value="Example")
format_type = st.sidebar.selectbox("Template Format", ["F++", "P++", "S++"])
character_type = st.sidebar.radio("Character Type", ["Adapted Character", "Original Character"])
use_example = st.sidebar.checkbox("Use Example Template", value=False)

# --- Main Display ---
st.title("🎭 AI Character Template Generator")
st.markdown("Use the sidebar to configure your template.")

# Generate Template
if use_example:
    result = get_example_template(name, format_type)
else:
    result = get_blank_template(name, format_type)

tokens = count_tokens(result)

st.subheader("📄 Generated Template")
st.code(result, language="text")
st.success(f"Token Count: {tokens}")

# Download Feature
st.download_button(
    label="💾 Download Template as .txt",
    data=result,
    file_name=f"{name}_template.txt",
    mime="text/plain"
)

# Spellcheck Help
with st.expander("🔧 Optional: Free Spell Check Tools"):
    st.markdown("- [🔗 LanguageTool](https://languagetool.org/)")
    st.markdown("- [🔗 GrammarCheck](https://www.grammarcheck.net/editor/)")
    st.markdown("- [🔗 Reverso Speller](https://www.reverso.net/spell-checker/english-spelling-grammar/)")

# Reference Sheet Expander
with st.expander("📚 Personality Trait Reference"):
    st.markdown("""
**Positive Traits**: Brave, Loyal, Kind, Optimistic, Humble  
**Neutral Traits**: Curious, Quiet, Determined, Blunt, Stoic  
**Negative Traits**: Impulsive, Jealous, Arrogant, Insecure, Reckless
    """)

with st.expander("📏 Appearance Description Reference"):
    st.markdown("""
**Height**: Petite and graceful / Tall and imposing / Short and agile  
**Build**: Lithe, Athletic, Sturdy, Curvy, Lean  
**Posture**: Upright and firm / Relaxed and casual / Swift and balanced
    """)

st.markdown("---")
st.markdown("Created with 💖 by Hiruko")
