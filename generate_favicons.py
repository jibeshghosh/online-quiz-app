import os
import math
import struct
import zlib

SVG_CONTENT = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100%" height="100%">
    <defs>
        <linearGradient id="logo-grad-fav" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#6366f1" />
            <stop offset="100%" stop-color="#a855f7" />
        </linearGradient>
        <filter id="logo-glow-fav" x="-20%" y="-20%" width="140%" height="140%">
            <feGaussianBlur stdDeviation="3" result="blur" />
            <feComposite in="SourceGraphic" in2="blur" operator="over" />
        </filter>
    </defs>
    <!-- Outer Q loop -->
    <path d="M 72.5 72.5 A 32 32 0 1 1 82 50 C 82 57 80 63 76.5 68" 
          fill="none" 
          stroke="url(#logo-grad-fav)" 
          stroke-width="8" 
          stroke-linecap="round" />
    
    <!-- The Q's synapse tail: curving down and right -->
    <path d="M 68 68 C 72 74, 76 82, 85 82" 
          fill="none" 
          stroke="url(#logo-grad-fav)" 
          stroke-width="8" 
          stroke-linecap="round" />
    
    <!-- Neural Synapse connections inside the Q -->
    <!-- Center node -->
    <circle cx="50" cy="50" r="7" fill="url(#logo-grad-fav)" filter="url(#logo-glow-fav)" />
    
    <!-- Other nodes -->
    <circle cx="38" cy="38" r="4.5" fill="#a855f7" />
    <circle cx="62" cy="38" r="4.5" fill="#6366f1" />
    <circle cx="44" cy="64" r="4.5" fill="#6366f1" />
    
    <!-- Synaptic pathways (lines connecting the nodes) -->
    <line x1="50" y1="50" x2="38" y2="38" stroke="url(#logo-grad-fav)" stroke-width="2.5" opacity="0.8" />
    <line x1="50" y1="50" x2="62" y2="38" stroke="url(#logo-grad-fav)" stroke-width="2.5" opacity="0.8" />
    <line x1="50" y1="50" x2="44" y2="64" stroke="url(#logo-grad-fav)" stroke-width="2.5" opacity="0.8" />
    <line x1="38" y1="38" x2="44" y2="64" stroke="url(#logo-grad-fav)" stroke-width="1.5" opacity="0.4" stroke-dasharray="3,3" />
    
    <!-- Small synaptic spark/pulse at the end of the tail -->
    <circle cx="85" cy="82" r="4" fill="#a855f7" filter="url(#logo-glow-fav)" />
</svg>"""

def create_png_bytes(width, height, draw_fn):
    rgba_pixels = []
    for y in range(height):
        for x in range(width):
            r, g, b, a = draw_fn(x, y, width, height)
            rgba_pixels.extend([r, g, b, a])
    
    raw_data = bytearray()
    for y in range(height):
        raw_data.append(0) # PNG filter type 0
        start = y * width * 4
        raw_data.extend(rgba_pixels[start:start + width * 4])
        
    compressed = zlib.compress(bytes(raw_data), level=9)
    
    def chunk(tag, data):
        return struct.pack('>I', len(data)) + tag + data + struct.pack('>I', zlib.crc32(tag + data) & 0xffffffff)

    header = b'\x89PNG\r\n\x1a\n'
    ihdr = chunk(b'IHDR', struct.pack('>IIBBBBB', width, height, 8, 6, 0, 0, 0))
    idat = chunk(b'IDAT', compressed)
    iend = chunk(b'IEND', b'')
    
    return header + ihdr + idat + iend

def create_ico_bytes(png_bytes, width=32, height=32):
    header = struct.pack('<HHH', 0, 1, 1)
    w_byte = 0 if width >= 256 else width
    h_byte = 0 if height >= 256 else height
    entry = struct.pack('<BBBBHHII', w_byte, h_byte, 0, 0, 1, 32, len(png_bytes), 6 + 16)
    return header + entry + png_bytes

def quiznapse_pixel_renderer(x, y, width, height):
    # Normalized coordinates 0..100
    nx = (x + 0.5) / width * 100.0
    ny = (y + 0.5) / height * 100.0
    
    # Background: transparent
    color = (0, 0, 0, 0)
    
    # Helper math
    dx = nx - 50.0
    dy = ny - 50.0
    dist = math.sqrt(dx*dx + dy*dy)
    angle = math.degrees(math.atan2(dy, dx)) % 360.0 # 0 to 360
    
    # Gradient colors: indigo #6366f1 (99,102,241) to purple #a855f7 (168,85,247)
    t = max(0.0, min(1.0, (nx + ny) / 200.0))
    gr = int(99 + t * (168 - 99))
    gg = int(102 + t * (85 - 102))
    gb = int(241 + t * (247 - 241))
    
    # 1. Outer Q ring: radius 32, stroke width 8 (r from 27 to 37)
    # Gap between ~ 35 deg and 65 deg (around bottom-right)
    in_ring_angle = not (35 <= angle <= 65)
    if 27.0 <= dist <= 37.0 and in_ring_angle:
        edge_dist = abs(dist - 32.0)
        alpha = max(0.0, min(1.0, (5.0 - edge_dist) / 1.5))
        if alpha > 0:
            color = (gr, gg, gb, int(255 * alpha))
            
    # 2. Q tail: curve from (68, 68) to (85, 82)
    tail_dx = nx - 76.5
    tail_dy = ny - 75.0
    tail_dist = math.sqrt(tail_dx*tail_dx + tail_dy*tail_dy)
    if tail_dist <= 7.0 and nx >= 65 and ny >= 65:
        alpha = max(0.0, min(1.0, (7.0 - tail_dist) / 1.5))
        if alpha > color[3]/255.0:
            color = (gr, gg, gb, int(255 * alpha))

    # 3. Synapse lines
    def line_dist(px, py, x1, y1, x2, y2):
        l2 = (x2-x1)**2 + (y2-y1)**2
        if l2 == 0: return math.sqrt((px-x1)**2 + (py-y1)**2)
        t_line = max(0, min(1, ((px - x1)*(x2 - x1) + (py - y1)*(y2 - y1)) / l2))
        proj_x = x1 + t_line * (x2 - x1)
        proj_y = y1 + t_line * (y2 - y1)
        return math.sqrt((px - proj_x)**2 + (py - proj_y)**2)

    lines = [
        (50, 50, 38, 38, 2.5, 0.8),
        (50, 50, 62, 38, 2.5, 0.8),
        (50, 50, 44, 64, 2.5, 0.8),
    ]
    for lx1, ly1, lx2, ly2, lwidth, lopacity in lines:
        ld = line_dist(nx, ny, lx1, ly1, lx2, ly2)
        if ld <= lwidth:
            alpha = max(0.0, min(1.0, (lwidth - ld) / 1.0)) * lopacity
            if alpha > color[3]/255.0:
                color = (gr, gg, gb, int(255 * alpha))

    # 4. Nodes
    nodes = [
        (50, 50, 8.5, gr, gg, gb, 1.0),      # Center node
        (38, 38, 5.0, 168, 85, 247, 1.0),    # Node 1
        (62, 38, 5.0, 99, 102, 241, 1.0),    # Node 2
        (44, 64, 5.0, 99, 102, 241, 1.0),    # Node 3
        (85, 82, 4.5, 168, 85, 247, 1.0),    # Spark node
    ]
    for cx, cy, cr, nr, ng, nb, na in nodes:
        ndist = math.sqrt((nx - cx)**2 + (ny - cy)**2)
        if ndist <= cr:
            alpha = max(0.0, min(1.0, (cr - ndist) / 1.2)) * na
            if alpha > color[3]/255.0:
                color = (nr, ng, nb, int(255 * alpha))

    return color

def generate_favicons():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    static_dir = os.path.join(base_dir, 'static')
    os.makedirs(static_dir, exist_ok=True)
    
    # 1. Write SVG
    svg_path = os.path.join(static_dir, 'favicon.svg')
    with open(svg_path, 'w', encoding='utf-8') as f:
        f.write(SVG_CONTENT)
        
    # 2. Generate 32x32 PNG
    png_32_bytes = create_png_bytes(32, 32, quiznapse_pixel_renderer)
    png_path = os.path.join(static_dir, 'favicon.png')
    with open(png_path, 'wb') as f:
        f.write(png_32_bytes)
        
    # 3. Generate 32x32 ICO
    ico_bytes = create_ico_bytes(png_32_bytes, 32, 32)
    ico_path = os.path.join(static_dir, 'favicon.ico')
    with open(ico_path, 'wb') as f:
        f.write(ico_bytes)

    # 4. Generate 180x180 Apple Touch Icon PNG
    apple_bytes = create_png_bytes(180, 180, quiznapse_pixel_renderer)
    apple_path = os.path.join(static_dir, 'apple-touch-icon.png')
    with open(apple_path, 'wb') as f:
        f.write(apple_bytes)

    print("[FAVICON-GEN] Successfully generated favicons in static/")

if __name__ == '__main__':
    generate_favicons()
