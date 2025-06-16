# Character Template Generator - Streamlit Version

import streamlit as st
import re

st.set_page_config(page_title="Character Template Generator", layout="centered")
st.title("🧠 Character Template Generator")

# --- Instructions and Guide Links ---
st.markdown("""
### How to Use This App
1. Enter your **character's name**.
2. Choose the **template format**:
   - `F++` → Appearance & style
   - `S++` → Role/Scenario details
   - `P++` → Personality & logic
3. Pick if it’s an **Original** or **Adapted** character.
4. Click **Generate Template**.
5. Edit, copy, save, or use as needed!

📖 **Helpful Writing Guides**:
- [🧬 Character Creation Guide](https://docs.google.com/document/d/1bEtS5YNWuZ4--ji8sfL5Cf8UCBsYeXxYpiKuaX6kLoo/edit?usp=sharing)
- [🧠 F++ Format Extended Guide](https://docs.google.com/document/d/1pa_6OyVh1r72Hhz1EqITrf3gzBzu6eC_HixSxeni3oY/edit?usp=sharing)
- [📝 Writing Styles Guide](https://docs.google.com/document/d/13T_HTVxtAYBqhBwcQBQv3NCSLEGKuhifer-QrHkVcpw/edit?usp=sharing)

_Optional: Use example to autofill a sample character._
""")

# --- Reference Section: Traits ---
with st.expander("📚 Personality Traits Reference", expanded=False):
    st.markdown("""
    <div style='background-color: rgba(255, 255, 255, 0.0); padding: 10px;'>
        <h4 style='color: #D6336C;'>Core Traits</h4>
        - Courageous, Loyal, Resilient, Determined, Adaptable

        <h4 style='color: #4C6EF5;'>Positive Traits</h4>
        - Friendly, Humble, Caring, Open-Minded, Observant, Generous, Patient

        <h4 style='color: #12B886;'>Neutral Traits</h4>
        - Curious, Independent, Practical, Street-Smart, Blunt, Guarded

        <h4 style='color: #F59F00;'>Negative Traits</h4>
        - Naïve, Impulsive, Rebellious, Risk-Taker, Overconfident, Stubborn
    </div>
    """, unsafe_allow_html=True)

# --- Reference Section: Appearance ---
with st.expander("🪞 Appearance Description Reference", expanded=False):
    st.markdown("""
    <div style='background-color: rgba(255, 255, 255, 0.0); padding: 10px;'>
        <h4 style='color: #1C7ED6;'>Hairstyle</h4>
        - Type: Ponytail, bob cut, layered, etc.
        - Texture: Curly, smooth, tousled...
        - Details: Fringe, side part, volume, etc.

        <h4 style='color: #1C7ED6;'>Eye Color</h4>
        - Hue: Emerald, amber, ocean blue...
        - Shape: Almond, round, slanted...
        - Expression: Intense, calm, playful...

        <h4 style='color: #1C7ED6;'>Body Proportions</h4>
        - Build: Slim, athletic, broad...
        - Posture: Confident, slouched, elegant...
        - Features: Defined jaw, soft cheeks, etc.

        <h4 style='color: #1C7ED6;'>Attire</h4>
        - Top, bottom, footwear, accessories
        - Style: Formal, casual, combat, fantasy...

        <h4 style='color: #1C7ED6;'>Overall Aura</h4>
        - Graceful, tough, mysterious, approachable...
    </div>
    """, unsafe_allow_html=True)

# --- Generator Configuration ---
name = st.text_input("Character Name")
format_type = st.selectbox("Format Type", ["F++", "S++", "P++"])
character_type = st.selectbox("Character Type", ["Adapted Character", "Original Character"])
use_example = st.checkbox("Use Example")

# --- Token Counting (Regex Version for Streamlit Compatibility) ---
def count_tokens(text):
    tokens = re.findall(r"\w+|[^\s\w]", text)
    return len(tokens)

# --- Template Generator Function ---
def generate_character_template(name, format_type, character_type, use_example):
    if use_example:
        example_insert = {
            "F++": f'''character("{name}") {{
    Gender("Female")
    Race("Human")
    Age("18")
    Height("Petite and toned, with nimble proportions")
    Nickname("Example")

    Appearance {{
        Hairstyle {{
            Type("Short bob cut, slightly angled toward the jawline.")
            Texture("Smooth and slightly layered for a natural, effortless look.")
            Details("Light bangs frame the forehead, adding a youthful charm.")
        }}

        HairColor("Jet black with a healthy sheen.")

        EyeColor {{
            Hue("Vibrant green with a soft and gentle undertone.")
            Shape("Almond-shaped, wide, and expressive.")
            Expression("Often thoughtful or slightly serious.")
        }}

        BodyProportions {{
            Build("Slim and athletic")
            Posture("Upright and composed")
            Features("Agile physique suited to an active lifestyle.")
        }}

        Attire {{
            Top("White hoodie with a pink stripe")
            Bottom("Light gray pleated skirt")
            Legwear("Fitted pink tights")
            Footwear("Sporty sneakers")
            Accessories("Minimalistic, functional.")
        }}

        OverallAura("Practical and laid-back appearance reflecting a tough-yet-caring spirit.")
    }}
}}''',
            "P++": f'''character("{name}") {{
    Gender("Female")
    Race("Human")
    Age("18")
    Height("Petite and athletic")
    Nickname("Example")

    Personality {{
        CoreTraits("Courageous, Loyal, Resilient, Determined, Adaptable")
        PositiveTraits("Friendly, Humble, Caring, Open-Minded, Observant")
        NeutralTraits("Practical, Independent, Street-Smart, Resourceful, Curious")
        NegativeTraits("Blunt, Rebellious, Naïve, Risk-Taker, Initially Guarded")
        Description("An adaptable fighter who's evolved from impulsiveness into someone driven by loyalty and purpose. She remains grounded through sarcasm, curiosity, and an unshakable will to grow.")
    }}
}}''',
            "S++": f'''character("{name}") {{
    Role("Combat Companion")
    Specialty("Close-quarters battle")
    CombatStyle("Aggressive and reactive")
    ScenarioTags("Dungeon Raid, Rival Hunter, Tense Rescue")
    SampleDialogue("I'll hold them off — just go!")
}}'''
        }
        return example_insert.get(format_type, "Invalid format type.")

    return f'''character("{name}") {{
    Gender("")
    Race("")
    Age("")
    Height("")
    Nickname("")

    {'Appearance {{\n        Hairstyle {{\n            Type("")\n            Texture("")\n            Details("")\n        }}\n        HairColor("")\n        EyeColor {{\n            Hue("")\n            Shape("")\n            Expression("")\n        }}\n        BodyProportions {{\n            Build("")\n            Posture("")\n            Features("")\n        }}\n        Attire {{\n            Top("")\n            Bottom("")\n            Legwear("")\n            Footwear("")\n            Accessories("")\n        }}\n        OverallAura("")\n    }}' if format_type == 'F++' else ''}

    {'Personality {{\n        CoreTraits("")\n        PositiveTraits("")\n        NeutralTraits("")\n        NegativeTraits("")\n        Description("")\n    }}' if format_type == 'P++' else ''}

    {'Role("")\n    Specialty("")\n    CombatStyle("")\n    ScenarioTags("")\n    SampleDialogue("")' if format_type == 'S++' else ''}
}}'''

# --- Generate Output and Editing ---
if st.button("Generate Template"):
    output = generate_character_template(name, format_type, character_type, use_example)
    edited_output = st.text_area("✏️ You can now edit your generated template below:", output, height=600)
    token_count = count_tokens(edited_output)
    st.success(f"Token Count: {token_count}")
    st.download_button("Download as .txt", edited_output, file_name=f"{name}_template.txt")
