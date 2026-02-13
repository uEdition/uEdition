"""Additional Sphinx directives for Room3b Videos."""

from docutils import nodes
from sphinx.transforms.post_transforms import SphinxPostTransform
from sphinx.util import logging
from sphinx.util.docutils import SphinxDirective
from sphinx_design.shared import create_component, is_component

logger = logging.getLogger(__name__)


class VideoDirective(SphinxDirective):
    """The VideoDirective directive is used to generate video block for videos."""

    has_content = False
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = True

    def run(self):
        """Create the AST for the directive."""
        video = create_component("room3b-video", rawtext=self.arguments[0], video_id=self.arguments[0])
        return [video]


class VideoHtmlTransform(SphinxPostTransform):
    """Transform video containers into the HTML specific AST structures."""

    default_priority = 198
    formats = ("html",)

    def run(self):
        """Run the transform."""
        document: nodes.document = self.document
        for node in document.findall(lambda node: is_component(node, "room3b-video")):
            video_id = node["video_id"]
            new_nodes = [
                nodes.raw(
                    "",
                    '<video class="video-js">'
                    f'<source src="https://video.room3b.eu/{video_id}.mp4" type="video/mp4"/>'
                    f'<track label="Subtitles" kind="subtitles" srclang="en" src="https://video.room3b.eu/{video_id}.vtt" />'  # noqa: E501
                    "</video>",
                    format="html",
                )
            ]
            node.replace_self(new_nodes)


def setup(app):
    """Set up the Video player extensions."""
    app.add_directive("room3b-video", VideoDirective)
    app.add_post_transform(VideoHtmlTransform)
    app.add_js_file("https://vjs.zencdn.net/8.23.4/video.min.js")
    app.add_js_file(
        None,
        body="""window.addEventListener('DOMContentLoaded', () => {
  for (let video of document.querySelectorAll('video')) {
    videojs(video, {
      aspectRatio: "16:9",
      controls: true,
      playbackRates: [0.5, 1, 1.5, 2, 3],
    });
  }
})""",
    )
    app.add_css_file("https://vjs.zencdn.net/8.23.4/video-js.css")
