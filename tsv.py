# Stage 1: Create the Album and Screen representations

class Artist:
    def __init__(self, name):
        self.name = name


class Album:
    def __init__(self, artist: Artist):
        self.artist = artist


class Field:
    def __init__(self, content):
        self.content = content


class Screen:
    def __init__(self, artist_field: Field):
        self.artist = artist_field


# Stage 1: Renderer that reads Album and Artist to create a structured format

class Stage1Renderer:
    def renderAlbum(self, album: Album):
        return f"Album by {album.artist.name}"

    def renderArtist(self, artist: Artist):
        return f"Artist: {artist.name}"


# Stage 2: Renderer that reads Screen and Field to create final HTML output

class Stage2Renderer:
    def renderScreen(self, screen: Screen):
        return f"<div>{screen.artist.content}</div>"

    def renderField(self, field: Field):
        return f"<span>{field.content}</span>"


# Creating HTML output

class HTML:
    def __init__(self):
        self.content = ""

    def addContent(self, content):
        self.content += content

    def render(self):
        return f"<html><body>{self.content}</body></html>"


# Example Usage

# Step 1: Create data objects
artist = Artist("The Beatles")
album = Album(artist)
field = Field("The Beatles Field Content")
screen = Screen(field)

# Step 2: Render intermediate formats
stage1_renderer = Stage1Renderer()
album_representation = stage1_renderer.renderAlbum(album)
artist_representation = stage1_renderer.renderArtist(artist)

# Step 3: Render final HTML using intermediate formats
stage2_renderer = Stage2Renderer()
screen_representation = stage2_renderer.renderScreen(screen)
field_representation = stage2_renderer.renderField(field)

# Step 4: Combine everything into an HTML document
html = HTML()
html.addContent(album_representation)
html.addContent(artist_representation)
html.addContent(screen_representation)
html.addContent(field_representation)

# Output HTML
print(html.render())
