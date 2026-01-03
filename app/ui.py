import streamlit as st
import json
from app.services import ArchitectureEngine


# --- MAIN UI LOGIC ---
def run_ui():
    st.set_page_config(page_title="ArchGen Pro", layout="wide", page_icon="🏗️")

    st.title("🏗️ ArchGen Pro: AI Solutions Architect")
    st.markdown("### Transform vague ideas into production-ready specs.")

    # Sidebar
    with st.sidebar:
        st.header("⚙️ Project Settings")
        st.info("Agentic Workflow Active")
        st.markdown(
            "- **Analyst Agent**: Llama-3-70b\n"
            "- **Architect Agent**: Llama-3-70b"
        )
        st.markdown("---")
        # st.caption("v1.0.0 | Internship Demo")

    # Input Area
    user_input = st.text_area(
        "Describe your project:",
        height=100,
        placeholder="e.g. A food delivery app like UberEats where users track orders in real-time."
    )

    if st.button("🚀 Generate Architecture", type="primary"):
        if not user_input:
            st.warning("Please describe your idea first.")
            return

        # Execution Pipeline
        with st.status("🤖 AI Agents at work...", expanded=True) as status:
            st.write("🕵️ **Analyst Agent:** Refining requirements...")
            refined_reqs = ArchitectureEngine.agent_analyst(user_input)

            st.write("👷 **Architect Agent:** Designing system & DB schema...")
            spec_json = ArchitectureEngine.agent_architect(refined_reqs)

            status.update(
                label="✅ Architecture Generated Successfully!",
                state="complete",
                expanded=False
            )

        # Output Tabs (NO DIAGRAMS)
        tab1, tab2, tab3 = st.tabs(["📄 Specs", "🗄️ Database", "🔌 APIs"])

        with tab1:
            st.subheader("Functional Requirements")
            st.markdown(refined_reqs)

            st.divider()
            st.subheader("System Modules")
            for mod in spec_json.get("modules", []):
                st.write(f"📦 {mod}")

            st.subheader("Recommended Tech Stack")
            st.write(", ".join(spec_json.get("tech_stack", [])))

        with tab2:
            st.subheader("Database Schema")
            st.json(spec_json.get("database_schema", []))

        with tab3:
            st.subheader("API Specification")
            st.table(spec_json.get("apis", []))

        # Export Feature
        full_report = (
            "# System Spec\n\n"
            "## Requirements\n"
            f"{refined_reqs}\n\n"
            "## Schema\n"
            f"{json.dumps(spec_json, indent=2)}"
        )

        st.download_button(
            "📥 Download MD Report",
            full_report,
            "architecture_spec.md"
        )
