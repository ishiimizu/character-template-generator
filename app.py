# Character Template Generator - Streamlit Version

import streamlit as st
import tiktoken

st.set_page_config(page_title="Character Template Generator", layout="centered")
st.title("🧠 Character Template Generator")

# --- Integrated Guides Section ---
st.markdown("""
### 📘 Reference Guides
- 📄 [Character Creation Guide](https://docs.google.com/document/d/1bEtS5YNWuZ4--ji8sfL5Cf8UCBsYeXxYpiKuaX6kLoo/edit)
- ✳️ [F++ Format Extended Guide](https://docs.google.com/document/d/1pa_6OyVh1r72Hhz1EqITrf3gzBzu6eC_HixSxeni3oY/edit)
- 🧾 [AI Character Writing Styles Guide](https://docs.google.com/document/d/13T_HTVxtAYBqhBwcQBQv3NCSLEGKuhifer-QrHkVcpw/edit)
""")

# --- Instructions ---
st.markdown("""
### How to Use This App
1. Enter your **character's name**.
2. Choose the **template format**:
   - `F++` → Appearance & style
   - `S++` → Role/Scenario details
   - `P++` → Personality & logic
3. Pick if it’s an **Original** or **Adapted** character.
4. Click **Generate Template**.
5. Copy, save, or use as needed!

_Optional: Use example to autofill a sample character._
""")

st.set_page_config(page_title="Character Template Generator", layout="centered")
st.title("🧠 Character Template Generator")

# --- Instructions ---
st.markdown("""
### How to Use This App
1. Enter your **character's name**.
2. Choose the **template format**:
   - `F++` → Appearance & style
   - `S++` → Role/Scenario details
   - `P++` → Personality & logic
3. Pick if it’s an **Original** or **Adapted** character.
4. Click **Generate Template**.
5. Copy, save, or use as needed!

_Optional: Use example to autofill a sample character._
""")

# --- Generator Configuration ---
name = st.text_input("Character Name")
format_type = st.selectbox("Format Type", ["F++", "S++", "P++"])
character_type = st.selectbox("Character Type", ["Adapted Character", "Original Character"])
use_example = st.checkbox("Use Example")

# --- Token Counting (Updated with TikToken) ---
def count_tokens(text, model="gpt-3.5-turbo"):
    enc = tiktoken.encoding_for_model(model)
    tokens = enc.encode(text)
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
    Height("Tall")
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

# --- Generate Output ---
if st.button("Generate Template"):
    output = generate_character_template(name, format_type, character_type, use_example)
    token_count = count_tokens(output)
    st.code(output, language="markdown")
    st.success(f"Token Count: {token_count}")

# --- Trait Reference Section ---
st.markdown("""
<style>
.trait-box {
    border-radius: 10px;
    padding: 15px;
    margin-bottom: 20px;
    font-family: Arial;
    line-height: 1.6;
    background-color: rgba(255,255,255,0.1);
}
.trait-positive {
    border: 2px solid #4DA8DA;
}
.trait-neutral {
    border: 2px solid #FFB347;
}
.trait-negative {
    border: 2px solid #FF6F61;
}
.trait-title {
    font-weight: bold;
    font-size: 18px;
    margin-bottom: 10px;
}
</style>

<details>
<summary><strong>📚 Personality Traits Reference (Click to Expand)</strong></summary>
<br>
<div class="trait-box trait-positive">
    <div class="trait-title">💙 Positive Traits</div>
    Affectionate, Ambitious, Brave, Calm, Caring, Charismatic, Cheerful, Compassionate, Confident, Considerate, Cooperative, Courteous, Creative, Decisive, Determined, Diligent, Empathetic, Enthusiastic, Faithful, Flexible, Forgiving, Friendly, Generous, Gentle, Helpful, Honest, Hopeful, Humble, Imaginative, Independent, Innovative, Kind, Logical, Loyal, Loving, Mature, Modest, Motivated, Optimistic, Organized, Outgoing, Patient, Polite, Positive, Practical, Proactive, Rational, Reliable, Respectful, Responsible, Sincere, Sociable, Supportive, Thoughtful, Tolerant, Trustworthy, Understanding, Warm
</div>

<div class="trait-box trait-neutral">
    <div class="trait-title">🟠 Neutral Traits</div>
    Analytical, Assertive, Cautious, Competitive, Curious, Direct, Discreet, Dreamy, Emotional, Focused, Formal, Honest (blunt), Idealistic, Introspective, Methodical, Observant, Outspoken, Perfectionist, Quiet, Realistic, Reflective, Reserved, Sarcastic, Serious, Shy, Skeptical, Strategic, Studious, Tenacious, Thoughtful (pragmatic), Tidy, Tough, Unconventional, Witty
</div>

<div class="trait-box trait-negative">
    <div class="trait-title">❤️‍🔥 Negative Traits</div>
    Aggressive, Aloof, Anxious, Arrogant, Bossy, Clingy, Cold, Conceited, Cowardly, Critical, Cruel, Cynical, Deceitful, Defensive, Demanding, Dishonest, Disloyal, Disrespectful, Distrustful, Envious, Fearful, Foolish, Forgetful, Greedy, Grumpy, Gullible, Hostile, Impatient, Impulsive, Inconsiderate, Inflexible, Intolerant, Irresponsible, Jealous, Lazy, Manipulative, Moody, Naive, Neglectful, Obsessive, Overbearing, Paranoid, Passive, Pessimistic, Possessive, Reckless, Rude, Selfish, Stubborn, Suspicious, Tactless, Unfriendly, Ungrateful, Unreliable, Vain, Vindictive, Weak-willed
</div>
</details>

<details>
<summary><strong>🧍 Appearance Description Reference (Click to Expand)</strong></summary>
<br>
<div class="trait-box trait-positive">
    <div class="trait-title">🟢 Head and Face</div>
    Oval, Round, Square, Heart, Diamond, Long, Triangular, Oblong, Pear-shaped, Rectangular<br>
    Features: Cheeks (rosy, plump...), Chin (pointed, cleft...), Ears (delicate, pierced...), Eyes (bright, slanted...), Nose (button, aquiline...), etc.
</div>

<div class="trait-box trait-neutral">
    <div class="trait-title">💇 Hair</div>
    Texture (curly, straight...), Length (shoulder-length, waist-length...), Style (braided, ponytail...), Color (auburn, silver...), Accessories (clips, ribbons, beads...)
</div>

<div class="trait-box trait-negative">
    <div class="trait-title">🏋️ Body</div>
    Build (athletic, burly...), Posture (upright, slouched...), Shape (hourglass, pear...), Muscles, Fat Distribution, Body Hair, Body Movements (graceful, rigid...)
</div>

<div class="trait-box trait-positive">
    <div class="trait-title">🧴 Skin</div>
    Texture (smooth, rough...), Tone (fair, olive...), Complexion (glowing, dull...), Marks (freckles, scars...), Condition (healthy, dry...)
</div>
</details>
""", unsafe_allow_html=True)
