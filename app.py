import gradio as gr
from brand_config import (
    BRAND_NAME,
    BUSINESS_DESCRIPTION,
    TARGET_AUDIENCE,
    CORE_SERVICES,
    BRAND_TONE,
    CONTENT_RULES,
)

def build_campaign(topic, platform, objective):
    if not topic.strip():
        return "Please enter a campaign topic first."

    audience = ", ".join(TARGET_AUDIENCE)
    services = ", ".join(CORE_SERVICES)
    rules = "\n".join(f"- {rule}" for rule in CONTENT_RULES)

    return f"""# {BRAND_NAME} — Campaign Brief

**Campaign topic:** {topic}
**Platform:** {platform}
**Objective:** {objective}

## Audience
{audience}

## Brand context
{BUSINESS_DESCRIPTION}

## Services
{services}

## Creative direction
{BRAND_TONE}

## Instructions for the campaign
{rules}

## Next step
This is the first campaign brief. In the next build stage, we will
connect an AI model so the Studio can generate finished campaign
ideas, adverts, social posts and visual prompts automatically.
"""

with gr.Blocks(title="SpeakPower Brand Promotion Studio") as demo:
    gr.Markdown("# SpeakPower Brand Promotion Studio")
    gr.Markdown("### Communication that moves people.")
    gr.Markdown(
        "Your online workspace for planning campaigns and creating "
        "promotional content for founders, executives and professionals."
    )

    with gr.Row():
        topic = gr.Textbox(
            label="What are we promoting?",
            placeholder="Example: Executive communication training",
            lines=2,
        )
    with gr.Row():
        platform = gr.Dropdown(
            ["LinkedIn", "WhatsApp", "Facebook", "Instagram", "Multi-platform"],
            value="LinkedIn",
            label="Main platform",
        )
        objective = gr.Dropdown(
            [
                "Build brand awareness",
                "Generate enquiries",
                "Promote a service",
                "Grow an audience",
                "Promote an event or training",
            ],
            value="Promote a service",
            label="Campaign objective",
        )

    create = gr.Button("Create campaign brief", variant="primary")
    output = gr.Markdown(label="Campaign brief")
    create.click(
        fn=build_campaign,
        inputs=[topic, platform, objective],
        outputs=output,
    )

if __name__ == "__main__":
    demo.launch()
