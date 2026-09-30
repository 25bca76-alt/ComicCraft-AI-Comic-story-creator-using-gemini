from pathlib import Path


def build_comic_layout(
    story: list[dict],
    image_paths: list[Path]
):

    layout = []


    for panel, image_path in zip(
        story,
        image_paths
    ):

        layout.append({

            "panel_number":
                panel["panel_number"],

            "title":
                panel["title"],

            "scene_description":
                panel["scene_description"],

            "image_prompt":
                panel["image_prompt"],

            "caption":
                panel.get("caption", ""),

            "narration":
                panel.get("narration", ""),

            "image_path":
                f"/static/panels/{image_path.name}",

            "local_image_path":
                str(image_path)
        })


    return layout